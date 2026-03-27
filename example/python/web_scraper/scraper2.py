#!/usr/bin/env python3
"""
Website Creator Skill Scraper
Scrapes GitHub repos and other links to build a comprehensive SKILL.md file.

Requirements:
    pip install requests beautifulsoup4 PyGithub

Usage:
    python scrape_skill.py
    python scrape_skill.py --token YOUR_GITHUB_TOKEN  (recommended, avoids rate limits)
"""

import argparse
import time
import re
import json
from pathlib import Path
from urllib.parse import urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing dependencies. Run: pip install requests beautifulsoup4")
    exit(1)

# ─── All links from your list ────────────────────────────────────────────────

LINKS = [
    # Learning / Roadmaps
    "https://github.com/kamranahmedse/developer-roadmap",
    "https://github.com/freeCodeCamp/freeCodeCamp",
    "https://github.com/microsoft/Web-Dev-For-Beginners",
    "https://github.com/EbookFoundation/free-programming-books",
    "https://github.com/jwasham/coding-interview-university",
    "https://github.com/getify/You-Dont-Know-JS",
    "https://github.com/trekhleb/javascript-algorithms",
    "https://github.com/ryanmcdermott/clean-code-javascript",
    "https://github.com/lydiahallie/javascript-questions",
    "https://github.com/goldbergyoni/nodebestpractices",
    # CSS / HTML
    "https://github.com/tailwindlabs/tailwindcss",
    "https://github.com/twbs/bootstrap",
    "https://github.com/animate-css/animate.css",
    "https://github.com/necolas/normalize.css",
    "https://github.com/h5bp/html5-boilerplate",
    "https://github.com/saadeghi/daisyui",
    "https://github.com/jgthms/bulma",
    "https://github.com/IanLunn/Hover",
    "https://github.com/bradtraversy/design-resources-for-developers",
    "https://github.com/joshbuchea/HEAD",
    "https://github.com/ConnorAtheton/loaders.css",
    "https://github.com/scottjehl/picturefill",
    "https://github.com/Modernizr/Modernizr",
    "https://github.com/suitcss/suit",
    "https://github.com/tachyons-css/tachyons",
    # Frameworks
    "https://github.com/facebook/react",
    "https://github.com/vuejs/core",
    "https://github.com/angular/angular",
    "https://github.com/sveltejs/svelte",
    "https://github.com/vercel/next.js",
    "https://github.com/nuxt/nuxt",
    "https://github.com/remix-run/remix",
    "https://github.com/solidjs/solid",
    "https://github.com/jquery/jquery",
    "https://github.com/preactjs/preact",
    "https://github.com/alpinejs/alpine",
    "https://github.com/facebook/react-native",
    "https://github.com/ionic-team/ionic-framework",
    "https://github.com/electron/electron",
    "https://github.com/expo/expo",
    # 3D / WebGL / Graphics
    "https://github.com/mrdoob/three.js",
    "https://github.com/pmndrs/react-three-fiber",
    "https://github.com/BabylonJS/Babylon.js",
    "https://github.com/pixijs/pixijs",
    "https://github.com/greggman/twgl.js",
    "https://github.com/regl-project/regl",
    "https://github.com/d3/d3",
    "https://github.com/visgl/deck.gl",
    "https://github.com/cesiumgs/cesium",
    "https://github.com/aframevr/aframe",
    "https://github.com/processing/p5.js",
    "https://github.com/glslify/glslify",
    "https://github.com/stackgl/stackgl",
    "https://github.com/cabbibo/puck",
    "https://github.com/o-gl/ogl",
    "https://github.com/playcanvas/engine",
    "https://github.com/gpuweb/gpuweb",
    "https://github.com/KhronosGroup/glTF",
    "https://github.com/google/filament",
    "https://github.com/layabox/LayaAir",
    # State / Utilities
    "https://github.com/reduxjs/redux",
    "https://github.com/pmndrs/zustand",
    "https://github.com/tanstack/query",
    "https://github.com/axios/axios",
    "https://github.com/lodash/lodash",
    "https://github.com/moment/moment",
    "https://github.com/date-fns/date-fns",
    "https://github.com/chartjs/Chart.js",
    "https://github.com/immerjs/immer",
    "https://github.com/validatorjs/validator.js",
    "https://github.com/faker-js/faker",
    "https://github.com/SortableJS/Sortable",
    "https://github.com/iamkun/dayjs",
    "https://github.com/ReactiveX/rxjs",
    "https://github.com/jquense/yup",
    # Backend / Tooling
    "https://github.com/nodejs/node",
    "https://github.com/expressjs/express",
    "https://github.com/nestjs/nest",
    "https://github.com/strapi/strapi",
    "https://github.com/prisma/prisma",
    "https://github.com/supabase/supabase",
    "https://github.com/vitejs/vite",
    "https://github.com/webpack/webpack",
    "https://github.com/microsoft/typescript",
    "https://github.com/prettier/prettier",
    "https://github.com/eslint/eslint",
    "https://github.com/cypress-io/cypress",
    "https://github.com/jestjs/jest",
    "https://github.com/microsoft/playwright",
    "https://github.com/fastify/fastify",
    # Awesome lists & misc
    "https://github.com/sindresorhus/awesome",
    "https://github.com/vinta/awesome-python",
    "https://github.com/enaqx/awesome-react",
    "https://github.com/uhub/awesome-javascript",
    "https://github.com/neutralinojs/neutralinojs",
    "https://github.com/ripienaar/free-for-dev",
    "https://github.com/public-apis/public-apis",
    "https://github.com/sdras/awesome-actions",
    "https://github.com/Chalarangelo/30-seconds-of-code",
    "https://github.com/airbnb/javascript",
    "https://github.com/donnemartin/system-design-primer",
    "https://github.com/anthropics/claude-cookbooks",
    "https://github.com/dair-ai/Prompt-Engineering-Guide",
]

# ─── Helpers ─────────────────────────────────────────────────────────────────

def parse_github_repo(url):
    """Extract owner/repo from a GitHub URL."""
    match = re.match(r"https://github\.com/([^/]+)/([^/]+)/?$", url)
    if match:
        return match.group(1), match.group(2)
    return None, None

def github_api_headers(token=None):
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def fetch_github_repo(owner, repo, token=None, session=None):
    """Fetch repo metadata, README, and top-level file tree from GitHub API."""
    s = session or requests.Session()
    headers = github_api_headers(token)
    base = f"https://api.github.com/repos/{owner}/{repo}"
    data = {}

    # — Repo metadata —
    try:
        r = s.get(base, headers=headers, timeout=15)
        r.raise_for_status()
        meta = r.json()
        data["name"] = meta.get("full_name", f"{owner}/{repo}")
        data["description"] = meta.get("description", "")
        data["stars"] = meta.get("stargazers_count", 0)
        data["language"] = meta.get("language", "")
        data["topics"] = meta.get("topics", [])
        data["url"] = meta.get("html_url", "")
        data["homepage"] = meta.get("homepage", "")
    except Exception as e:
        print(f"  ✗ metadata error for {owner}/{repo}: {e}")
        data["name"] = f"{owner}/{repo}"
        data["description"] = ""
        data["stars"] = 0
        data["language"] = ""
        data["topics"] = []
        data["url"] = f"https://github.com/{owner}/{repo}"
        data["homepage"] = ""

    # — README —
    try:
        r = s.get(f"{base}/readme", headers={**headers, "Accept": "application/vnd.github.raw"}, timeout=15)
        if r.status_code == 200:
            text = r.text
            # Trim very long READMEs to first ~600 lines to keep file manageable
            lines = text.splitlines()
            if len(lines) > 600:
                text = "\n".join(lines[:600]) + f"\n\n... [README truncated at 600 lines, full length: {len(lines)} lines] ..."
            data["readme"] = text
        else:
            data["readme"] = "(no README found)"
    except Exception as e:
        print(f"  ✗ README error for {owner}/{repo}: {e}")
        data["readme"] = "(README fetch failed)"

    # — File tree (top level) —
    try:
        r = s.get(f"{base}/contents", headers=headers, timeout=15)
        if r.status_code == 200:
            files = [f["name"] for f in r.json() if isinstance(r.json(), list)]
            data["files"] = files
        else:
            data["files"] = []
    except Exception as e:
        data["files"] = []

    # — Latest release —
    try:
        r = s.get(f"{base}/releases/latest", headers=headers, timeout=10)
        if r.status_code == 200:
            rel = r.json()
            data["latest_release"] = rel.get("tag_name", "")
            data["release_date"] = rel.get("published_at", "")[:10]
        else:
            data["latest_release"] = ""
            data["release_date"] = ""
    except Exception:
        data["latest_release"] = ""
        data["release_date"] = ""

    return data

def fetch_generic_url(url, session=None):
    """Fallback: fetch a non-GitHub URL and extract text."""
    s = session or requests.Session()
    try:
        r = s.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        # Remove scripts/styles
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        text = soup.get_text(separator="\n", strip=True)
        lines = [l for l in text.splitlines() if l.strip()]
        return "\n".join(lines[:300])
    except Exception as e:
        return f"(fetch failed: {e})"

def format_repo_section(data, index):
    """Format a repo's data as a markdown section."""
    stars_fmt = f"{data['stars']:,}" if data['stars'] else "N/A"
    topics_str = ", ".join(data['topics']) if data['topics'] else "none"
    files_str = ", ".join(data['files'][:30]) if data['files'] else "N/A"
    release_str = f"{data['latest_release']} ({data['release_date']})" if data['latest_release'] else "N/A"

    section = f"""
---

## [{index}] {data['name']}

- **URL**: {data['url']}
- **Stars**: ⭐ {stars_fmt}
- **Primary Language**: {data['language'] or 'N/A'}
- **Topics**: {topics_str}
- **Homepage**: {data['homepage'] or 'N/A'}
- **Latest Release**: {release_str}
- **Top-level files**: {files_str}

### Description

{data['description'] or '(no description)'}

### README

```
{data['readme']}
```

"""
    return section

# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Scrape repos and build SKILL.md")
    parser.add_argument("--token", "-t", default=None,
                        help="GitHub personal access token (strongly recommended to avoid rate limiting)")
    parser.add_argument("--output", "-o", default="SKILL.md",
                        help="Output file name (default: SKILL.md)")
    parser.add_argument("--delay", "-d", type=float, default=1.0,
                        help="Delay in seconds between API calls (default: 1.0)")
    parser.add_argument("--start", type=int, default=0,
                        help="Start from index N (useful for resuming)")
    args = parser.parse_args()

    if not args.token:
        print("⚠️  No GitHub token provided. You will likely hit rate limits after ~60 requests.")
        print("   Get a free token at: https://github.com/settings/tokens")
        print("   Then run: python scrape_skill.py --token YOUR_TOKEN\n")

    session = requests.Session()
    session.headers.update({"User-Agent": "skill-scraper/1.0"})

    output_path = Path(args.output)
    all_results = []
    errors = []

    print(f"🔍 Scraping {len(LINKS)} links...\n")

    for i, url in enumerate(LINKS):
        if i < args.start:
            continue

        # Clean up Google search wrapper URLs
        clean_url = url
        if "google.com/search?q=" in url:
            match = re.search(r"q=(https://[^\s&]+)", url)
            if match:
                clean_url = match.group(1)
            else:
                print(f"  [{i+1}/{len(LINKS)}] Skipping malformed Google URL: {url}")
                continue

        print(f"  [{i+1}/{len(LINKS)}] {clean_url}")
        owner, repo = parse_github_repo(clean_url)

        if owner and repo:
            data = fetch_github_repo(owner, repo, token=args.token, session=session)
            data["source_url"] = clean_url
            all_results.append(("github", data))
        else:
            text = fetch_generic_url(clean_url, session=session)
            all_results.append(("generic", {"url": clean_url, "content": text}))

        # Save progress every 10 items
        if (i + 1) % 10 == 0:
            _write_output(output_path, all_results, partial=True)
            print(f"  💾 Progress saved to {output_path} ({i+1}/{len(LINKS)} done)")

        time.sleep(args.delay)

    _write_output(output_path, all_results, partial=False)
    print(f"\n✅ Done! Output written to: {output_path}")
    print(f"   Total repos scraped: {len([r for r in all_results if r[0] == 'github'])}")
    print(f"   File size: {output_path.stat().st_size / 1024 / 1024:.1f} MB")
    print(f"   Line count: {sum(1 for _ in output_path.open())}")

def _write_output(path, results, partial=False):
    """Write all collected results to the output file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write("""---
name: website-creator
description: >
  Comprehensive skill for building professional, modern websites and web applications.
  Use whenever the user wants to create, design, or improve any website, web app,
  landing page, dashboard, portfolio, e-commerce site, or any frontend/fullstack project.
  Covers HTML, CSS, JavaScript, all major frameworks (React, Vue, Angular, Svelte, Next.js,
  Nuxt, Remix), CSS libraries (Tailwind, Bootstrap, Bulma, DaisyUI), 3D/WebGL (Three.js,
  Babylon.js, Pixi.js), state management, testing, tooling, backend, and best practices.
  Trigger this skill for ANY web development task, even if the user just says "make me a website"
  or "build a landing page" without specifying a stack.
---

# Website Creator Skill

> Auto-generated from {count} sources. {partial_note}
> Generation date: {date}

This skill contains comprehensive reference data scraped from the most important
web development GitHub repositories and resources. Use it to make informed
decisions about libraries, frameworks, and best practices when building websites.

## Table of Contents

{toc}

---

""".format(
            count=len(results),
            partial_note="(PARTIAL — still generating)" if partial else "(COMPLETE)",
            date=__import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M"),
            toc="\n".join(
                f"- [{i+1}] {r[1].get('name', r[1].get('url', 'Unknown'))}"
                for i, r in enumerate(results)
            )
        ))

        for i, (kind, data) in enumerate(results):
            if kind == "github":
                f.write(format_repo_section(data, i + 1))
            else:
                f.write(f"\n---\n\n## [{i+1}] {data['url']}\n\n```\n{data['content']}\n```\n\n")

        f.write("\n\n---\n\n*End of Website Creator Skill*\n")

if __name__ == "__main__":
    main()
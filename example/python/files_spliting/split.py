#!/usr/bin/env python3
"""
split_html.py - Separe un ou plusieurs fichiers HTML en HTML + CSS + JS.

Usage:
  python split_html.py monsite.html
  python split_html.py a.html b.html c.html
  python split_html.py a.html b.html c.html --output-dir ./output
  python split_html.py --folder ./mes_sites
  python split_html.py --folder ./mes_sites --output-dir ./output
"""

import re
import sys
import argparse
from pathlib import Path


# ─────────────────────────────────────────────
# Extraction
# ─────────────────────────────────────────────

def extract_blocks(html, tag):
    """Extrait tous les blocs <tag>...</tag> et les remplace par des placeholders."""
    pattern = re.compile(rf'<{tag}[^>]*>(.*?)</{tag}>', re.DOTALL | re.IGNORECASE)
    blocks = []

    def replace(match):
        blocks.append(match.group(1))
        return f'___{tag.upper()}_PLACEHOLDER_{len(blocks) - 1}___'

    cleaned = pattern.sub(replace, html)
    return cleaned, blocks


def remove_external_tags(html):
    """Supprime les <link .css> et <script src=...> locaux deja presents."""
    html = re.sub(
        r'<link\s[^>]*rel=["\']stylesheet["\'][^>]*href=["\'][^"\']*\.css["\'][^>]*/?>',
        '', html, flags=re.IGNORECASE
    )
    html = re.sub(
        r'<script\s[^>]*src=["\'][^"\']*\.js["\'][^>]*>\s*</script>',
        '', html, flags=re.IGNORECASE
    )
    return html


def remove_comments_css(content):
    """Supprime les commentaires CSS /* ... */"""
    return re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)


def remove_comments_js(content):
    """
    Supprime les commentaires JS // et /* ... */
    Preserve les URLs (https://, http://).
    """
    # Supprimer les blocs /* ... */
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    # Supprimer les // ligne par ligne en protegeant les URLs
    result = []
    for line in content.split('\n'):
        protected = line.replace('https://', '__HTTPS__').replace('http://', '__HTTP__')
        cleaned = re.sub(r'//.*$', '', protected)
        cleaned = cleaned.replace('__HTTPS__', 'https://').replace('__HTTP__', 'http://')
        result.append(cleaned)
    return '\n'.join(result)


def clean_content(content):
    """Enleve les lignes vides en debut/fin de bloc."""
    lines = content.split('\n')
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return '\n'.join(lines)


# ─────────────────────────────────────────────
# Reconstruction du HTML
# ─────────────────────────────────────────────

def inject_links(html, css_filename, js_filename):
    """Injecte le <link> CSS dans <head> et le <script> avant </body>."""
    html = re.sub(r'___STYLE_PLACEHOLDER_\d+___\n?', '', html)
    html = re.sub(r'___SCRIPT_PLACEHOLDER_\d+___\n?', '', html)

    css_tag = f'<link rel="stylesheet" href="{css_filename}">'
    if '</head>' in html:
        html = html.replace('</head>', f'{css_tag}\n</head>', 1)
    else:
        html = css_tag + '\n' + html

    js_tag = f'<script src="{js_filename}"></script>'
    if '</body>' in html:
        html = html.replace('</body>', f'{js_tag}\n</body>', 1)
    else:
        html = html + '\n' + js_tag

    return html


def clean_blank_lines(html, max_consecutive=2):
    """Reduit les lignes vides consecutives."""
    result = []
    count = 0
    for line in html.split('\n'):
        if line.strip() == '':
            count += 1
            if count <= max_consecutive:
                result.append(line)
        else:
            count = 0
            result.append(line)
    return '\n'.join(result)


# ─────────────────────────────────────────────
# Traitement d'un fichier
# ─────────────────────────────────────────────

def split_html(input_path, output_dir=None, base_name=None):
    input_path = Path(input_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {input_path}")

    out_dir = Path(output_dir) if output_dir else input_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    name     = base_name or input_path.stem
    html_out = out_dir / f"{name}.html"
    css_out  = out_dir / f"{name}.css"
    js_out   = out_dir / f"{name}.js"

    print(f"\n  Source  : {input_path}")
    print(f"  Sortie  : {out_dir}")
    print(f"  Fichiers: {name}.html / {name}.css / {name}.js\n")

    # Lire avec gestion de l'encodage Windows
    try:
        with open(input_path, encoding='utf-8') as f:
            html = f.read()
    except UnicodeDecodeError:
        with open(input_path, encoding='utf-8-sig') as f:
            html = f.read()

    original_size = len(html.encode('utf-8'))

    # Traitement
    html = remove_external_tags(html)

    html, style_blocks  = extract_blocks(html, 'style')
    html, script_blocks = extract_blocks(html, 'script')

    css_content = '\n\n'.join(
        clean_content(remove_comments_css(b))
        for b in style_blocks if b.strip()
    )
    js_content = '\n\n'.join(
        clean_content(remove_comments_js(b))
        for b in script_blocks if b.strip()
    )

    html = clean_blank_lines(html)
    html = inject_links(html, f"{name}.css", f"{name}.js")

    # Ecrire les 3 fichiers
    with open(css_out,  'w', encoding='utf-8') as f:
        f.write(css_content + '\n')
    with open(js_out,   'w', encoding='utf-8') as f:
        f.write(js_content + '\n')
    with open(html_out, 'w', encoding='utf-8') as f:
        f.write(html)

    # Rapport
    def fmt(n):
        if n >= 1024 * 1024:
            return f"{n / 1024 / 1024:.1f} MB"
        return f"{n / 1024:.1f} KB"

    total_size = html_out.stat().st_size + css_out.stat().st_size + js_out.stat().st_size

    print(f"  {'Fichier':<28} {'Lignes':>8}   {'Taille':>10}")
    print(f"  {'-'*28}  {'-'*8}   {'-'*10}")
    for path in [html_out, css_out, js_out]:
        with open(path, encoding='utf-8') as f:
            nb_lines = sum(1 for _ in f)
        print(f"  {path.name:<28} {nb_lines:>8}   {fmt(path.stat().st_size):>10}")
    print(f"  {'-'*28}  {'-'*8}   {'-'*10}")
    print(f"  {'TOTAL':<28} {'':>8}   {fmt(total_size):>10}")
    print(f"\n  Source originale : {fmt(original_size)}")
    print(f"  CSS : {len(style_blocks)} bloc(s) extrait(s) | JS : {len(script_blocks)} bloc(s) extrait(s)")
    print(f"\n  Ouvre {html_out.name} dans ton navigateur")
    print(f"  (les 3 fichiers doivent rester dans le meme dossier)\n")


# ─────────────────────────────────────────────
# Point d'entree principal
# ─────────────────────────────────────────────

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Separe un ou plusieurs fichiers HTML en HTML + CSS + JS.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples :
  python split_html.py monsite.html
  python split_html.py a.html b.html c.html
  python split_html.py a.html b.html c.html --output-dir ./output
  python split_html.py --folder ./mes_sites
  python split_html.py --folder ./mes_sites --output-dir ./output
        """
    )
    parser.add_argument(
        'input',
        nargs='*',
        help='Fichier(s) HTML source (ex: a.html b.html c.html)'
    )
    parser.add_argument(
        '--output-dir', '-o',
        default=None,
        help='Dossier de sortie (defaut: meme dossier que chaque fichier source)'
    )
    parser.add_argument(
        '--name', '-n',
        default=None,
        help='Nom de base des fichiers generes (un seul fichier uniquement)'
    )
    parser.add_argument(
        '--folder', '-f',
        default=None,
        help='Traiter tous les .html dans un dossier (ex: --folder ./mes_sites)'
    )

    args = parser.parse_args()

    # Collecter les fichiers a traiter
    targets = []

    if args.folder:
        folder = Path(args.folder)
        if not folder.is_dir():
            print(f"Erreur : dossier introuvable : {folder}")
            sys.exit(1)
        found = sorted(folder.glob('*.html'))
        if not found:
            print(f"Aucun fichier .html trouve dans : {folder}")
            sys.exit(0)
        targets.extend(found)
        print(f"\n{len(found)} fichier(s) trouve(s) dans {folder}")

    if args.input:
        targets.extend(Path(p) for p in args.input)

    if not targets:
        parser.print_help()
        sys.exit(1)

    # --name n'a de sens que pour un seul fichier
    if args.name and len(targets) > 1:
        print("--name ignore car plusieurs fichiers sont traites.\n")
        args.name = None

    # Traiter chaque fichier
    total  = len(targets)
    ok     = 0
    errors = []

    for i, path in enumerate(targets, 1):
        if total > 1:
            print(f"\n[{i}/{total}] {'─' * 43}")
        try:
            split_html(str(path), args.output_dir, args.name)
            ok += 1
        except Exception as e:
            print(f"  Erreur sur {path.name} : {e}\n")
            errors.append(path.name)

    # Resume final si plusieurs fichiers
    if total > 1:
        print('=' * 47)
        print(f"  {ok}/{total} fichier(s) traite(s) avec succes")
        if errors:
            print(f"  Echecs : {', '.join(errors)}")
        print('=' * 47)
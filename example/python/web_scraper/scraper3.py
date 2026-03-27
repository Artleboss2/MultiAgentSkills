#!/usr/bin/env python3
"""
Website Metadata Extractor for Penetration Testing
Downloads hidden metadata from various file types on a target website.

Author: HackerAI
Usage: python metadata_extractor.py
"""

import requests
import os
import argparse
import urllib.parse
from pathlib import Path
import re
from bs4 import BeautifulSoup
import concurrent.futures
from urllib.parse import urljoin, urlparse
import mimetypes

class MetadataExtractor:
    def __init__(self, base_url, output_dir="downloads", max_workers=10):
        self.base_url = base_url
        self.output_dir = Path(output_dir)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.max_workers = max_workers
        
    def create_dirs(self):
        """Create output directories for different file types"""
        dirs = {
            'html': self.output_dir / 'html',
            'css': self.output_dir / 'css',
            'js': self.output_dir / 'js',
            'images': self.output_dir / 'images',
            'videos': self.output_dir / 'videos',
            'models': self.output_dir / '3d_models'
        }
        for dir_path in dirs.values():
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def get_page_content(self):
        """Fetch main page and parse for resources"""
        try:
            response = self.session.get(self.base_url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"[-] Failed to fetch {self.base_url}: {e}")
            return None
    
    def extract_resources(self, content):
        """Extract URLs for HTML, CSS, JS, images, videos, 3D models"""
        soup = BeautifulSoup(content, 'html.parser')
        resources = {'html': [], 'css': [], 'js': [], 'images': [], 'videos': [], 'models': []}
        
        # HTML files (links to other HTML pages)
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.endswith('.html') or href.endswith('.htm'):
                resources['html'].append(href)
        
        # CSS files
        for link in soup.find_all('link', rel='stylesheet', href=True):
            resources['css'].append(link['href'])
        
        # JS files
        for script in soup.find_all('script', src=True):
            resources['js'].append(script['src'])
        
        # Images
        for img in soup.find_all('img', src=True):
            resources['images'].append(img['src'])
        for img in soup.find_all('img', srcset=True):
            resources['images'].extend(img['srcset'].split(','))
        
        # Videos
        for video in soup.find_all('video', src=True):
            resources['videos'].append(video['src'])
        for source in soup.find_all('source', src=True):
            if source.parent.name in ['video', 'audio']:
                resources['videos'].append(source['src'])
        
        # 3D Models (common formats)
        model_patterns = [
            r'\.(gltf|glb|obj|fbx|dae|ply|stl)$',  # 3D model extensions
            r'three\.js', r'gltf', r'glb', r'model',  # Common 3D keywords
        ]
        
        # Scan inline scripts and links for 3D models
        scripts = soup.find_all('script')
        for script in scripts:
            if script.string:
                for pattern in model_patterns:
                    matches = re.findall(pattern, script.string, re.IGNORECASE)
                    for match in matches:
                        if match.endswith(('.gltf', '.glb', '.obj', '.fbx', '.dae', '.ply', '.stl')):
                            resources['models'].append(match)
        
        # Convert relative URLs to absolute
        domain = urlparse(self.base_url).netloc
        for category in resources:
            resources[category] = [self._normalize_url(url, domain) for url in resources[category]]
            resources[category] = list(set(resources[category]))  # Remove duplicates
        
        return resources
    
    def _normalize_url(self, url, domain):
        """Convert relative URLs to absolute"""
        parsed = urlparse(url)
        if not parsed.netloc:
            return urljoin(self.base_url, url)
        return url
    
    def download_file(self, url, category):
        """Download a single file with metadata preservation"""
        try:
            filename = os.path.basename(urlparse(url).path)
            if not filename:
                filename = f"{category}_{hash(url) % 10000}"
            
            # Clean filename
            filename = re.sub(r'[^\w\-\.]', '_', filename)
            
            output_path = self.output_dir / category / filename
            
            response = self.session.get(url, timeout=15, stream=True)
            response.raise_for_status()
            
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"[+] Downloaded: {url} -> {output_path}")
            return str(output_path)
            
        except Exception as e:
            print(f"[-] Failed to download {url}: {e}")
            return None
    
    def extract_metadata(self, file_path):
        """Extract metadata from downloaded files (basic implementation)"""
        try:
            from PIL import Image
            from PIL.ExifTags import TAGS
            
            if file_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.tiff']:
                with Image.open(file_path) as img:
                    exifdata = img.getexif()
                    metadata = {}
                    for tag_id, value in exifdata.items():
                        tag = TAGS.get(tag_id, tag_id)
                        metadata[tag] = value
                    return metadata if metadata else "No EXIF data found"
        except ImportError:
            print("[!] Install pillow for image metadata: pip install pillow")
        except Exception:
            pass
        
        return "Metadata extraction not implemented for this file type"
    
    def download_category(self, category, urls):
        """Download all files in a specific category"""
        print(f"\n[*] Downloading {category.upper()} files ({len(urls)} found)...")
        successful_downloads = []
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(self.download_file, url, category) for url in urls]
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    successful_downloads.append(result)
        
        return successful_downloads
    
    def run_extraction(self, categories):
        """Main extraction workflow"""
        print(f"[*] Starting metadata extraction from: {self.base_url}")
        print(f"[*] Target categories: {', '.join(categories)}")
        
        self.create_dirs()
        
        # Get page content and extract resources
        content = self.get_page_content()
        if not content:
            return
        
        resources = self.extract_resources(content)
        
        # Download selected categories
        all_downloads = {}
        for category in categories:
            if category in resources and resources[category]:
                downloads = self.download_category(category, resources[category])
                all_downloads[category] = downloads
        
        # Extract metadata from downloads
        print("\n[*] Extracting metadata...")
        for category, files in all_downloads.items():
            for file_path in files:
                metadata = self.extract_metadata(Path(file_path))
                if metadata != "Metadata extraction not implemented for this file type":
                    print(f"[*] Metadata from {file_path.name}: {metadata}")
        
        print(f"\n[+] Extraction complete! Files saved to: {self.output_dir.absolute()}")

def main():
    parser = argparse.ArgumentParser(description="Extract metadata from website resources")
    parser.add_argument("url", help="Target website URL")
    parser.add_argument("-o", "--output", default="downloads", help="Output directory")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of download threads")
    parser.add_argument("--all", action="store_true", help="Download all file types")
    
    args = parser.parse_args()
    
    # Available categories
    categories = ['html', 'css', 'js', 'images', 'videos', 'models']
    
    if args.all:
        selected_categories = categories
    else:
        print("Select file types to download (comma-separated):")
        print("html, css, js, images, videos, models")
        print("Or 'all' for everything")
        user_input = input("Enter categories: ").strip().lower()
        
        if user_input == 'all':
            selected_categories = categories
        else:
            selected_categories = [cat.strip() for cat in user_input.split(',') if cat.strip() in categories]
        
        if not selected_categories:
            print("No valid categories selected. Exiting.")
            return
    
    # Run extraction
    extractor = MetadataExtractor(args.url, args.output, args.threads)
    extractor.run_extraction(selected_categories)

if __name__ == "__main__":
    main()
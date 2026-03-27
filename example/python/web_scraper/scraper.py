#!/usr/bin/env python3
"""
Comprehensive Website Scraper for Pentesting
Extracts HTML, CSS, JS, images, and all linked assets.
Handles JavaScript-rendered content with Selenium.
"""

import os
import re
import time
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import argparse
from pathlib import Path
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class WebsiteScraper:
    def __init__(self, target_url, output_dir="scraped_site", use_selenium=True, headless=True):
        self.target_url = target_url
        self.base_url = urlparse(target_url).scheme + "://" + urlparse(target_url).netloc
        self.output_dir = Path(output_dir)
        self.use_selenium = use_selenium
        self.headless = headless
        
        # Create output directory structure
        self.output_dir.mkdir(exist_ok=True)
        self.html_dir = self.output_dir / "html"
        self.css_dir = self.output_dir / "css"
        self.js_dir = self.output_dir / "js"
        self.assets_dir = self.output_dir / "assets"
        
        for directory in [self.html_dir, self.css_dir, self.js_dir, self.assets_dir]:
            directory.mkdir(exist_ok=True)
        
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        
    def download_file(self, url, local_path):
        """Download a single file and save it locally."""
        try:
            response = self.session.get(url, timeout=10, stream=True)
            response.raise_for_status()
            
            with open(local_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            logger.info(f"Downloaded: {url} -> {local_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to download {url}: {str(e)}")
            return False

    def extract_and_save_assets(self, soup, base_url):
        """Extract CSS, JS, and other assets from BeautifulSoup object."""
        assets_saved = {}
        
        # Extract CSS
        for link in soup.find_all('link', rel='stylesheet'):
            href = link.get('href')
            if href:
                full_url = urljoin(base_url, href)
                filename = Path(urlparse(full_url).path).name or 'style.css'
                local_path = self.css_dir / filename
                if self.download_file(full_url, local_path):
                    link['href'] = str(local_path.relative_to(self.output_dir))
                    assets_saved.setdefault('css', []).append(full_url)
        
        # Extract JS
        for script in soup.find_all('script', src=True):
            src = script.get('src')
            full_url = urljoin(base_url, src)
            filename = Path(urlparse(full_url).path).name or 'script.js'
            local_path = self.js_dir / filename
            if self.download_file(full_url, local_path):
                script['src'] = str(local_path.relative_to(self.output_dir))
                assets_saved.setdefault('js', []).append(full_url)
        
        # Extract images and other assets
        for img in soup.find_all('img', src=True):
            src = img.get('src')
            full_url = urljoin(base_url, src)
            filename = Path(urlparse(full_url).path).name
            if filename:
                local_path = self.assets_dir / filename
                self.download_file(full_url, local_path)
                img['src'] = str(local_path.relative_to(self.output_dir))
        
        return assets_saved

    def get_dynamic_content(self, url):
        """Use Selenium to get JavaScript-rendered content."""
        if not self.use_selenium:
            return None
        
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        
        driver = webdriver.Chrome(options=chrome_options)
        try:
            logger.info(f"Loading {url} with Selenium...")
            driver.get(url)
            
            # Wait for page to fully load
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Additional wait for dynamic content
            time.sleep(3)
            
            html = driver.page_source
            logger.info("Selenium capture complete")
            return html
            
        except TimeoutException:
            logger.error("Selenium timeout")
            return None
        finally:
            driver.quit()

    def scrape(self):
        """Main scraping function."""
        logger.info(f"Starting scrape of {self.target_url}")
        
        # Try Selenium first for dynamic content
        html_content = self.get_dynamic_content(self.target_url)
        
        # Fallback to requests if Selenium fails
        if not html_content:
            logger.info("Falling back to requests...")
            try:
                response = self.session.get(self.target_url, timeout=15)
                response.raise_for_status()
                html_content = response.text
            except Exception as e:
                logger.error(f"Failed to fetch page: {str(e)}")
                return False
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract and save assets
        assets = self.extract_and_save_assets(soup, self.target_url)
        
        # Save main HTML
        main_filename = Path(urlparse(self.target_url).path).name or 'index.html'
        if main_filename == '/':
            main_filename = 'index.html'
        
        html_path = self.html_dir / main_filename
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        logger.info(f"Saved HTML: {html_path}")
        logger.info(f"Assets saved - CSS: {len(assets.get('css', []))}, JS: {len(assets.get('js', []))}")
        logger.info(f"Complete site saved to: {self.output_dir.absolute()}")
        
        return True

def main():
    parser = argparse.ArgumentParser(description="Comprehensive Website Scraper for Pentesting")
    parser.add_argument("url", help="Target URL to scrape")
    parser.add_argument("-o", "--output", default="scraped_site", help="Output directory")
    parser.add_argument("--no-selenium", action="store_true", help="Disable Selenium (static content only)")
    parser.add_argument("--no-headless", action="store_true", help="Show browser window (with Selenium)")
    
    args = parser.parse_args()
    
    scraper = WebsiteScraper(
        target_url=args.url,
        output_dir=args.output,
        use_selenium=not args.no_selenium,
        headless=not args.no_headless
    )
    
    success = scraper.scrape()
    if success:
        print(f"\n✅ Scraping complete! Files saved to: {scraper.output_dir.absolute()}")
        print(f"📁 Structure:")
        print(f"   ├── html/ (HTML files)")
        print(f"   ├── css/ (Stylesheets)")
        print(f"   ├── js/ (JavaScript files)")
        print(f"   └── assets/ (Images & other files)")
    else:
        print("❌ Scraping failed")

if __name__ == "__main__":
    main()
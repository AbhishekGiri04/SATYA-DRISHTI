from playwright.async_api import async_playwright
from .base_adapter import BaseAdapter
from bs4 import BeautifulSoup
import re
import requests

class TwitterAdapter(BaseAdapter):
    """Twitter/X adapter with fallback methods"""
    
    async def extract(self, url: str):
        """Extract tweet content with multiple fallback methods"""
        
        # Method 1: Try direct scraping first (faster)
        try:
            return await self._extract_direct(url)
        except:
            pass
        
        # Method 2: Try Playwright with stealth
        try:
            return await self._extract_playwright(url)
        except Exception as e:
            # Return error with helpful message
            return {
                "url": url,
                "platform": "twitter",
                "title": "Twitter/X Content",
                "author": "Unknown",
                "published_at": "",
                "text": "Unable to extract Twitter/X content due to platform restrictions. Please try with a direct text paste or screenshot analysis.",
                "meta_description": "Twitter content extraction blocked",
                "media": [],
                "html": "",
                "extraction_error": str(e)
            }
    
    async def _extract_direct(self, url: str):
        """Try direct HTTP request first"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract from meta tags
        meta_desc = soup.find("meta", property="og:description")
        if meta_desc and meta_desc.get("content"):
            content = meta_desc.get("content", "")
            if len(content) > 20 and "sign in" not in content.lower():
                return self._create_unified_output(
                    url=url,
                    platform="twitter",
                    title=content[:100],
                    author="Twitter User",
                    published_at="",
                    text=content,
                    meta_description=content[:200],
                    media=[]
                )
        
        raise ValueError("Direct extraction failed")
    
    async def _extract_playwright(self, url: str):
        """Playwright extraction with stealth"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            )
            page = await context.new_page()
            
            # Add stealth
            await page.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', {get: () => undefined})
            """)
            
            await page.goto(url, timeout=15000, wait_until='domcontentloaded')
            await page.wait_for_timeout(2000)  # Wait for content to load
            
            html_content = await page.content()
            await browser.close()
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Check if blocked
            page_text = soup.get_text().lower()
            if any(x in page_text for x in ["javascript is disabled", "sign in to x", "log in to twitter"]):
                raise ValueError("Twitter/X blocked access")
            
            # Extract tweet content
            text = ""
            author = ""
            
            # Try multiple selectors
            tweet_selectors = [
                '[data-testid="tweetText"]',
                '[data-testid="tweet"] span',
                'article div[lang]'
            ]
            
            for selector in tweet_selectors:
                elements = soup.select(selector)
                if elements:
                    text = ' '.join([elem.get_text().strip() for elem in elements[:3]])
                    if len(text) > 10:
                        break
            
            # Extract author
            author_selectors = [
                '[data-testid="User-Name"]',
                'article div[dir="ltr"] span'
            ]
            
            for selector in author_selectors:
                elem = soup.select_one(selector)
                if elem:
                    author = elem.get_text().strip()
                    break
            
            if not text or len(text) < 10:
                raise ValueError("Unable to extract tweet content")
            
            return self._create_unified_output(
                url=url,
                platform="twitter",
                title=text[:100],
                author=author or "Twitter User",
                published_at="",
                text=text,
                meta_description=text[:200],
                media=[]
            )

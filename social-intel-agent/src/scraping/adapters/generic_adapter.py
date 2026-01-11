from playwright.async_api import async_playwright
from .base_adapter import BaseAdapter
from bs4 import BeautifulSoup
import trafilatura
import requests

class GenericAdapter(BaseAdapter):
    """Generic web adapter with fallback methods"""
    
    async def extract(self, url: str):
        """Extract content with multiple fallback methods"""
        
        # Method 1: Try trafilatura with requests first (faster)
        try:
            return await self._extract_trafilatura(url)
        except:
            pass
        
        # Method 2: Try Playwright for JavaScript sites
        try:
            return await self._extract_playwright(url)
        except Exception as e:
            # Return minimal content with error info
            return {
                "url": url,
                "platform": "generic",
                "title": "Content Extraction Failed",
                "author": "",
                "published_at": "",
                "text": f"Unable to extract content from this URL. The site may require JavaScript or have access restrictions. Error: {str(e)[:100]}",
                "meta_description": "Content extraction failed",
                "media": [],
                "html": "",
                "extraction_error": str(e)
            }
    
    async def _extract_trafilatura(self, url: str):
        """Fast extraction using trafilatura"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        
        # Use trafilatura for main content
        text = trafilatura.extract(response.content) or ""
        
        if len(text) < 50:
            raise ValueError("Insufficient content extracted")
        
        # Parse metadata
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = ""
        if soup.title:
            title = soup.title.string or ""
        
        meta_desc = ""
        meta_tag = soup.find("meta", attrs={"name": "description"})
        if not meta_tag:
            meta_tag = soup.find("meta", property="og:description")
        if meta_tag:
            meta_desc = meta_tag.get("content", "")
        
        return self._create_unified_output(
            url=url,
            platform="generic",
            title=title,
            author="",
            published_at="",
            text=text,
            meta_description=meta_desc,
            media=[]
        )
    
    async def _extract_playwright(self, url: str):
        """Playwright extraction for JavaScript sites"""
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
            await page.wait_for_timeout(3000)  # Wait for JS to load
            
            html_content = await page.content()
            await browser.close()
            
            # Check if JavaScript is disabled message
            if "javascript is disabled" in html_content.lower():
                raise ValueError("Site requires JavaScript and blocks automated access")
            
            # Use trafilatura on the rendered HTML
            text = trafilatura.extract(html_content) or ""
            
            # Parse with BeautifulSoup for metadata
            soup = BeautifulSoup(html_content, 'html.parser')
            
            title = ""
            if soup.title:
                title = soup.title.string or ""
            
            meta_desc = ""
            meta_tag = soup.find("meta", attrs={"name": "description"})
            if not meta_tag:
                meta_tag = soup.find("meta", property="og:description")
            if meta_tag:
                meta_desc = meta_tag.get("content", "")
            
            if len(text) < 20:
                raise ValueError("Insufficient content extracted from rendered page")
            
            return self._create_unified_output(
                url=url,
                platform="generic",
                title=title,
                author="",
                published_at="",
                text=text,
                meta_description=meta_desc,
                media=[]
            )

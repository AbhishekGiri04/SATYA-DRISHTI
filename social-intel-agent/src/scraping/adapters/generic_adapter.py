from playwright.async_api import async_playwright
from .base_adapter import BaseAdapter
from bs4 import BeautifulSoup
import trafilatura

class GenericAdapter(BaseAdapter):
    """Generic web adapter using trafilatura and Playwright"""
    
    async def extract(self, url: str):
        """Extract content from any webpage"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            )
            page = await context.new_page()
            
            await page.goto(url, timeout=15000, wait_until='domcontentloaded')
            html_content = await page.content()
            await browser.close()
            
            # Use trafilatura for main content extraction
            text = trafilatura.extract(html_content) or ""
            
            # Parse with BeautifulSoup for metadata
            soup = BeautifulSoup(html_content, 'html.parser')
            
            title = ""
            if soup.title:
                title = soup.title.string or ""
            
            meta_desc = ""
            meta_tag = soup.find("meta", attrs={"name": "description"})
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

from playwright.async_api import async_playwright
from .base_adapter import BaseAdapter
from bs4 import BeautifulSoup

class TikTokAdapter(BaseAdapter):
    """TikTok adapter using Playwright"""
    
    async def extract(self, url: str):
        """Extract TikTok video using Playwright"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            )
            page = await context.new_page()
            
            await page.goto(url, timeout=15000, wait_until='domcontentloaded')
            content = await page.content()
            await browser.close()
            
            soup = BeautifulSoup(content, 'html.parser')
            
            # Extract from meta tags
            title = ""
            text = ""
            
            og_title = soup.find("meta", property="og:title")
            if og_title:
                title = og_title.get("content", "")
            
            og_desc = soup.find("meta", property="og:description")
            if og_desc:
                text = og_desc.get("content", "")
            
            return self._create_unified_output(
                url=url,
                platform="tiktok",
                title=title,
                author="",
                published_at="",
                text=text,
                meta_description=text[:200],
                media=[]
            )

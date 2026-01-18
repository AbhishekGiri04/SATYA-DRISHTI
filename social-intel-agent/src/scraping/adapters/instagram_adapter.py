from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
from .base_adapter import BaseAdapter
from bs4 import BeautifulSoup
import asyncio

class InstagramAdapter(BaseAdapter):
    """Instagram adapter using Playwright"""
    
    async def extract(self, url: str):
        """Extract Instagram post using Playwright"""
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                context = await browser.new_context(
                    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
                )
                page = await context.new_page()
                
                try:
                    await page.goto(url, timeout=10000, wait_until='domcontentloaded')
                    content = await page.content()
                except PlaywrightTimeout:
                    await browser.close()
                    return self._create_unified_output(
                        url=url,
                        platform="instagram",
                        title="Instagram Post",
                        author="",
                        published_at="",
                        text="Instagram content extraction timed out. Please try a different URL.",
                        meta_description="",
                        media=[]
                    )
                
                await browser.close()
                
                soup = BeautifulSoup(content, 'html.parser')
                
                # Extract from meta tags
                title = ""
                text = ""
                author = ""
                
                og_title = soup.find("meta", property="og:title")
                if og_title:
                    title = og_title.get("content", "")
                
                og_desc = soup.find("meta", property="og:description")
                if og_desc:
                    text = og_desc.get("content", "")
                
                return self._create_unified_output(
                    url=url,
                    platform="instagram",
                    title=title or "Instagram Post",
                    author=author,
                    published_at="",
                    text=text or "Instagram post content",
                    meta_description=text[:200] if text else "",
                    media=[]
                )
        except Exception as e:
            return self._create_unified_output(
                url=url,
                platform="instagram",
                title="Instagram Post",
                author="",
                published_at="",
                text=f"Error extracting Instagram content: {str(e)}",
                meta_description="",
                media=[]
            )

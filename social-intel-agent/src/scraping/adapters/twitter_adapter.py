from playwright.async_api import async_playwright
from .base_adapter import BaseAdapter
from bs4 import BeautifulSoup
import re

class TwitterAdapter(BaseAdapter):
    """Twitter/X adapter using Playwright"""
    
    async def extract(self, url: str):
        """Extract tweet content"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            )
            page = await context.new_page()
            
            await page.goto(url, timeout=15000, wait_until='domcontentloaded')
            html_content = await page.content()
            await browser.close()
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Check if blocked
            page_text = soup.get_text().lower()
            if any(x in page_text for x in ["sign in to x", "log in to twitter", "join x today"]):
                raise ValueError("Twitter/X requires authentication. Please use authenticated session.")
            
            # Extract from meta tags
            text = ""
            author = ""
            
            meta_desc = soup.find("meta", property="og:description")
            if meta_desc:
                content = meta_desc.get("content", "")
                content = re.sub(r'^.*?on X:\s*[\"\"\"]', '', content)
                content = re.sub(r'[\"\"\"]$', '', content)
                text = content
            
            title_tag = soup.find("title")
            if title_tag and "on X:" in title_tag.string:
                author = title_tag.string.split("on X:")[0].strip()
            
            if not text or len(text) < 10:
                raise ValueError("Unable to extract tweet content")
            
            return self._create_unified_output(
                url=url,
                platform="twitter",
                title=text[:100],
                author=author,
                published_at="",
                text=text,
                meta_description=text[:200],
                media=[]
            )

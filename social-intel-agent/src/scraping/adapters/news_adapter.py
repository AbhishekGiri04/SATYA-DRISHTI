import requests
import trafilatura
from bs4 import BeautifulSoup
from .base_adapter import BaseAdapter

class NewsAdapter(BaseAdapter):
    """News article adapter using trafilatura"""
    
    async def extract(self, url: str):
        """Extract news article content"""
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        html = response.text
        
        # Extract main content with trafilatura
        text = trafilatura.extract(html, include_comments=False, include_tables=False) or ""
        
        # Extract metadata with trafilatura
        metadata = trafilatura.extract_metadata(html)
        
        # Parse HTML for additional metadata
        soup = BeautifulSoup(html, 'html.parser')
        
        title = ""
        if metadata and metadata.title:
            title = metadata.title
        elif soup.title:
            title = soup.title.string or ""
        
        author = ""
        if metadata and metadata.author:
            author = metadata.author
        
        published_at = ""
        if metadata and metadata.date:
            published_at = metadata.date
        
        meta_desc = ""
        if metadata and metadata.description:
            meta_desc = metadata.description
        else:
            meta_tag = soup.find("meta", attrs={"name": "description"})
            if meta_tag:
                meta_desc = meta_tag.get("content", "")
        
        return self._create_unified_output(
            url=url,
            platform="news",
            title=title,
            author=author,
            published_at=published_at,
            text=text,
            meta_description=meta_desc,
            media=[]
        )

from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseAdapter(ABC):
    """Base adapter for all platform extractors"""
    
    @abstractmethod
    async def extract(self, url: str) -> Dict[str, Any]:
        """Extract content from URL and return unified format"""
        pass
    
    def _create_unified_output(self, **kwargs) -> Dict[str, Any]:
        """Create standardized output format"""
        return {
            "url": kwargs.get("url", ""),
            "platform": kwargs.get("platform", "unknown"),
            "title": kwargs.get("title", ""),
            "author": kwargs.get("author", ""),
            "published_at": kwargs.get("published_at", ""),
            "text": kwargs.get("text", ""),
            "meta_description": kwargs.get("meta_description", ""),
            "media": kwargs.get("media", []),
            "raw_html": kwargs.get("raw_html", "")
        }

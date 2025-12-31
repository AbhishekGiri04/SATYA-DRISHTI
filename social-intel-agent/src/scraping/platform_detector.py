from urllib.parse import urlparse
from typing import Literal

PlatformType = Literal["twitter", "reddit", "youtube", "instagram", "tiktok", "facebook", "news", "generic"]

class PlatformDetector:
    """Detects which platform a URL belongs to"""
    
    PLATFORM_PATTERNS = {
        "twitter": ["twitter.com", "x.com"],
        "reddit": ["reddit.com"],
        "youtube": ["youtube.com", "youtu.be"],
        "instagram": ["instagram.com"],
        "tiktok": ["tiktok.com"],
        "facebook": ["facebook.com", "fb.com"],
    }
    
    NEWS_DOMAINS = [
        "cnn.com", "bbc.com", "nytimes.com", "theguardian.com", "reuters.com",
        "apnews.com", "bloomberg.com", "wsj.com", "washingtonpost.com", "forbes.com"
    ]
    
    def detect(self, url: str) -> PlatformType:
        """Detect platform from URL"""
        parsed = urlparse(url)
        domain = parsed.netloc.replace("www.", "").lower()
        
        # Check social media platforms
        for platform, patterns in self.PLATFORM_PATTERNS.items():
            if any(pattern in domain for pattern in patterns):
                return platform
        
        # Check if it's a news site
        if any(news_domain in domain for news_domain in self.NEWS_DOMAINS):
            return "news"
        
        # Default to generic
        return "generic"

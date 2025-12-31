from .platform_detector import PlatformDetector
from .adapters import (
    TwitterAdapter, RedditAdapter, YouTubeAdapter,
    InstagramAdapter, TikTokAdapter, NewsAdapter, GenericAdapter
)

class UniversalExtractor:
    """Universal content extractor that routes to appropriate adapter"""
    
    def __init__(self):
        self.detector = PlatformDetector()
        self.adapters = {
            "twitter": TwitterAdapter(),
            "reddit": RedditAdapter(),
            "youtube": YouTubeAdapter(),
            "instagram": InstagramAdapter(),
            "tiktok": TikTokAdapter(),
            "news": NewsAdapter(),
            "generic": GenericAdapter()
        }
    
    async def extract(self, url: str):
        """Detect platform and extract content using appropriate adapter"""
        platform = self.detector.detect(url)
        adapter = self.adapters.get(platform, self.adapters["generic"])
        
        try:
            result = await adapter.extract(url)
            result["detected_platform"] = platform
            return result
        except Exception as e:
            # Fallback to generic adapter if platform-specific fails
            if platform != "generic":
                result = await self.adapters["generic"].extract(url)
                result["detected_platform"] = "generic"
                result["fallback_reason"] = str(e)
                return result
            raise

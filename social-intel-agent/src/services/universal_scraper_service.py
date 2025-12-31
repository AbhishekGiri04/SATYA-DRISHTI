from src.scraping.universal_extractor import UniversalExtractor
from src.config.logger import setup_logger

logger = setup_logger(__name__)

class UniversalScraperService:
    """Universal scraper service using multi-adapter system"""
    
    def __init__(self):
        self.extractor = UniversalExtractor()
    
    async def scrape(self, url: str):
        """Scrape content using appropriate adapter"""
        logger.info(f"Extracting content from {url}")
        
        try:
            result = await self.extractor.extract(url)
            result['html'] = result.get('html', '')
            result['base_url'] = url.split('?')[0].rsplit('/', 1)[0]
            logger.info(f"Successfully extracted content from {result['platform']}")
            return result
        except Exception as e:
            logger.error(f"Extraction failed: {str(e)}")
            raise

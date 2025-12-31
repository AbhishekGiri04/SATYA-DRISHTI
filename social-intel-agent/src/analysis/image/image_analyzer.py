from src.analysis.image.image_extractor import ImageExtractor
from src.analysis.image.nsfw_image_detector import NSFWImageDetector
from src.analysis.image.violence_detector import ViolenceDetector
from src.analysis.image.religious_hate_detector import ReligiousHateDetector
from src.analysis.image.ocr_extractor import OCRExtractor
from src.config.logger import setup_logger

logger = setup_logger(__name__)

class ImageAnalyzer:
    def __init__(self):
        self.extractor = ImageExtractor()
        self.nsfw_detector = NSFWImageDetector()
        self.violence_detector = ViolenceDetector()
        self.religious_hate_detector = ReligiousHateDetector()
        self.ocr_extractor = OCRExtractor()
    
    def analyze_images(self, html: str, base_url: str, text_analyzer=None):
        """Analyze all images with comprehensive detection"""
        image_urls = self.extractor.extract_images(html, base_url)
        
        if not image_urls:
            return []
        
        results = []
        for url in image_urls[:10]:  # Limit to 10 images for performance
            logger.info(f"Analyzing image: {url}")
            image = self.extractor.download_image(url)
            
            if image is None:
                continue
            
            # Run all detectors
            nsfw = self.nsfw_detector.detect(image)
            violence = self.violence_detector.detect(image)
            religious_hate = self.religious_hate_detector.detect(image)
            ocr = self.ocr_extractor.extract_text(image)
            
            # Analyze OCR text if present
            ocr_analysis = None
            if ocr.get("text") and len(ocr.get("text", "").strip()) > 10 and text_analyzer:
                ocr_analysis = text_analyzer(ocr.get("text"))
            
            risk_score = self._calculate_image_risk(nsfw, violence, religious_hate, ocr, ocr_analysis)
            
            results.append({
                "image_url": url,
                "nsfw": nsfw,
                "violence": violence,
                "religious_hate": religious_hate,
                "ocr": ocr,
                "ocr_analysis": ocr_analysis,
                "image_risk_score": risk_score
            })
        
        return results
    
    def _calculate_image_risk(self, nsfw, violence, religious_hate, ocr, ocr_analysis):
        """Calculate comprehensive image risk score"""
        risk = 0
        
        # NSFW scoring (0-35 points)
        if nsfw.get("is_explicit"):
            risk += nsfw.get("confidence", 0) * 35
        elif nsfw.get("is_sexual"):
            risk += nsfw.get("confidence", 0) * 25
        elif nsfw.get("is_nsfw"):
            risk += nsfw.get("confidence", 0) * 20
        
        # Violence scoring (0-30 points)
        if violence.get("is_violent"):
            risk += violence.get("violence_score", 0) * 30
        
        # Hateful visual scoring (0-25 points)
        if violence.get("is_hateful_visual"):
            risk += violence.get("hate_score", 0) * 25
        
        # Religious hate scoring (0-30 points)
        if religious_hate.get("is_religious_hate"):
            risk += religious_hate.get("confidence", 0) * 30
        
        # Spam scoring (0-10 points)
        if violence.get("is_spam"):
            risk += violence.get("spam_score", 0) * 10
        
        # OCR text analysis (0-20 points)
        if ocr_analysis:
            ocr_risk = ocr_analysis.get("risk_assessment", {}).get("score", 0)
            risk += (ocr_risk / 100) * 20
        elif ocr.get("text") and len(ocr.get("text", "")) > 10:
            risk += 5  # Base bonus for text presence
        
        return min(int(risk), 100)

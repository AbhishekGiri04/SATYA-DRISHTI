import cv2
import numpy as np
from PIL import Image
import requests
from io import BytesIO
from src.analysis.image.nsfw_image_detector import NSFWImageDetector
from src.analysis.image.violence_detector import ViolenceDetector
from src.analysis.image.ocr_extractor import OCRExtractor
from src.config.logger import setup_logger

logger = setup_logger(__name__)

class VideoAnalyzer:
    def __init__(self):
        self.nsfw_detector = NSFWImageDetector()
        self.violence_detector = ViolenceDetector()
        self.ocr_extractor = OCRExtractor()
    
    def analyze_video_thumbnail(self, thumbnail_url: str):
        """Analyze video thumbnail for harmful content"""
        try:
            response = requests.get(thumbnail_url, timeout=10)
            image = Image.open(BytesIO(response.content)).convert('RGB')
            
            # Run image analysis on thumbnail
            nsfw = self.nsfw_detector.detect(image)
            violence = self.violence_detector.detect(image)
            ocr = self.ocr_extractor.extract_text(image)
            
            risk_score = self._calculate_thumbnail_risk(nsfw, violence, ocr)
            
            return {
                "thumbnail_url": thumbnail_url,
                "nsfw": nsfw,
                "violence": violence,
                "ocr": ocr,
                "risk_score": risk_score
            }
        except Exception as e:
            logger.error(f"Thumbnail analysis failed: {e}")
            return {"error": str(e)}
    
    def _calculate_thumbnail_risk(self, nsfw, violence, ocr):
        """Calculate risk score for video thumbnail"""
        risk = 0
        
        if nsfw.get("is_explicit"):
            risk += nsfw.get("confidence", 0) * 40
        elif nsfw.get("is_nsfw"):
            risk += nsfw.get("confidence", 0) * 25
        
        if violence.get("is_violent"):
            risk += violence.get("violence_score", 0) * 35
        
        if violence.get("is_hateful_visual"):
            risk += violence.get("hate_score", 0) * 30
        
        return min(int(risk), 100)
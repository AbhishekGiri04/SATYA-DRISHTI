import easyocr
import numpy as np
from src.config.logger import setup_logger

logger = setup_logger(__name__)

class OCRExtractor:
    def __init__(self):
        try:
            self.reader = easyocr.Reader(['en'], gpu=False, verbose=False)
            logger.info("EasyOCR initialized")
        except Exception as e:
            logger.error(f"EasyOCR init failed: {e}")
            self.reader = None
    
    def extract_text(self, image):
        if image is None or self.reader is None:
            return {"text": "", "confidence": 0.0}
        
        try:
            # Convert to numpy array if needed
            if not isinstance(image, np.ndarray):
                image = np.array(image)
            
            results = self.reader.readtext(image)
            
            if not results:
                logger.info("No text detected in image")
                return {"text": "", "confidence": 0.0}
            
            text = ' '.join([result[1] for result in results])
            avg_confidence = sum([result[2] for result in results]) / len(results)
            
            logger.info(f"OCR extracted: {text[:50]}... (confidence: {avg_confidence:.2f})")
            
            return {
                "text": text.strip(),
                "confidence": avg_confidence,
                "word_count": len(text.split())
            }
        except Exception as e:
            logger.error(f"OCR extraction failed: {e}")
            return {"text": "", "confidence": 0.0}

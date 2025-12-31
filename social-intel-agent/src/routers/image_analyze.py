from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.analysis.image.image_extractor import ImageExtractor
from src.analysis.image.nsfw_image_detector import NSFWImageDetector
from src.analysis.image.violence_detector import ViolenceDetector
from src.analysis.image.religious_hate_detector import ReligiousHateDetector
from src.analysis.image.ocr_extractor import OCRExtractor
from src.analysis.image.image_marker import ImageMarker
from src.config.logger import setup_logger

router = APIRouter()
logger = setup_logger(__name__)

class ImageAnalyzeRequest(BaseModel):
    image_url: str

@router.post("/analyze-image/")
async def analyze_image(request: ImageAnalyzeRequest):
    """Analyze a single image URL"""
    try:
        logger.info(f"Analyzing image: {request.image_url}")
        
        # Initialize detectors
        extractor = ImageExtractor()
        nsfw_detector = NSFWImageDetector()
        violence_detector = ViolenceDetector()
        religious_hate_detector = ReligiousHateDetector()
        ocr_extractor = OCRExtractor()
        marker = ImageMarker()
        
        # Download image
        image = extractor.download_image(request.image_url)
        
        if image is None:
            return {
                "status": "error",
                "message": "Failed to download image"
            }
        
        # Run all detectors
        logger.info("Running NSFW detection...")
        nsfw = nsfw_detector.detect(image)
        logger.info(f"NSFW result: {nsfw.get('is_nsfw')}, confidence: {nsfw.get('confidence')}")
        
        logger.info("Running violence detection...")
        violence = violence_detector.detect(image)
        
        logger.info("Running religious hate detection...")
        religious_hate = religious_hate_detector.detect(image, nsfw)
        
        logger.info("Running OCR extraction...")
        ocr = ocr_extractor.extract_text(image)
        logger.info(f"OCR result: text='{ocr.get('text', '')[:50]}', confidence={ocr.get('confidence')}")
        
        # Calculate confidence-based risk score
        risk_score = 0
        
        # NSFW contribution (0-35 points)
        nsfw_conf = nsfw.get("confidence", 0)
        if nsfw.get("is_explicit"):
            risk_score += nsfw_conf * 35
        elif nsfw.get("is_sexual"):
            risk_score += nsfw_conf * 25
        elif nsfw.get("is_nsfw"):
            risk_score += nsfw_conf * 20
        
        # Violence contribution (0-30 points)
        violence_conf = violence.get("violence_score", 0)
        if violence.get("is_violent"):
            risk_score += violence_conf * 30
        
        # Hateful visual contribution (0-25 points)
        hate_conf = violence.get("hate_score", 0)
        if violence.get("is_hateful_visual"):
            risk_score += hate_conf * 25
        
        # Religious hate contribution (0-40 points)
        religious_conf = religious_hate.get("confidence", 0)
        if religious_hate.get("is_religious_hate"):
            risk_score += religious_conf * 40
        
        # Spam contribution (0-10 points)
        spam_conf = violence.get("spam_score", 0)
        if violence.get("is_spam"):
            risk_score += spam_conf * 10
        
        risk_score = min(int(risk_score), 100)
        
        # Create detection dict for marking
        detections = {
            "nsfw": nsfw,
            "violence": violence,
            "religious_hate": religious_hate,
            "ocr": ocr
        }
        
        # Mark image with detections
        marked_image = marker.mark_image(image, detections)
        
        # Categorize image
        categorization = marker.categorize_image(detections)
        
        # Generate detailed report
        report = {
            "summary": f"Image classified as {categorization['primary_category'].upper()}",
            "detected_issues": [],
            "recommendations": []
        }
        
        if nsfw.get('is_nsfw'):
            report['detected_issues'].append("NSFW content detected")
            report['recommendations'].append("Content should be age-restricted")
        
        if violence.get('is_violent'):
            report['detected_issues'].append("Violent imagery detected")
            report['recommendations'].append("May require content warning")
        
        if violence.get('is_hateful_visual'):
            report['detected_issues'].append("Hateful symbols or imagery detected")
            report['recommendations'].append("Content violates community guidelines")
        
        if religious_hate.get('is_religious_hate'):
            report['detected_issues'].append("Religious hate content detected")
            if religious_hate.get('religious_symbols'):
                report['detected_issues'].append(f"Religious symbols: {', '.join(religious_hate.get('religious_symbols', []))}")
            if religious_hate.get('hate_context'):
                report['detected_issues'].append(f"Hate context: {', '.join(religious_hate.get('hate_context', []))}")
            report['recommendations'].append("Content should be removed immediately")
        
        if violence.get('is_spam'):
            report['detected_issues'].append("Spam or scam content detected")
            report['recommendations'].append("Mark as spam")
        
        if ocr.get('text'):
            report['detected_issues'].append(f"Text extracted: {ocr['text'][:100]}")
        
        if not report['detected_issues']:
            report['detected_issues'].append("No harmful content detected")
            report['recommendations'].append("Image is safe for general audiences")
        
        logger.info(f"Analysis complete - Risk: {risk_score}, Category: {categorization['primary_category']}, OCR: {bool(ocr.get('text'))}")
        
        return {
            "status": "success",
            "image_url": request.image_url,
            "risk_score": risk_score,
            "nsfw": {
                "is_nsfw": nsfw.get('is_nsfw', False),
                "is_explicit": nsfw.get('is_explicit', False),
                "is_sexual": nsfw.get('is_sexual', False),
                "confidence": nsfw.get('confidence', 0.0)
            },
            "violence": {
                "is_violent": violence.get('is_violent', False),
                "is_hateful_visual": violence.get('is_hateful_visual', False),
                "is_spam": violence.get('is_spam', False),
                "violence_score": violence.get('violence_score', 0.0),
                "hate_score": violence.get('hate_score', 0.0),
                "spam_score": violence.get('spam_score', 0.0)
            },
            "religious_hate": {
                "is_religious_hate": religious_hate.get('is_religious_hate', False),
                "confidence": religious_hate.get('confidence', 0.0),
                "religious_symbols": religious_hate.get('religious_symbols', []),
                "hate_context": religious_hate.get('hate_context', []),
                "extremist_symbols": religious_hate.get('extremist_symbols', [])
            },
            "ocr": {
                "text": ocr.get('text', ''),
                "confidence": ocr.get('confidence', 0.0)
            },
            "marked_image": marked_image,
            "categorization": categorization,
            "report": report
        }
        
    except Exception as e:
        logger.error(f"Image analysis failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

import warnings
warnings.filterwarnings('ignore', message='.*image_processor_type.*')

from transformers import pipeline

class NSFWImageDetector:
    def __init__(self):
        try:
            # Lightweight and accurate NSFW detector
            self.classifier = pipeline("image-classification", model="Falconsai/nsfw_image_detection")
        except:
            self.classifier = None
    
    def detect(self, image):
        if not self.classifier or image is None:
            return {"is_nsfw": False, "is_explicit": False, "is_sexual": False, "confidence": 0.0}
        
        try:
            result = self.classifier(image)
            
            # Parse results for different NSFW categories
            scores = {r['label'].lower(): r['score'] for r in result}
            
            nsfw_score = scores.get('nsfw', 0.0)
            explicit_score = scores.get('explicit', nsfw_score)
            sexual_score = scores.get('sexual', nsfw_score)
            
            return {
                "is_nsfw": nsfw_score > 0.5,
                "is_explicit": explicit_score > 0.6,
                "is_sexual": sexual_score > 0.5,
                "confidence": max(nsfw_score, explicit_score, sexual_score),
                "scores": scores
            }
        except:
            return {"is_nsfw": False, "is_explicit": False, "is_sexual": False, "confidence": 0.0}

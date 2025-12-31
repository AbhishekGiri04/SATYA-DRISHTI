from transformers import pipeline

class NSFWDetector:
    """Detects sexual and explicit adult content"""
    
    def __init__(self):
        try:
            # Lightweight: NSFW_text_classifier (125MB)
            self.classifier = pipeline("text-classification", 
                                      model="michellejieli/NSFW_text_classifier")
        except:
            self.classifier = None
    
    def detect(self, text: str):
        if not self.classifier or not text or len(text) < 10:
            return {"is_nsfw": False, "confidence": 0.0, "matches": []}
        
        try:
            result = self.classifier(text[:512])
            is_nsfw = result[0]["label"] == "NSFW"
            confidence = result[0]["score"]
            
            return {
                "is_nsfw": is_nsfw,
                "confidence": confidence,
                "matches": []
            }
        except:
            return {"is_nsfw": False, "confidence": 0.0, "matches": []}

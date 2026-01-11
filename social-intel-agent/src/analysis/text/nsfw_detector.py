from transformers import pipeline

class NSFWDetector:
    """Detects sexual and explicit adult content"""
    
    def __init__(self):
        try:
            self.classifier = pipeline("zero-shot-classification", model="cross-encoder/nli-distilroberta-base")
        except:
            self.classifier = None
    
    def detect(self, text: str):
        if not self.classifier or not text or len(text) < 10:
            return {"is_nsfw": False, "confidence": 0.0, "categories": []}
        
        try:
            labels = ["sexual content", "explicit adult content", "pornography", "safe content"]
            result = self.classifier(text[:512], labels)
            
            nsfw_categories = []
            max_nsfw_score = 0.0
            
            for label, score in zip(result['labels'], result['scores']):
                if label != "safe content" and score > 0.5:
                    nsfw_categories.append(label)
                    max_nsfw_score = max(max_nsfw_score, score)
            
            return {
                "is_nsfw": len(nsfw_categories) > 0,
                "confidence": max_nsfw_score,
                "categories": nsfw_categories,
                "scores": {label: score for label, score in zip(result['labels'], result['scores'])}
            }
        except:
            return {"is_nsfw": False, "confidence": 0.0, "categories": []}

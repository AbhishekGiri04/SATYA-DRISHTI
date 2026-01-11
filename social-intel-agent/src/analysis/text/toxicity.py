from transformers import pipeline
import re

class ToxicityDetector:
    def __init__(self):
        try:
            self.classifier = pipeline("text-classification", model="martin-ha/toxic-comment-model")
        except:
            self.classifier = None
    
    def detect(self, text: str):
        if not self.classifier:
            return {"is_toxic": False, "confidence": 0.0}
        
        # Meta-context detection (Fix 2)
        meta_context = self._detect_meta_usage(text)
        
        result = self.classifier(text[:512])
        is_toxic = result[0]["label"] == "toxic"
        confidence = result[0]["score"]
        
        # Reduce confidence if meta-context detected
        if meta_context and is_toxic:
            confidence *= 0.4  # 60% reduction
        
        return {
            "is_toxic": is_toxic and confidence > 0.5,
            "confidence": confidence
        }
    
    def _detect_meta_usage(self, text: str) -> bool:
        """Detect if text is discussing toxicity rather than being toxic"""
        text_lower = text.lower()
        meta_patterns = [
            (r'\btoxic\b.*\bis\b', True),
            (r'\bcalled.*\btoxic\b', True),
            (r'\baccused.*\btoxic\b', True),
            (r'\blabeled.*\btoxic\b', True),
            (r'\bconsidered.*\btoxic\b', True),
            (r'\bwhat is\b.*\btoxic\b', True),
        ]
        
        for pattern, _ in meta_patterns:
            if re.search(pattern, text_lower):
                return True
        return False
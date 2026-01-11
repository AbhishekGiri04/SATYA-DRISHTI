from transformers import pipeline
import re

class IntentDetector:
    """Detects if content is reporting vs endorsing harmful content"""
    
    def __init__(self):
        try:
            self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        except:
            self.classifier = None
    
    def detect(self, text: str):
        if not self.classifier or not text or len(text) < 10:
            return {"intent": "unknown", "confidence": 0.0}
        
        try:
            # Fix 4: Split long text into chunks for better intent detection
            chunks = self._split_into_chunks(text, max_tokens=300)
            
            if len(chunks) == 0:
                return {"intent": "unknown", "confidence": 0.0}
            
            # Analyze each chunk
            labels = [
                "this text is reporting news about harmful content",
                "this text is endorsing harmful content",
                "this text is neutral discussion",
                "this text describes a personal experience"
            ]
            
            intent_scores = {"reporting": [], "endorsing": [], "neutral": [], "personal": []}
            
            for chunk in chunks:
                result = self.classifier(chunk, labels)
                
                for label, score in zip(result['labels'], result['scores']):
                    if "reporting news" in label:
                        intent_scores["reporting"].append(score)
                    elif "endorsing" in label:
                        intent_scores["endorsing"].append(score)
                    elif "personal experience" in label:
                        intent_scores["personal"].append(score)
                    else:
                        intent_scores["neutral"].append(score)
            
            # Average scores across chunks
            avg_scores = {k: sum(v)/len(v) if v else 0.0 for k, v in intent_scores.items()}
            
            # Determine primary intent
            primary_intent = max(avg_scores, key=avg_scores.get)
            confidence = avg_scores[primary_intent]
            
            return {
                "intent": primary_intent,
                "confidence": confidence,
                "all_scores": avg_scores
            }
        except Exception as e:
            return {"intent": "unknown", "confidence": 0.0}
    
    def _split_into_chunks(self, text: str, max_tokens: int = 300) -> list:
        """Split text into chunks of approximately max_tokens words"""
        # Clean text first
        text = re.sub(r'@\w+|u/\w+', '', text)
        text = re.sub(r'http\S+|www\S+', '', text)
        
        words = text.split()
        chunks = []
        
        for i in range(0, len(words), max_tokens):
            chunk = ' '.join(words[i:i+max_tokens])
            if len(chunk.strip()) > 20:  # Minimum chunk size
                chunks.append(chunk)
        
        return chunks if chunks else [text[:512]]

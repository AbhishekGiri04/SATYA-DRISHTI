from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        # Lightweight: distilbert-base-uncased (67MB)
        self.classifier = pipeline("sentiment-analysis", 
                                  model="distilbert-base-uncased-finetuned-sst-2-english")
    
    def analyze(self, text: str):
        result = self.classifier(text[:512])
        return {
            "label": result[0]["label"],
            "score": result[0]["score"]
        }
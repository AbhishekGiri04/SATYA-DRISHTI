from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.classifier = pipeline("sentiment-analysis")
    
    def analyze(self, text: str):
        result = self.classifier(text)
        return {
            "label": result[0]["label"],
            "score": result[0]["score"]
        }
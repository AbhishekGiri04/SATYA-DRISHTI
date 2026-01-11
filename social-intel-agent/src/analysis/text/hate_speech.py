from transformers import pipeline

class HateSpeechDetector:
    def __init__(self):
        try:
            self.classifier = pipeline("text-classification", model="Hate-speech-CNERG/dehatebert-mono")
        except:
            self.classifier = None
    
    def detect(self, text: str):
        if not self.classifier:
            return {"is_hate_speech": False, "confidence": 0.0, "label": "unknown"}
        
        result = self.classifier(text[:512])
        is_hate = result[0]["label"].lower() in ["hate", "offensive", "hateful"]
        
        return {
            "is_hate_speech": is_hate,
            "confidence": result[0]["score"],
            "label": result[0]["label"]
        }

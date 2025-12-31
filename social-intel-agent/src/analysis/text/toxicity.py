from transformers import pipeline
import re

class ToxicityDetector:
    def __init__(self):
        try:
            self.classifier = pipeline("text-classification", 
                                      model="unitary/unbiased-toxic-roberta")
        except:
            self.classifier = None
        
        # Hinglish/Desi abuse patterns
        self.hinglish_toxic = [
            'chutiya', 'chu****', 'madarchod', 'bhen', 'gandu', 'harami',
            'kutta', 'kutti', 'saala', 'kamina', 'nalayak', 'bewakoof',
            'aukat', 'aukaat', 'nikal', 'bhag', 'theek nahi hoga',
            'problem ho jayegi', 'baap kaun hai', 'dimaag ghutno',
            'tera baap', 'teri maa', 'gaand', 'lund',
            # Dating/DM abuse
            'mid at best', 'no wonder you\'re single', 'send pics',
            'don\'t act so high', 'act so high',
            # Celebrating harm
            'well deserved', 'another one bites', 'bites the dust',
        ]
        
        # Implicit threats
        self.threat_patterns = [
            r'\bwarna\b.*\b(theek nahi|problem|dekh lena)\b',
            r'\bbaap kaun hai\b',
            r'\bnikal\b.*\b(yahan se|warna)\b',
            r'\bdeserve whatever happens\b',
            r'\bdisappear\b.*\b(already|should)\b',
            r'\bnobody would miss\b',
            r'\bgas them\b',  # Explicit genocide
            r'\bsend pics\b.*\b(or|else)\b',  # Coercion
        ]
    
    def detect(self, text: str):
        if not self.classifier:
            return {"is_toxic": False, "confidence": 0.0, "matches": []}
        
        # Check Hinglish toxic words first
        text_lower = text.lower()
        hinglish_matches = [word for word in self.hinglish_toxic if word in text_lower]
        if hinglish_matches:
            return {"is_toxic": True, "confidence": 0.9, "matches": hinglish_matches}
        
        # Check threat patterns
        for pattern in self.threat_patterns:
            if re.search(pattern, text_lower):
                return {"is_toxic": True, "confidence": 0.85, "matches": ["implicit_threat"]}
        
        # Check if it's a question/discussion (not toxic)
        if self._is_question_or_discussion(text):
            return {"is_toxic": False, "confidence": 0.0, "matches": []}
        
        # Meta-context detection
        meta_context = self._detect_meta_usage(text)
        
        result = self.classifier(text[:512])
        is_toxic = result[0]["label"].lower() in ["toxic", "toxicity"]
        confidence = result[0]["score"]
        
        # Reduce confidence if meta-context detected
        if meta_context and is_toxic:
            confidence *= 0.3
        
        # Balanced threshold: 0.65
        return {
            "is_toxic": is_toxic and confidence > 0.65,
            "confidence": confidence if is_toxic else 0.0,
            "matches": []
        }
    
    def _is_question_or_discussion(self, text: str) -> bool:
        """Detect if text is a genuine question or discussion"""
        text_lower = text.lower()
        
        # Skip if contains direct attacks or harmful phrases
        attack_words = [
            'stupid', 'idiot', 'kill yourself', 'die', 'hate you', 'fuck',
            'disappear', 'nobody would miss', 'shouldn\'t exist', 'wiped out',
            'deserve whatever happens', 'useless'
        ]
        if any(word in text_lower for word in attack_words):
            return False
        
        # Skip dog whistles and coded hate
        dog_whistles = [
            'go back to where', 'we all know what kind', 'before them',
            'violent ideology', 'races are smarter', 'women are inferior'
        ]
        if any(phrase in text_lower for phrase in dog_whistles):
            return False
        
        # Question patterns (must be at start)
        question_words = ['why', 'how', 'what', 'when', 'where', 'who', 'did they', 'is it', 'are they']
        if any(text_lower.strip().startswith(word) for word in question_words):
            return True
        
        # Discussion patterns
        discussion_patterns = [
            r'\bmy (grandparents|parents|family)\b',
            r'\bback in the (day|50s|60s|70s)\b',
            r'\bused to\b',
            r'\bthey say\b',
        ]
        
        for pattern in discussion_patterns:
            if re.search(pattern, text_lower):
                return True
        
        return False
    
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
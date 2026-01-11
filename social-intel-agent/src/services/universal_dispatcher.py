from src.services.universal_scraper_service import UniversalScraperService
from src.analysis.text.sentiment import SentimentAnalyzer
from src.analysis.text.toxicity import ToxicityDetector
from src.analysis.text.hate_speech import HateSpeechDetector
from src.analysis.text.content_classifier import ContentClassifier
from src.analysis.text.intent_detector import IntentDetector
from src.analysis.text.nsfw_detector import NSFWDetector
from src.analysis.text.misinformation_detector import MisinformationDetector
from src.analysis.image.image_extractor import ImageExtractor
from src.analysis.image.nsfw_image_detector import NSFWImageDetector
from src.analysis.image.violence_detector import ViolenceDetector
from src.analysis.image.religious_hate_detector import ReligiousHateDetector
from src.analysis.image.ocr_extractor import OCRExtractor
from src.analysis.video.video_analyzer import VideoAnalyzer
from src.analysis.social.social_media_analyzer import SocialMediaAnalyzer
from src.analysis.scoring.risk_score import RiskScorer
from src.config.logger import setup_logger
import uuid
from datetime import datetime

logger = setup_logger(__name__)

class UniversalAnalysisDispatcher:
    """Universal analysis dispatcher with complete AI analysis"""
    
    def __init__(self):
        self.scraper = UniversalScraperService()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.toxicity_detector = ToxicityDetector()
        self.hate_speech_detector = HateSpeechDetector()
        self.content_classifier = ContentClassifier()
        self.intent_detector = IntentDetector()
        self.nsfw_detector = NSFWDetector()
        self.misinformation_detector = MisinformationDetector()
        self.image_extractor = ImageExtractor()
        self.nsfw_image_detector = NSFWImageDetector()
        self.violence_detector = ViolenceDetector()
        self.religious_hate_detector = ReligiousHateDetector()
        self.ocr_extractor = OCRExtractor()
        self.video_analyzer = VideoAnalyzer()
        self.social_media_analyzer = SocialMediaAnalyzer()
        self.risk_scorer = RiskScorer()
    
    async def analyze(self, url: str, deep_analysis: bool = False):
        """Complete analysis pipeline"""
        try:
            # Step 1: Extract content
            logger.info(f"Starting analysis for {url}")
            extracted_data = await self.scraper.scrape(url)
            
            text_content = extracted_data.get("text", "").strip()
            
            if not text_content or len(text_content) < 10:
                return {
                    "analysis_id": str(uuid.uuid4()),
                    "timestamp": datetime.utcnow().isoformat(),
                    "url": url,
                    "platform": extracted_data.get("platform", "unknown"),
                    "status": "error",
                    "message": "No meaningful text content found"
                }
            
            # Truncate for analysis
            analysis_text = text_content[:512]
            
            # Step 2: Sentiment analysis
            logger.info("Analyzing sentiment")
            sentiment = self.sentiment_analyzer.analyze(analysis_text)
            
            # Step 3: Toxicity detection
            logger.info("Detecting toxicity")
            toxicity = self.toxicity_detector.detect(analysis_text)
            
            # Step 4: Hate speech detection
            logger.info("Detecting hate speech")
            hate_speech = self.hate_speech_detector.detect(analysis_text)
            
            # Step 5: Content classification
            logger.info("Classifying content categories")
            content_categories = self.content_classifier.classify(analysis_text)
            
            # Step 6: Intent detection
            logger.info("Detecting intent")
            intent = self.intent_detector.detect(analysis_text)
            
            # Step 7: NSFW detection
            logger.info("Detecting NSFW content")
            nsfw = self.nsfw_detector.detect(analysis_text)
            
            # Step 7.5: Misinformation detection
            logger.info("Detecting misinformation")
            misinformation = self.misinformation_detector.detect(analysis_text)
            
            # Step 7.6: Social media analysis
            logger.info("Analyzing social media patterns")
            platform = extracted_data.get("detected_platform", "unknown")
            social_analysis = self.social_media_analyzer.analyze_social_content(analysis_text, platform)
            
            # Step 8: Image analysis with OCR text analysis
            logger.info("Analyzing images")
            image_analysis = []
            try:
                html = extracted_data.get('html', '')
                base_url = extracted_data.get('base_url', url)
                logger.info(f"HTML length: {len(html) if html else 0}, Base URL: {base_url}")
                
                if html:
                    image_urls = self.image_extractor.extract_images(html, base_url)
                    
                    for img_url in image_urls[:10]:  # Limit to 10 images
                        logger.info(f"Analyzing image: {img_url}")
                        image = self.image_extractor.download_image(img_url)
                        
                        if image is None:
                            continue
                        
                        # Run all detectors
                        nsfw = self.nsfw_image_detector.detect(image)
                        violence = self.violence_detector.detect(image)
                        religious_hate = self.religious_hate_detector.detect(image, nsfw)
                        ocr = self.ocr_extractor.extract_text(image)
                        
                        # Analyze OCR text if present
                        ocr_analysis = None
                        if ocr.get("text") and len(ocr.get("text", "").strip()) > 10:
                            ocr_text = ocr.get("text")[:512]
                            ocr_analysis = {
                                "sentiment": self.sentiment_analyzer.analyze(ocr_text),
                                "toxicity": self.toxicity_detector.detect(ocr_text),
                                "hate_speech": self.hate_speech_detector.detect(ocr_text),
                                "content_categories": self.content_classifier.classify(ocr_text),
                                "risk_assessment": self.risk_scorer.calculate({
                                    "sentiment": self.sentiment_analyzer.analyze(ocr_text),
                                    "toxicity": self.toxicity_detector.detect(ocr_text),
                                    "hate_speech": self.hate_speech_detector.detect(ocr_text),
                                    "content_categories": self.content_classifier.classify(ocr_text),
                                    "intent": {"intent": "unknown", "confidence": 0},
                                    "nsfw": self.nsfw_detector.detect(ocr_text)
                                })
                            }
                        
                        # Calculate image risk score
                        risk_score = self._calculate_image_risk(nsfw, violence, religious_hate, ocr, ocr_analysis)
                        
                        image_analysis.append({
                            "image_url": img_url,
                            "nsfw": nsfw,
                            "violence": violence,
                            "religious_hate": religious_hate,
                            "ocr": ocr,
                            "ocr_analysis": ocr_analysis,
                            "image_risk_score": risk_score
                        })
                    
                    logger.info(f"Image analysis completed: {len(image_analysis)} images analyzed")
                else:
                    logger.warning("No HTML content available for image extraction")
            except Exception as e:
                logger.error(f"Image analysis failed: {str(e)}", exc_info=True)
            

            
            # Step 10: Calculate risk score
            analysis_data = {
                "sentiment": sentiment,
                "toxicity": toxicity,
                "hate_speech": hate_speech,
                "content_categories": content_categories,
                "intent": intent,
                "nsfw": nsfw,
                "misinformation": misinformation,
                "social_analysis": social_analysis,
                "image_analysis": image_analysis
            }
            
            risk_assessment = self.risk_scorer.calculate(analysis_data)
            
            # Calculate combined risk
            image_risk = self._calculate_combined_image_risk(image_analysis)
            text_risk = risk_assessment['score']
            combined_risk = int(text_risk * 0.6 + image_risk * 0.4)
            combined_level = self._get_risk_level(combined_risk)
            
            # Step 11: Generate report
            logger.info(f"Generating report with {len(image_analysis)} images, combined risk: {combined_risk}")
            
            report = {
                "analysis_id": str(uuid.uuid4()),
                "timestamp": datetime.utcnow().isoformat(),
                "url": url,
                "platform": extracted_data.get("detected_platform", "unknown"),
                "status": "completed",
                "metadata": {
                    "title": extracted_data.get("title", ""),
                    "author": extracted_data.get("author", ""),
                    "published_at": extracted_data.get("published_at", "")
                },
                "risk_assessment": risk_assessment,
                "image_analysis": image_analysis,
                "combined_risk": {
                    "score": combined_risk,
                    "level": combined_level,
                    "text_risk": text_risk,
                    "image_risk": image_risk
                },
                "content_analysis": {
                    "sentiment": sentiment,
                    "toxicity": toxicity,
                    "hate_speech": hate_speech,
                    "content_categories": content_categories,
                    "intent": intent,
                    "nsfw": nsfw,
                    "misinformation": misinformation,
                    "social_analysis": social_analysis
                },
                "summary": self._generate_summary(risk_assessment, sentiment, toxicity, hate_speech, content_categories, intent, nsfw, image_analysis),
                "text_preview": text_content[:200] + ("..." if len(text_content) > 200 else "")
            }
            
            logger.info(f"Analysis completed with risk level: {risk_assessment['level']}")
            return report
            
        except Exception as e:
            logger.error(f"Analysis failed: {str(e)}")
            return {
                "analysis_id": str(uuid.uuid4()),
                "timestamp": datetime.utcnow().isoformat(),
                "url": url,
                "status": "error",
                "message": str(e)
            }
    
    def _generate_summary(self, risk, sentiment, toxicity, hate_speech, content_categories, intent, nsfw, image_analysis):
        """Generate human-readable summary"""
        summary_parts = []
        
        # Image analysis summary
        if image_analysis:
            nsfw_images = sum(1 for img in image_analysis if img.get('nsfw', {}).get('is_nsfw'))
            explicit_images = sum(1 for img in image_analysis if img.get('nsfw', {}).get('is_explicit'))
            violent_images = sum(1 for img in image_analysis if img.get('violence', {}).get('is_violent'))
            hateful_visuals = sum(1 for img in image_analysis if img.get('violence', {}).get('is_hateful_visual'))
            spam_images = sum(1 for img in image_analysis if img.get('violence', {}).get('is_spam'))
            religious_hate_images = sum(1 for img in image_analysis if img.get('religious_hate', {}).get('is_religious_hate'))
            ocr_detected = sum(1 for img in image_analysis if img.get('ocr', {}).get('text'))
            
            if explicit_images:
                summary_parts.append(f"{explicit_images} explicit image(s) detected.")
            elif nsfw_images:
                summary_parts.append(f"{nsfw_images} NSFW image(s) detected.")
            if violent_images:
                summary_parts.append(f"{violent_images} violent image(s) detected.")
            if hateful_visuals:
                summary_parts.append(f"{hateful_visuals} hateful visual(s) detected.")
            if religious_hate_images:
                summary_parts.append(f"{religious_hate_images} religious hate image(s) detected.")
            if spam_images:
                summary_parts.append(f"{spam_images} spam image(s) detected.")
            if ocr_detected:
                summary_parts.append(f"Text extracted from {ocr_detected} image(s) and analyzed.")
        
        # NSFW check
        if nsfw.get('is_nsfw') and nsfw.get('confidence', 0) > 0.6:
            summary_parts.append("Explicit adult or sexual content detected in text.")
        
        intent_type = intent.get('intent', 'unknown')
        if intent_type == 'reporting' and not nsfw.get('is_nsfw'):
            summary_parts.append("The content appears to be news reporting or factual discussion.")
        elif intent_type == 'endorsing':
            summary_parts.append("The content may be endorsing or promoting harmful content.")
        
        if risk['level'] in ['CRITICAL', 'HIGH']:
            summary_parts.append(f"High risk detected (Score: {risk['score']}/100).")
        elif risk['level'] == 'MEDIUM':
            summary_parts.append(f"Moderate risk detected (Score: {risk['score']}/100).")
        else:
            summary_parts.append(f"Low risk content (Score: {risk['score']}/100).")
        
        if toxicity.get('is_toxic') and toxicity.get('confidence', 0) > 0.7:
            summary_parts.append("Contains toxic language.")
        
        if hate_speech.get('is_hate_speech') and hate_speech.get('confidence', 0) > 0.7:
            summary_parts.append("Hate speech detected.")
        
        detected = content_categories.get('detected_categories', [])
        if detected:
            cat_str = ", ".join(detected)
            summary_parts.append(f"Categories: {cat_str}.")
        
        if risk.get('reasons'):
            summary_parts.extend(risk['reasons'])
        
        return " ".join(summary_parts) if summary_parts else "Content analyzed successfully."
    
    def _calculate_combined_image_risk(self, image_analysis):
        if not image_analysis:
            return 0
        scores = [img.get('image_risk_score', 0) for img in image_analysis]
        return int(sum(scores) / len(scores)) if scores else 0
    
    def _calculate_image_risk(self, nsfw, violence, religious_hate, ocr, ocr_analysis):
        """Calculate comprehensive image risk score"""
        risk = 0
        
        # NSFW scoring (0-35 points)
        if nsfw.get("is_explicit"):
            risk += nsfw.get("confidence", 0) * 35
        elif nsfw.get("is_sexual"):
            risk += nsfw.get("confidence", 0) * 25
        elif nsfw.get("is_nsfw"):
            risk += nsfw.get("confidence", 0) * 20
        
        # Violence scoring (0-30 points)
        if violence.get("is_violent"):
            risk += violence.get("violence_score", 0) * 30
        
        # Hateful visual scoring (0-25 points)
        if violence.get("is_hateful_visual"):
            risk += violence.get("hate_score", 0) * 25
        
        # Religious hate scoring (0-30 points)
        if religious_hate.get("is_religious_hate"):
            risk += religious_hate.get("confidence", 0) * 30
        
        # Spam scoring (0-10 points)
        if violence.get("is_spam"):
            risk += violence.get("spam_score", 0) * 10
        
        # OCR text analysis (0-20 points)
        if ocr_analysis:
            ocr_risk = ocr_analysis.get("risk_assessment", {}).get("score", 0)
            risk += (ocr_risk / 100) * 20
        elif ocr.get("text") and len(ocr.get("text", "")) > 10:
            risk += 5  # Base bonus for text presence
        
        return min(int(risk), 100)
    
    def _get_risk_level(self, score):
        if score >= 70:
            return "CRITICAL"
        elif score >= 50:
            return "HIGH"
        elif score >= 30:
            return "MEDIUM"
        elif score >= 15:
            return "LOW"
        return "SAFE"

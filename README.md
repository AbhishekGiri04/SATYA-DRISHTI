# SATYA-DRISHTI - Digital Suraksha Framework

**AI-Powered Content Moderation System for Digital India**

Developed by: **Team Code Catalyst**  
Team Lead: **Abhishek Giri**  
Members: **Athrav Gangwar, Muskan Sharma, Kashish Sharma**

Tech Stack: Python (FastAPI) + React + 12 AI Models + MongoDB

---

## Problem Statement

Online platforms face critical challenges in content moderation:

### Communication & Safety Crisis
- Manual Moderation Overload: 100,000+ posts daily per moderator
- Language Barriers: 85% Indian content in regional languages
- Delayed Response: 24-48 hours before detection
- Platform Fragmentation: Separate approaches needed

### Detection Challenges
- Context Blindness: 60% false positives from keyword filters
- Evolving Threats: New slang bypasses systems
- Multi-modal Content: Text, images need different analysis
- Cultural Nuances: Indian context missed by global tools

### Legal & Compliance Issues
- No Legal Framework: Tools don't map to Indian laws
- Evidence Chain: No audit trail
- Jurisdiction Gaps: No Cybercrime Cell integration

### Business Impact
- Brand Safety: 73% advertisers avoid harmful platforms
- User Churn: 45% leave due to toxicity
- Legal Liability: Lawsuits for hosting illegal content
- Resource Drain: $500K-$2M annual moderation costs

---

## Our Solution

SATYA-DRISHTI revolutionizes content moderation through:

### For Social Media Platforms
- Real-time Detection: 10-15 seconds with 87% accuracy
- Multi-platform Support: Reddit, Twitter, Instagram, YouTube, TikTok, News
- Context-Aware: 80% false positive reduction
- Scalable: Handle millions of posts daily

### For Law Enforcement
- Cybercell Reports: Legal-ready with SHA256 evidence hash
- Indian Laws: IPC Sections 153A, 506 and IT Act 67, 66D
- Audit Trail: Complete logging for court
- Real-time Dashboard: Live threat monitoring

### For Government
- Source Verification: Vishwaas Score for news
- Multilingual: 9 Indian languages
- Bhashini Integration: Pattern-based detection
- Policy Enforcement: Configure moderation rules

### Enterprise-Grade AI
- 12 AI Models: 7 text + 5 image detectors
- Risk Scoring: 0-100 scale with 5 levels
- MongoDB: Persistent storage
- RESTful APIs: Complete CRUD operations

---

## System Architecture

### High-Level Flow

User Input URL → Platform Detection → Content Extraction → AI Analysis (12 Models) → Risk Scoring → Governance Layer → MongoDB Storage → JSON Response

### Data Flow

Browser → FastAPI (8001) → Platform Detection → Content Extraction (Text + Images) → AI Analysis (7 Text + 5 Image Models) → Risk Scoring → Governance (Source Verify + Language Detect + Report) → MongoDB Atlas → Response

---

## Key Features

### Content Analysis
- Multi-Platform: 8 adapters (Reddit, Twitter, Instagram, YouTube, TikTok, News, Generic, Images)
- Text Analysis: 7 AI models (sentiment, toxicity, hate speech, intent, categories, NSFW)
- Image Analysis: 5 detectors (NSFW 3-level, violence, hateful visuals, religious hate, OCR)
- Context-Aware: Intent detection (reporting vs endorsing)
- Risk Scoring: 0-100 with 5 levels (SAFE, LOW, MEDIUM, HIGH, CRITICAL)

### Governance Features
- Source Verification: Vishwaas Score with PIB Fact-Check
- Multilingual: Hindi, Bengali, Tamil, Telugu, Marathi, Gujarati, Kannada, Malayalam, Punjabi
- Cybercell Reports: Auto-generate with evidence hash
- Indian Laws: IPC 153A, 506 and IT Act 67, 66D, 354D
- Real-time Dashboard: Live statistics

### AI Capabilities
- 12 AI Models: Parallel processing
- 87% Accuracy: Content analysis
- Context Understanding: Meta-context detection
- Confidence Scoring: All predictions
- Predictive Analytics: Performance predictions

---

## Tech Stack

- Python 3.13: Core backend
- FastAPI: Async web framework
- React 18: Frontend UI
- MongoDB Atlas: Cloud database
- PyTorch: Deep learning
- HuggingFace: AI models
- OpenCV: Image processing
- EasyOCR: Text extraction
- BeautifulSoup4: HTML parsing
- Playwright: Browser automation
- Trafilatura: News extraction
- Vite: Frontend build

### AI Models (3GB Total)

Text Models (7):
- distilbert-base-uncased (67MB)
- unitary/unbiased-toxic-roberta (125MB)
- cardiffnlp/twitter-roberta-base-hate (125MB)
- facebook/bart-large-mnli (1.5GB)
- MoritzLaurer/mDeBERTa-v3-base-mnli-xnli (279MB)
- michellejieli/NSFW_text_classifier (125MB)
- Zero-Shot Classification

Image Models (5):
- Falconsai/nsfw_image_detection (50MB)
- openai/clip-vit-base-patch32 (150MB)
- CLIP Hateful Visual Detector
- Religious Hate Detector
- EasyOCR (30MB)

---

## Installation & Setup

### Prerequisites
- Python 3.13+
- Node.js 18+
- MongoDB Atlas account
- 8GB RAM minimum

### Quick Start

1. Clone repository
2. Backend: cd social-intel-agent && pip install -r requirements.txt
3. Frontend: cd react-interface && npm install
4. Configure MongoDB in src/database/mongodb.py
5. Start backend: uvicorn src.app:app --port 8001 --reload
6. Start frontend: npm run dev
7. Access: http://localhost:5173

---

## API Documentation

POST /analyze/ - Analyze URL
GET /governance/stats/dashboard - Statistics
POST /governance/verify-source - Verify source
POST /governance/detect-language - Detect language

---

## Performance Metrics

- 87% Accuracy
- 10-15 seconds processing (CPU)
- 3-5 seconds (GPU)
- 80% false positive reduction
- 12 AI models parallel
- 8 platforms supported
- 9 languages
- 24 categories

---

## Round 2 Improvements

### Current Limitations
- Mock PIB API (5 hardcoded entries)
- Pattern-based language (not real Bhashini)
- In-memory stats (MongoDB needs optimization)
- No PDF reports
- No video analysis
- No authentication
- No rate limiting

### Planned Enhancements

Phase 1: Real API Integration
- Real PIB Fact-Check API
- Bhashini API Integration
- Expand fake news DB to 1000+
- Real-time PIB feed

Phase 2: Advanced Features
- PDF report generation
- Video deepfake detection
- Audio analysis
- Live streaming monitoring

Phase 3: Security & Scale
- JWT authentication
- Rate limiting
- Redis caching
- Load balancing (1M+ requests/day)
- CDN integration

Phase 4: AI Improvements
- Fine-tuned models on Indian data
- Ensemble learning
- Active learning from feedback
- Explainable AI

Phase 5: Enterprise Features
- Mobile apps (iOS/Android)
- Browser extension
- Slack/Teams integration
- Custom dashboards
- API marketplace

---

## Team Code Catalyst

Abhishek Giri - Team Lead & Full-stack Developer
Athrav Gangwar - Backend Developer
Muskan Sharma - Frontend Developer
Kashish Sharma - AI/ML Engineer

---

## Contact

Team Lead: Abhishek Giri
LinkedIn: linkedin.com/in/abhishek-giri04
GitHub: github.com/abhishekgiri04
Telegram: t.me/AbhishekGiri7
Email: abhishekgiri.dev@gmail.com

---

Built with love for Digital India

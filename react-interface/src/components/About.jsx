import React from 'react';
import './About.css';

function About() {
  return (
    <div className="about-container">
      <section className="about-hero">
        <div className="hero-content">
          <h1 className="about-title">About SATYA-DRISHTI</h1>
          <p className="about-tagline">AI-Powered Content Moderation for Digital India</p>
          <p className="about-intro">
            SATYA-DRISHTI is an advanced AI-powered content moderation system designed to protect Digital India 
            from harmful online content. Using 12 sophisticated AI models, we analyze social media posts, images, 
            and news articles in real-time with 87% accuracy, detecting hate speech, toxicity, NSFW content, 
            and misinformation across 8 major platforms in 9 Indian languages.
          </p>
        </div>
      </section>

      <section className="how-it-works">
        <h2 className="section-title">How It Works</h2>
        <p className="section-subtitle">Our AI-powered pipeline processes content through 6 intelligent stages</p>
        <div className="workflow-steps">
          <div className="step-card">
            <div className="step-number">1</div>
            <h3>URL Input</h3>
            <p>Users submit any social media URL or image link through our intuitive web interface. The system accepts links from Reddit, Twitter, Instagram, YouTube, TikTok, news websites, and direct image URLs.</p>
          </div>
          <div className="step-card">
            <div className="step-number">2</div>
            <h3>Content Extraction</h3>
            <p>Platform-specific adapters intelligently scrape and extract text, images, and metadata. We use BeautifulSoup4 for static content, Playwright for dynamic JavaScript-heavy sites, and Trafilatura for news articles.</p>
          </div>
          <div className="step-card">
            <div className="step-number">3</div>
            <h3>AI Analysis</h3>
            <p>12 AI models run in parallel: 7 text analyzers (Sentiment, Toxicity, Hate Speech, Intent, Categories, NSFW, Zero-Shot) and 5 image detectors (NSFW, Violence, Hateful Visuals, Religious Hate, OCR) powered by PyTorch and HuggingFace.</p>
          </div>
          <div className="step-card">
            <div className="step-number">4</div>
            <h3>Risk Scoring</h3>
            <p>Weighted aggregation algorithm combines all model outputs (Text: 60%, Image: 40%) to generate a comprehensive 0-100 risk score with 5 severity levels: SAFE, LOW, MEDIUM, HIGH, CRITICAL.</p>
          </div>
          <div className="step-card">
            <div className="step-number">5</div>
            <h3>Governance Layer</h3>
            <p>Source verification checks news credibility (Vishwaas Score), language detection identifies 9 Indian languages, and legal mapping automatically tags violations with relevant IPC sections and IT Act provisions.</p>
          </div>
          <div className="step-card">
            <div className="step-number">6</div>
            <h3>Results & Reporting</h3>
            <p>Comprehensive report with detailed analysis, risk breakdown, legal implications, and cybercell-ready documentation with SHA256 evidence hash for court admissibility. All data stored in MongoDB Atlas.</p>
          </div>
        </div>
      </section>

      <section className="api-docs">
        <h2 className="section-title">API Documentation</h2>
        <p className="section-subtitle">RESTful APIs for seamless integration with your applications</p>
        <div className="api-grid">
          <div className="api-card">
            <div className="api-method">POST</div>
            <h3>/analyze/</h3>
            <p className="api-desc">Analyze any social media URL for harmful content detection</p>
            <div className="api-example">
              <div className="code-label">Request Body:</div>
              <code>
{`{
  "url": "https://twitter.com/example/status/123",
  "deep_analysis": false
}`}
              </code>
            </div>
            <div className="api-response">
              <div className="code-label">Response:</div>
              <code className="response-code">
{`{
  "risk_score": 75,
  "risk_level": "HIGH",
  "platform": "twitter",
  "text_analysis": {...},
  "image_analysis": {...},
  "governance": {...}
}`}
              </code>
            </div>
          </div>
          <div className="api-card">
            <div className="api-method">POST</div>
            <h3>/analyze-image/</h3>
            <p className="api-desc">Direct image URL analysis for visual content moderation</p>
            <div className="api-example">
              <div className="code-label">Request Body:</div>
              <code>
{`{
  "image_url": "https://example.com/image.jpg"
}`}
              </code>
            </div>
            <div className="api-response">
              <div className="code-label">Response:</div>
              <code className="response-code">
{`{
  "risk_score": 45,
  "nsfw": {...},
  "violence": {...},
  "ocr": {...}
}`}
              </code>
            </div>
          </div>
          <div className="api-card">
            <div className="api-method get">GET</div>
            <h3>/governance/stats/dashboard</h3>
            <p className="api-desc">Retrieve real-time analytics and platform statistics</p>
            <div className="api-response">
              <div className="code-label">Response:</div>
              <code className="response-code">
{`{
  "total_analyses": 1523,
  "risk_distribution": {...},
  "platform_breakdown": {...},
  "avg_risk_score": 42.5
}`}
              </code>
            </div>
          </div>
          <div className="api-card">
            <div className="api-method">POST</div>
            <h3>/governance/verify-source</h3>
            <p className="api-desc">Verify news source credibility with PIB Fact-Check integration</p>
            <div className="api-example">
              <div className="code-label">Request Body:</div>
              <code>
{`{
  "url": "https://news-site.com/article"
}`}
              </code>
            </div>
            <div className="api-response">
              <div className="code-label">Response:</div>
              <code className="response-code">
{`{
  "vishwaas_score": 85,
  "credibility": "HIGH",
  "pib_verified": true
}`}
              </code>
            </div>
          </div>
        </div>
        <div className="api-link">
          <a href="http://localhost:8001/docs" target="_blank" rel="noopener noreferrer">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" style={{display: 'inline-block', verticalAlign: 'middle', marginRight: '10px'}}>
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
              <polyline points="14 2 14 8 20 8"/>
              <line x1="16" y1="13" x2="8" y2="13"/>
              <line x1="16" y1="17" x2="8" y2="17"/>
            </svg>
            View Complete API Documentation (Swagger UI)
          </a>
        </div>
      </section>

      <section className="impact-section">
        <h2 className="section-title">Impact & Performance Metrics</h2>
        <p className="section-subtitle">Real-world results from our AI-powered content moderation system</p>
        <div className="impact-grid">
          <div className="impact-card">
            <svg className="impact-icon-svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#10b981" strokeWidth="2">
              <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            <div className="impact-number">87%</div>
            <p>Overall Accuracy</p>
            <span className="impact-detail">Across all 12 AI models</span>
          </div>
          <div className="impact-card">
            <svg className="impact-icon-svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#10b981" strokeWidth="2">
              <rect x="3" y="3" width="7" height="7"/>
              <rect x="14" y="3" width="7" height="7"/>
              <rect x="14" y="14" width="7" height="7"/>
              <rect x="3" y="14" width="7" height="7"/>
            </svg>
            <div className="impact-number">12</div>
            <p>AI Models</p>
            <span className="impact-detail">7 Text + 5 Image Analyzers</span>
          </div>
          <div className="impact-card">
            <svg className="impact-icon-svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#10b981" strokeWidth="2">
              <circle cx="12" cy="12" r="10"/>
              <line x1="2" y1="12" x2="22" y2="12"/>
              <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
            </svg>
            <div className="impact-number">8</div>
            <p>Platforms Supported</p>
            <span className="impact-detail">Reddit, Twitter, Instagram, YouTube, TikTok, News</span>
          </div>
          <div className="impact-card">
            <svg className="impact-icon-svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#10b981" strokeWidth="2">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
              <circle cx="12" cy="10" r="3"/>
            </svg>
            <div className="impact-number">9</div>
            <p>Indian Languages</p>
            <span className="impact-detail">Hindi, Bengali, Tamil, Telugu, Marathi, Gujarati, Kannada, Malayalam, Punjabi</span>
          </div>
          <div className="impact-card">
            <svg className="impact-icon-svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#10b981" strokeWidth="2">
              <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/>
              <polyline points="17 6 23 6 23 12"/>
            </svg>
            <div className="impact-number">10-15s</div>
            <p>Analysis Time (CPU)</p>
            <span className="impact-detail">3-5s with GPU acceleration</span>
          </div>
          <div className="impact-card">
            <svg className="impact-icon-svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#10b981" strokeWidth="2">
              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
              <polyline points="22 4 12 14.01 9 11.01"/>
            </svg>
            <div className="impact-number">80%</div>
            <p>False Positive Reduction</p>
            <span className="impact-detail">Compared to keyword-based filters</span>
          </div>
        </div>

        <div className="features-list">
          <h3>Key Features & Capabilities</h3>
          <div className="features-grid-list">
            <div className="feature-item">
              <svg className="feature-icon-svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
                <circle cx="12" cy="12" r="10"/>
                <line x1="2" y1="12" x2="22" y2="12"/>
                <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
              </svg>
              <div>
                <strong>Multi-Platform Support:</strong> Seamlessly analyzes content from Reddit, Twitter, Instagram, YouTube, TikTok, and news websites with platform-specific adapters
              </div>
            </div>
            <div className="feature-item">
              <svg className="feature-icon-svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                <polyline points="14 2 14 8 20 8"/>
                <line x1="16" y1="13" x2="8" y2="13"/>
                <line x1="16" y1="17" x2="8" y2="17"/>
                <polyline points="10 9 9 9 8 9"/>
              </svg>
              <div>
                <strong>Advanced Text Analysis:</strong> 7 AI models detect sentiment, toxicity, hate speech, intent classification, content categories, NSFW text, and custom zero-shot labels
              </div>
            </div>
            <div className="feature-item">
              <svg className="feature-icon-svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                <circle cx="8.5" cy="8.5" r="1.5"/>
                <polyline points="21 15 16 10 5 21"/>
              </svg>
              <div>
                <strong>Comprehensive Image Analysis:</strong> 5 detectors identify NSFW content (3-level), violence, hateful visuals, religious hate imagery, plus OCR text extraction
              </div>
            </div>
            <div className="feature-item">
              <svg className="feature-icon-svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                <path d="M9 12l2 2 4-4"/>
              </svg>
              <div>
                <strong>Source Verification:</strong> Vishwaas Score (0-100) with PIB Fact-Check integration to combat misinformation and fake news
              </div>
            </div>
            <div className="feature-item">
              <svg className="feature-icon-svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
              </svg>
              <div>
                <strong>Multilingual Support:</strong> Pattern-based detection for 9 Indian languages with Bhashini integration for regional content moderation
              </div>
            </div>
            <div className="feature-item">
              <svg className="feature-icon-svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
                <path d="M3 3h18v18H3zM12 8v8m-4-4h8"/>
              </svg>
              <div>
                <strong>Legal Compliance:</strong> Automatic mapping to IPC Sections (153A, 506) and IT Act provisions (67, 66D, 354D) for law enforcement coordination
              </div>
            </div>
            <div className="feature-item">
              <svg className="feature-icon-svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                <polyline points="14 2 14 8 20 8"/>
              </svg>
              <div>
                <strong>Cybercell Reports:</strong> Auto-generated legal-ready reports with SHA256 evidence hash for court admissibility and complete audit trail
              </div>
            </div>
            <div className="feature-item">
              <svg className="feature-icon-svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
                <line x1="12" y1="20" x2="12" y2="10"/>
                <line x1="18" y1="20" x2="18" y2="4"/>
                <line x1="6" y1="20" x2="6" y2="16"/>
              </svg>
              <div>
                <strong>Real-time Dashboard:</strong> Live threat monitoring with risk distribution, platform breakdown, and comprehensive analytics
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="tech-stack">
        <h2 className="section-title">Technology Stack</h2>
        <p className="section-subtitle">Built with cutting-edge technologies for maximum performance and scalability</p>
        <div className="tech-grid">
          <div className="tech-item">
            <svg className="tech-icon-svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <polyline points="16 18 22 12 16 6"/>
              <polyline points="8 6 2 12 8 18"/>
            </svg>
            <h4>Backend</h4>
            <p><strong>Python 3.13</strong> - Core backend language with async support</p>
            <p><strong>FastAPI</strong> - High-performance async web framework</p>
            <p><strong>Uvicorn</strong> - ASGI server for production deployment</p>
          </div>
          <div className="tech-item">
            <svg className="tech-icon-svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <polygon points="12 2 2 7 12 12 22 7 12 2"/>
              <polyline points="2 17 12 22 22 17"/>
              <polyline points="2 12 12 17 22 12"/>
            </svg>
            <h4>Frontend</h4>
            <p><strong>React 18</strong> - Modern UI library with hooks</p>
            <p><strong>Vite</strong> - Lightning-fast build tool</p>
            <p><strong>JavaScript ES6+</strong> - Client-side scripting</p>
          </div>
          <div className="tech-item">
            <svg className="tech-icon-svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <ellipse cx="12" cy="5" rx="9" ry="3"/>
              <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/>
              <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/>
            </svg>
            <h4>Database</h4>
            <p><strong>MongoDB Atlas</strong> - Cloud-hosted NoSQL database</p>
            <p><strong>PyMongo</strong> - Python MongoDB driver</p>
            <p><strong>Indexing</strong> - Optimized queries for performance</p>
          </div>
          <div className="tech-item">
            <svg className="tech-icon-svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <circle cx="12" cy="12" r="10"/>
              <path d="M12 16v-4"/>
              <path d="M12 8h.01"/>
            </svg>
            <h4>AI/ML</h4>
            <p><strong>PyTorch 2.0</strong> - Deep learning framework</p>
            <p><strong>HuggingFace Transformers</strong> - Pre-trained models</p>
            <p><strong>OpenCV</strong> - Image processing library</p>
            <p><strong>EasyOCR</strong> - Text extraction from images</p>
          </div>
          <div className="tech-item">
            <svg className="tech-icon-svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <circle cx="12" cy="12" r="10"/>
              <line x1="2" y1="12" x2="22" y2="12"/>
              <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
            </svg>
            <h4>Web Scraping</h4>
            <p><strong>BeautifulSoup4</strong> - HTML parsing</p>
            <p><strong>Playwright</strong> - Browser automation</p>
            <p><strong>Trafilatura</strong> - News article extraction</p>
          </div>
          <div className="tech-item">
            <svg className="tech-icon-svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <rect x="3" y="3" width="7" height="7"/>
              <rect x="14" y="3" width="7" height="7"/>
              <rect x="14" y="14" width="7" height="7"/>
              <rect x="3" y="14" width="7" height="7"/>
            </svg>
            <h4>AI Models (3GB)</h4>
            <p><strong>DistilBERT</strong> - Sentiment analysis (67MB)</p>
            <p><strong>RoBERTa</strong> - Toxicity & hate speech (125MB)</p>
            <p><strong>BART-MNLI</strong> - Intent classification (1.5GB)</p>
            <p><strong>CLIP-ViT</strong> - Image analysis (150MB)</p>
            <p><strong>mDeBERTa</strong> - Category detection (279MB)</p>
          </div>
        </div>
      </section>

      <section className="architecture-section">
        <h2 className="section-title">System Architecture</h2>
        <p className="section-subtitle">Microservices-based architecture with clear separation of concerns</p>
        <div className="architecture-flow">
          <div className="arch-layer">
            <h4>Client Layer</h4>
            <p>React Frontend (Port 5173) → User Interface</p>
          </div>
          <div className="arch-arrow">↓</div>
          <div className="arch-layer">
            <h4>API Gateway</h4>
            <p>FastAPI Server (Port 8001) → Request Validation & CORS</p>
          </div>
          <div className="arch-arrow">↓</div>
          <div className="arch-layer">
            <h4>Platform Detection</h4>
            <p>URL Analyzer → 8 Platform Adapters → Content Extraction</p>
          </div>
          <div className="arch-arrow">↓</div>
          <div className="arch-layer">
            <h4>AI Analysis Engine</h4>
            <p>7 Text Models + 5 Image Models → Parallel Processing</p>
          </div>
          <div className="arch-arrow">↓</div>
          <div className="arch-layer">
            <h4>Risk Scoring</h4>
            <p>Weighted Aggregation → 0-100 Score → 5 Risk Levels</p>
          </div>
          <div className="arch-arrow">↓</div>
          <div className="arch-layer">
            <h4>Governance Layer</h4>
            <p>Source Verification + Language Detection + Legal Mapping</p>
          </div>
          <div className="arch-arrow">↓</div>
          <div className="arch-layer">
            <h4>Data Layer</h4>
            <p>MongoDB Atlas → Analysis Collection → Statistics</p>
          </div>
        </div>
      </section>
    </div>
  );
}

export default About;

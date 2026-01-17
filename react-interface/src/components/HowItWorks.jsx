import React from 'react';
import './HowItWorks.css';

function HowItWorks() {
  return (
    <div className="how-it-works">
      <div className="hero-section">
        <div className="hero-badge">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
            <path d="M9 12l2 2 4-4"/>
          </svg>
          <span>AI-Powered Intelligence</span>
        </div>
        <h1>How SATYA-DRISHTI Works</h1>
        <p>Discover how our intelligent AI-powered system analyzes digital content in real-time, combining cutting-edge machine learning with India's legal framework to protect citizens from online threats</p>
        <div className="hero-stats-cards">
          <div className="stat-card blue-card">
            <div className="stat-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                <path d="M2 17l10 5 10-5"/>
                <path d="M2 12l10 5 10-5"/>
              </svg>
            </div>
            <div className="stat-content">
              <span className="stat-number">12</span>
              <span className="stat-label">AI Models</span>
              <p className="stat-desc">Specialized deep learning models</p>
            </div>
          </div>
          <div className="stat-card green-card">
            <div className="stat-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                <polyline points="22,4 12,14.01 9,11.01"/>
              </svg>
            </div>
            <div className="stat-content">
              <span className="stat-number">87%</span>
              <span className="stat-label">Accuracy</span>
              <p className="stat-desc">Overall detection precision</p>
            </div>
          </div>
          <div className="stat-card orange-card">
            <div className="stat-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <circle cx="12" cy="12" r="10"/>
                <line x1="2" y1="12" x2="22" y2="12"/>
                <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
              </svg>
            </div>
            <div className="stat-content">
              <span className="stat-number">9</span>
              <span className="stat-label">Languages</span>
              <p className="stat-desc">Indian language support</p>
            </div>
          </div>
        </div>
      </div>

      <div className="models-overview">
        <h2>AI Model Architecture</h2>
        <div className="architecture-visual">
          <div className="model-category text-category">
            <div className="category-header">
              <div className="category-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                  <polyline points="14,2 14,8 20,8"/>
                  <line x1="16" y1="13" x2="8" y2="13"/>
                  <line x1="16" y1="17" x2="8" y2="17"/>
                </svg>
              </div>
              <h3>Text Analysis Engine</h3>
              <span className="model-count">7 Models</span>
            </div>
            <div className="models-list">
              <div className="model-card hate-speech">
                <div className="model-header">
                  <span className="model-number">01</span>
                  <h4>Hate Speech Detection</h4>
                  <div className="accuracy-badge">94% Accurate</div>
                </div>
                <p>Advanced NLP algorithms identify discriminatory language targeting individuals or groups based on race, religion, gender, or ethnicity</p>
                <div className="model-features">
                  <span>Multi-lingual Support</span>
                  <span>Context Awareness</span>
                  <span>Real-time Processing</span>
                </div>
              </div>
              
              <div className="model-card toxicity">
                <div className="model-header">
                  <span className="model-number">02</span>
                  <h4>Toxicity Classification</h4>
                  <div className="accuracy-badge">91% Accurate</div>
                </div>
                <p>Detects harmful, abusive, and offensive content patterns using transformer-based deep learning models</p>
                <div className="model-features">
                  <span>Severity Scoring</span>
                  <span>Pattern Recognition</span>
                  <span>Behavioral Analysis</span>
                </div>
              </div>

              <div className="model-card sentiment">
                <div className="model-header">
                  <span className="model-number">03</span>
                  <h4>Sentiment Analysis</h4>
                  <div className="accuracy-badge">95% Accurate</div>
                </div>
                <p>Analyzes emotional tone and contextual sentiment with industry-leading accuracy using advanced NLP</p>
                <div className="model-features">
                  <span>Emotion Detection</span>
                  <span>Tone Analysis</span>
                  <span>Cultural Context</span>
                </div>
              </div>

              <div className="model-card intent">
                <div className="model-header">
                  <span className="model-number">04</span>
                  <h4>Intent Classification</h4>
                  <div className="accuracy-badge">89% Accurate</div>
                </div>
                <p>Determines malicious intent and threat level assessment through behavioral pattern analysis</p>
                <div className="model-features">
                  <span>Threat Assessment</span>
                  <span>Intent Scoring</span>
                  <span>Risk Prediction</span>
                </div>
              </div>

              <div className="model-card language">
                <div className="model-header">
                  <span className="model-number">05</span>
                  <h4>Language Detection</h4>
                  <div className="accuracy-badge">98% Accurate</div>
                </div>
                <p>Identifies content language across 9 Indian languages including Hindi, Bengali, Tamil, Telugu, and more</p>
                <div className="model-features">
                  <span>9 Indian Languages</span>
                  <span>Script Recognition</span>
                  <span>Dialect Support</span>
                </div>
              </div>

              <div className="model-card misinformation">
                <div className="model-header">
                  <span className="model-number">06</span>
                  <h4>Misinformation Detection</h4>
                  <div className="accuracy-badge">85% Accurate</div>
                </div>
                <p>Cross-references content with verified fact-checking databases and identifies false information</p>
                <div className="model-features">
                  <span>Fact Verification</span>
                  <span>Source Credibility</span>
                  <span>PIB Integration</span>
                </div>
              </div>

              <div className="model-card context">
                <div className="model-header">
                  <span className="model-number">07</span>
                  <h4>Context Understanding</h4>
                  <div className="accuracy-badge">88% Accurate</div>
                </div>
                <p>Analyzes contextual meaning and cultural nuances to reduce false positives and improve accuracy</p>
                <div className="model-features">
                  <span>Cultural Awareness</span>
                  <span>Contextual Analysis</span>
                  <span>Nuance Detection</span>
                </div>
              </div>
            </div>
          </div>

          <div className="model-category image-category">
            <div className="category-header">
              <div className="category-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                  <circle cx="8.5" cy="8.5" r="1.5"/>
                  <polyline points="21,15 16,10 5,21"/>
                </svg>
              </div>
              <h3>Visual Analysis Engine</h3>
              <span className="model-count">5 Models</span>
            </div>
            <div className="models-list">
              <div className="model-card nsfw">
                <div className="model-header">
                  <span className="model-number">08</span>
                  <h4>NSFW Content Detection</h4>
                  <div className="accuracy-badge">93% Accurate</div>
                </div>
                <p>Identifies inappropriate and explicit visual content using advanced computer vision algorithms</p>
                <div className="model-features">
                  <span>Adult Content</span>
                  <span>Explicit Material</span>
                  <span>Age Verification</span>
                </div>
              </div>

              <div className="model-card violence">
                <div className="model-header">
                  <span className="model-number">09</span>
                  <h4>Violence Detection</h4>
                  <div className="accuracy-badge">90% Accurate</div>
                </div>
                <p>Recognizes violent imagery and graphic content through deep learning visual analysis</p>
                <div className="model-features">
                  <span>Graphic Violence</span>
                  <span>Weapon Detection</span>
                  <span>Injury Recognition</span>
                </div>
              </div>

              <div className="model-card symbols">
                <div className="model-header">
                  <span className="model-number">10</span>
                  <h4>Hateful Symbols Recognition</h4>
                  <div className="accuracy-badge">87% Accurate</div>
                </div>
                <p>Detects hate symbols, extremist imagery, and offensive visuals using pattern recognition</p>
                <div className="model-features">
                  <span>Symbol Database</span>
                  <span>Extremist Content</span>
                  <span>Cultural Symbols</span>
                </div>
              </div>

              <div className="model-card ocr">
                <div className="model-header">
                  <span className="model-number">11</span>
                  <h4>OCR Text Extraction</h4>
                  <div className="accuracy-badge">96% Accurate</div>
                </div>
                <p>Extracts and analyzes text embedded within images for comprehensive content review</p>
                <div className="model-features">
                  <span>Multi-language OCR</span>
                  <span>Text Recognition</span>
                  <span>Font Analysis</span>
                </div>
              </div>

              <div className="model-card meme">
                <div className="model-header">
                  <span className="model-number">12</span>
                  <h4>Meme Classification</h4>
                  <div className="accuracy-badge">84% Accurate</div>
                </div>
                <p>Analyzes meme content for harmful or misleading information using visual and textual analysis</p>
                <div className="model-features">
                  <span>Meme Templates</span>
                  <span>Viral Content</span>
                  <span>Humor Analysis</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="workflow-section">
        <h2>Analysis Workflow Pipeline</h2>
        <div className="workflow-container">
          <div className="workflow-step step-1">
            <div className="step-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>
                <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>
              </svg>
            </div>
            <h3>Content Ingestion</h3>
            <p>Secure URL validation and intelligent content extraction from 8+ social media platforms</p>
            <div className="step-details">
              <span>Platform Detection</span>
              <span>Content Parsing</span>
              <span>Media Extraction</span>
            </div>
          </div>
          
          <div className="workflow-arrow">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <line x1="5" y1="12" x2="19" y2="12"/>
              <polyline points="12,5 19,12 12,19"/>
            </svg>
          </div>

          <div className="workflow-step step-2">
            <div className="step-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                <path d="M2 17l10 5 10-5"/>
                <path d="M2 12l10 5 10-5"/>
              </svg>
            </div>
            <h3>Parallel AI Processing</h3>
            <p>All 12 specialized models analyze content simultaneously for comprehensive threat assessment</p>
            <div className="step-details">
              <span>Multi-threading</span>
              <span>Load Balancing</span>
              <span>Real-time Analysis</span>
            </div>
          </div>

          <div className="workflow-arrow">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <line x1="5" y1="12" x2="19" y2="12"/>
              <polyline points="12,5 19,12 12,19"/>
            </svg>
          </div>

          <div className="workflow-step step-3">
            <div className="step-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <circle cx="12" cy="12" r="3"/>
                <path d="M12 1v6m0 6v6m11-7h-6m-6 0H1"/>
              </svg>
            </div>
            <h3>Risk Calculation</h3>
            <p>Advanced weighted algorithm combines all model results into comprehensive 0-100 risk score</p>
            <div className="step-details">
              <span>Weight Assignment</span>
              <span>Score Aggregation</span>
              <span>Confidence Metrics</span>
            </div>
          </div>

          <div className="workflow-arrow">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <line x1="5" y1="12" x2="19" y2="12"/>
              <polyline points="12,5 19,12 12,19"/>
            </svg>
          </div>

          <div className="workflow-step step-4">
            <div className="step-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                <polyline points="14,2 14,8 20,8"/>
                <line x1="16" y1="13" x2="8" y2="13"/>
                <line x1="16" y1="17" x2="8" y2="17"/>
              </svg>
            </div>
            <h3>Report Generation</h3>
            <p>Detailed analysis report with actionable recommendations and legal compliance documentation</p>
            <div className="step-details">
              <span>Evidence Collection</span>
              <span>Legal Mapping</span>
              <span>Action Items</span>
            </div>
          </div>
        </div>
      </div>

      <div className="technical-specs">
        <h2>Technical Performance Metrics</h2>
        <div className="specs-container">
          <div className="spec-card speed">
            <div className="spec-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <circle cx="12" cy="12" r="10"/>
                <polyline points="12,6 12,12 16,14"/>
              </svg>
            </div>
            <h4>Processing Speed</h4>
            <div className="spec-value">10-15s</div>
            <p>Average analysis time with CPU processing. GPU acceleration reduces to 3-5 seconds</p>
            <div className="spec-breakdown">
              <div className="breakdown-item">
                <span>Text Analysis: 3-5s</span>
                <div className="progress-bar"><div className="progress" style={{width: '30%'}}></div></div>
              </div>
              <div className="breakdown-item">
                <span>Image Analysis: 5-8s</span>
                <div className="progress-bar"><div className="progress" style={{width: '50%'}}></div></div>
              </div>
              <div className="breakdown-item">
                <span>Risk Calculation: 1-2s</span>
                <div className="progress-bar"><div className="progress" style={{width: '15%'}}></div></div>
              </div>
            </div>
          </div>

          <div className="spec-card accuracy">
            <div className="spec-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                <polyline points="22,4 12,14.01 9,11.01"/>
              </svg>
            </div>
            <h4>Detection Accuracy</h4>
            <div className="spec-value">87%</div>
            <p>Overall detection accuracy across all 12 models with continuous improvement through machine learning</p>
            <div className="accuracy-chart">
              <div className="chart-item">
                <span>Text Models</span>
                <div className="accuracy-bar">
                  <div className="accuracy-fill" style={{width: '91%'}}></div>
                  <span className="accuracy-percent">91%</span>
                </div>
              </div>
              <div className="chart-item">
                <span>Image Models</span>
                <div className="accuracy-bar">
                  <div className="accuracy-fill" style={{width: '90%'}}></div>
                  <span className="accuracy-percent">90%</span>
                </div>
              </div>
            </div>
          </div>

          <div className="spec-card languages">
            <div className="spec-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <circle cx="12" cy="12" r="10"/>
                <line x1="2" y1="12" x2="22" y2="12"/>
                <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
              </svg>
            </div>
            <h4>Language Coverage</h4>
            <div className="spec-value">9</div>
            <p>Comprehensive support for major Indian languages with cultural context understanding</p>
            <div className="language-grid">
              <span>Hindi</span>
              <span>English</span>
              <span>Bengali</span>
              <span>Tamil</span>
              <span>Telugu</span>
              <span>Marathi</span>
              <span>Gujarati</span>
              <span>Kannada</span>
              <span>Malayalam</span>
            </div>
          </div>

          <div className="spec-card platforms">
            <div className="spec-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
                <line x1="8" y1="21" x2="16" y2="21"/>
                <line x1="12" y1="17" x2="12" y2="21"/>
              </svg>
            </div>
            <h4>Platform Integration</h4>
            <div className="spec-value">8+</div>
            <p>Universal compatibility across major social media platforms and news aggregation sites</p>
            <div className="platform-list">
              <div className="platform-item">Twitter/X</div>
              <div className="platform-item">Reddit</div>
              <div className="platform-item">Instagram</div>
              <div className="platform-item">YouTube</div>
              <div className="platform-item">Facebook</div>
              <div className="platform-item">TikTok</div>
              <div className="platform-item">News Sites</div>
              <div className="platform-item">Blogs</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default HowItWorks;
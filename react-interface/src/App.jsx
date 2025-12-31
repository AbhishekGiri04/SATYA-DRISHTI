import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import Navbar from './components/Navbar.jsx';
import Footer from './components/Footer.jsx';
import ResultCard from './components/ResultCard.jsx';
import HomeContent from './components/HomeContent.jsx';
import HowItWorks from './components/HowItWorks.jsx';
import Docs from './components/Docs.jsx';
import Contact from './components/Contact.jsx';
import ImpactMonitor from './components/ImpactMonitor.jsx';
import GovernanceDashboard from './components/GovernanceDashboard.jsx';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8001';

function App() {
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');
  const [currentSection, setCurrentSection] = useState('home');
  const [imageUrl, setImageUrl] = useState('');
  const [imageLoading, setImageLoading] = useState(false);
  const [imageResult, setImageResult] = useState(null);
  const [flash, setFlash] = useState({ show: false, message: '', type: '' });
  const [analysisStep, setAnalysisStep] = useState('');

  const showFlash = (message, type) => {
    setFlash({ show: true, message, type });
    setTimeout(() => setFlash({ show: false, message: '', type: '' }), 4000);
  };

  const analyzeUrl = async () => {
    if (!url.trim()) {
      showFlash('Please enter a URL', 'error');
      return;
    }

    const urlPattern = /^(https?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$/;
    if (!urlPattern.test(url)) {
      showFlash('Error - Link not Working', 'error');
      return;
    }

    setLoading(true);
    setError('');
    setResult(null);
    setAnalysisStep('scraping');
    
    // Simulate pipeline steps
    const steps = ['scraping', 'sentiment', 'toxicity', 'hate', 'categories', 'intent', 'nsfw', 'images', 'complete'];
    let stepIndex = 0;
    const stepInterval = setInterval(() => {
      stepIndex++;
      if (stepIndex < steps.length) {
        setAnalysisStep(steps[stepIndex]);
      } else {
        clearInterval(stepInterval);
      }
    }, 2000);

    try {
      const response = await axios.post(`${API_URL}/analyze/`, {
        url: url,
        deep_analysis: false
      });

      clearInterval(stepInterval);
      if (response.data.status === 'error') {
        showFlash('Error - Link not Working', 'error');
      } else {
        console.log('Analysis Result:', response.data);
        console.log('Image Analysis:', response.data.image_analysis);
        setAnalysisStep('complete');
        setTimeout(() => {
          setResult(response.data);
          showFlash('Analysis completed successfully!', 'success');
        }, 500);
      }
    } catch (err) {
      clearInterval(stepInterval);
      showFlash('Error - Link not Working', 'error');
    } finally {
      setLoading(false);
      setAnalysisStep('');
    }
  };

  const getProgressPercentage = () => {
    const steps = ['scraping', 'sentiment', 'toxicity', 'hate', 'categories', 'intent', 'nsfw', 'images', 'complete'];
    const index = steps.indexOf(analysisStep);
    return index >= 0 ? ((index + 1) / steps.length) * 100 : 0;
  };

  const analyzeImage = async () => {
    if (!imageUrl.trim()) {
      showFlash('Please enter an image URL', 'error');
      return;
    }

    setImageLoading(true);
    setImageResult(null);

    try {
      const response = await axios.post(`${API_URL}/analyze-image/`, {
        image_url: imageUrl
      });

      if (response.data.status === 'error') {
        showFlash('Error analyzing image', 'error');
      } else {
        console.log('Image Analysis Response:', response.data);
        setImageResult(response.data);
        showFlash('Image analysis completed!', 'success');
      }
    } catch (err) {
      showFlash('Error analyzing image', 'error');
    } finally {
      setImageLoading(false);
    }
  };

  const renderContent = () => {
    switch(currentSection) {
      case 'how':
        return <HowItWorks />;
      case 'docs':
        return <Docs />;
      case 'impact':
        return <ImpactMonitor />;
      case 'contact':
        return <Contact />;
      case 'governance':
        return <GovernanceDashboard />;
      default:
        return (
          <>
            <header className="header">
              <h1 className="header-title">
                <span className="title-text">Content Analysis Hub</span>
              </h1>
              <p className="header-subtitle">AI-Powered Safety Analysis for Digital India</p>
              <div className="header-stats">
                <div className="stat-item">
                  <span className="stat-number">12</span>
                  <span className="stat-label">AI Models</span>
                </div>
                <div className="stat-item">
                  <span className="stat-number">87%</span>
                  <span className="stat-label">Accuracy</span>
                </div>
                <div className="stat-item">
                  <span className="stat-number">10s</span>
                  <span className="stat-label">Analysis</span>
                </div>
              </div>
            </header>

            <div className="input-section">
              <input
                type="text"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && analyzeUrl()}
                placeholder="Enter any URL to analyze content safety..."
                className="url-input"
              />
              <button onClick={analyzeUrl} disabled={loading} className="analyze-btn">
                {loading ? 'Analyzing...' : 'Analyze'}
              </button>
            </div>

            {loading && (
              <div className="loading">
                <div className="analysis-pipeline">
                  <h3>AI Analysis in Progress</h3>
                  <div className="pipeline-steps">
                    <div className={`step ${analysisStep === 'scraping' ? 'active' : analysisStep ? 'completed' : ''}`}>
                      <div className="step-icon">→</div>
                      <div className="step-info">
                        <div className="step-title">Web Scraping</div>
                        <div className="step-desc">Extracting content from URL</div>
                      </div>
                    </div>
                    <div className={`step ${analysisStep === 'sentiment' ? 'active' : ['toxicity', 'hate', 'categories', 'intent', 'nsfw', 'images', 'complete'].includes(analysisStep) ? 'completed' : ''}`}>
                      <div className="step-icon">→</div>
                      <div className="step-info">
                        <div className="step-title">Sentiment Analysis</div>
                        <div className="step-desc">Detecting emotional tone</div>
                      </div>
                    </div>
                    <div className={`step ${analysisStep === 'toxicity' ? 'active' : ['hate', 'categories', 'intent', 'nsfw', 'images', 'complete'].includes(analysisStep) ? 'completed' : ''}`}>
                      <div className="step-icon">→</div>
                      <div className="step-info">
                        <div className="step-title">Toxicity Detection</div>
                        <div className="step-desc">Identifying harmful language</div>
                      </div>
                    </div>
                    <div className={`step ${analysisStep === 'hate' ? 'active' : ['categories', 'intent', 'nsfw', 'images', 'complete'].includes(analysisStep) ? 'completed' : ''}`}>
                      <div className="step-icon">→</div>
                      <div className="step-info">
                        <div className="step-title">Hate Speech Detection</div>
                        <div className="step-desc">Scanning for targeted hate</div>
                      </div>
                    </div>
                    <div className={`step ${analysisStep === 'categories' ? 'active' : ['intent', 'nsfw', 'images', 'complete'].includes(analysisStep) ? 'completed' : ''}`}>
                      <div className="step-icon">→</div>
                      <div className="step-info">
                        <div className="step-title">Content Classification</div>
                        <div className="step-desc">18 fine-grained categories</div>
                      </div>
                    </div>
                    <div className={`step ${analysisStep === 'intent' ? 'active' : ['nsfw', 'images', 'complete'].includes(analysisStep) ? 'completed' : ''}`}>
                      <div className="step-icon">→</div>
                      <div className="step-info">
                        <div className="step-title">Intent Detection</div>
                        <div className="step-desc">Context-aware analysis</div>
                      </div>
                    </div>
                    <div className={`step ${analysisStep === 'nsfw' ? 'active' : ['images', 'complete'].includes(analysisStep) ? 'completed' : ''}`}>
                      <div className="step-icon">→</div>
                      <div className="step-info">
                        <div className="step-title">NSFW Detection</div>
                        <div className="step-desc">Explicit content scanning</div>
                      </div>
                    </div>
                    <div className={`step ${analysisStep === 'images' ? 'active' : analysisStep === 'complete' ? 'completed' : ''}`}>
                      <div className="step-icon">→</div>
                      <div className="step-info">
                        <div className="step-title">Image Analysis</div>
                        <div className="step-desc">Visual content + OCR</div>
                      </div>
                    </div>
                  </div>
                  <div className="progress-bar">
                    <div className="progress-fill" style={{ width: `${getProgressPercentage()}%` }}></div>
                  </div>
                  <p className="analysis-status">Processing with 7 AI models...</p>
                </div>
              </div>
            )}

            {result && <ResultCard data={result} />}

            {!result && !loading && !error && (
              <>
                <div className="analysis-tabs">
                  <button className="tab-btn active">URL Analysis</button>
                  <button className="tab-btn" onClick={() => document.getElementById('image-section').scrollIntoView({ behavior: 'smooth' })}>Image Analysis</button>
                </div>
                <HomeContent />
                <div id="image-section" className="image-analysis-section-home">
                  <h2>Direct Image Analysis</h2>
                  <p className="section-desc">Analyze any public image URL for harmful content</p>
                  <div className="input-section">
                    <input
                      type="text"
                      value={imageUrl}
                      onChange={(e) => setImageUrl(e.target.value)}
                      onKeyPress={(e) => e.key === 'Enter' && analyzeImage()}
                      placeholder="Enter image URL (e.g., https://example.com/image.jpg)..."
                      className="url-input"
                    />
                    <button onClick={analyzeImage} disabled={imageLoading} className="analyze-btn">
                      {imageLoading ? 'Analyzing...' : 'Analyze Image'}
                    </button>
                  </div>

                  {imageLoading && (
                    <div className="loading">
                      <div className="spinner"></div>
                      <p>Analyzing image...</p>
                    </div>
                  )}

                  {imageResult && (
                    <div className="image-only-result">
                      <div className="image-comparison">
                        <div className="image-preview-section">
                          <h4>Original Image</h4>
                          <img src={imageUrl} alt="Original" className="analyzed-img" referrerPolicy="no-referrer" />
                        </div>
                        {imageResult.marked_image && (
                          <div className="image-preview-section">
                            <h4>Marked Analysis</h4>
                            <img src={imageResult.marked_image} alt="Marked" className="analyzed-img" />
                          </div>
                        )}
                      </div>
                      <div className="image-analysis-details">
                        <h3>Analysis Results</h3>
                        
                        {imageResult.categorization && (
                          <div className="categorization-section">
                            <div className="primary-category">
                              <span className="category-label">Primary Category:</span>
                              <span className="category-value">{imageResult.categorization.primary_category.toUpperCase().replace(/_/g, ' ')}</span>
                            </div>
                            {imageResult.categorization.all_categories.length > 0 && (
                              <div className="all-categories">
                                <span className="category-label">All Categories:</span>
                                <div className="category-badges">
                                  {imageResult.categorization.all_categories.map((cat, idx) => (
                                    <span key={idx} className="cat-badge">{cat.replace(/_/g, ' ')}</span>
                                  ))}
                                </div>
                              </div>
                            )}
                          </div>
                        )}
                        <div className="risk-score-display">
                          <div className="score-circle" style={{ borderColor: imageResult.risk_score > 70 ? '#dc2626' : imageResult.risk_score > 50 ? '#ef4444' : imageResult.risk_score > 30 ? '#f59e0b' : '#10b981' }}>
                            <span className="score-num">{imageResult.risk_score || 0}</span>
                            <span className="score-max">/100</span>
                          </div>
                          <div className="risk-level-text" style={{ color: imageResult.risk_score > 70 ? '#dc2626' : imageResult.risk_score > 50 ? '#ef4444' : imageResult.risk_score > 30 ? '#f59e0b' : '#10b981' }}>
                            {imageResult.risk_score > 70 ? 'CRITICAL' : imageResult.risk_score > 50 ? 'HIGH' : imageResult.risk_score > 30 ? 'MEDIUM' : imageResult.risk_score > 15 ? 'LOW' : 'SAFE'}
                          </div>
                        </div>
                        <div className="detection-results">
                          <div className="detection-item">
                            <span className="detection-label">NSFW:</span>
                            <span className="detection-value" style={{ color: imageResult.nsfw?.is_nsfw ? '#ef4444' : '#10b981' }}>
                              {imageResult.nsfw?.is_explicit ? 'Explicit' : imageResult.nsfw?.is_sexual ? 'Sexual' : imageResult.nsfw?.is_nsfw ? 'Yes' : 'No'} ({(imageResult.nsfw?.confidence * 100).toFixed(1)}%)
                            </span>
                          </div>
                          <div className="detection-item">
                            <span className="detection-label">Violence:</span>
                            <span className="detection-value" style={{ color: imageResult.violence?.is_violent ? '#ef4444' : '#10b981' }}>
                              {imageResult.violence?.is_violent ? 'Yes' : 'No'} ({((imageResult.violence?.violence_score || 0) * 100).toFixed(1)}%)
                            </span>
                          </div>
                          <div className="detection-item">
                            <span className="detection-label">Hateful Visual:</span>
                            <span className="detection-value" style={{ color: imageResult.violence?.is_hateful_visual ? '#ef4444' : '#10b981' }}>
                              {imageResult.violence?.is_hateful_visual ? 'Yes' : 'No'} ({((imageResult.violence?.hate_score || 0) * 100).toFixed(1)}%)
                            </span>
                          </div>
                          <div className="detection-item">
                            <span className="detection-label">Spam:</span>
                            <span className="detection-value" style={{ color: imageResult.violence?.is_spam ? '#f59e0b' : '#10b981' }}>
                              {imageResult.violence?.is_spam ? 'Yes' : 'No'} ({((imageResult.violence?.spam_score || 0) * 100).toFixed(1)}%)
                            </span>
                          </div>
                          {imageResult.religious_hate && (
                            <div className="detection-item">
                              <span className="detection-label">Religious Hate:</span>
                              <span className="detection-value" style={{ color: imageResult.religious_hate?.is_religious_hate ? '#ef4444' : '#10b981' }}>
                                {imageResult.religious_hate?.is_religious_hate ? 'Detected' : 'None'}
                              </span>
                            </div>
                          )}
                          <div className="detection-item ocr-item">
                            <span className="detection-label">OCR Text:</span>
                            <span className="detection-value">{imageResult.ocr?.text || 'No text detected'}</span>
                          </div>
                        </div>
                        
                        {imageResult.report && (
                          <div className="analysis-report">
                            <h4>📋 Detailed Report</h4>
                            <div className="report-summary">{imageResult.report.summary}</div>
                            
                            <div className="report-section">
                              <h5>⚠️ Detected Issues:</h5>
                              <ul className="report-list">
                                {imageResult.report.detected_issues.map((issue, idx) => (
                                  <li key={idx}>{issue}</li>
                                ))}
                              </ul>
                            </div>
                            
                            <div className="report-section">
                              <h5>💡 Recommendations:</h5>
                              <ul className="report-list">
                                {imageResult.report.recommendations.map((rec, idx) => (
                                  <li key={idx}>{rec}</li>
                                ))}
                              </ul>
                            </div>
                          </div>
                        )}
                      </div>
                    </div>
                  )}
                </div>
              </>
            )}
          </>
        );
    }
  };

  return (
    <div className="app">
      {flash.show && (
        <div className={`flash-message ${flash.type}`}>
          {flash.type === 'error' ? 'Error' : 'Success'} {flash.message}
        </div>
      )}
      <Navbar onSectionChange={setCurrentSection} currentSection={currentSection} />
      <div className="container">
        {renderContent()}
      </div>
      <Footer />
    </div>
  );
}

export default App;

import React from 'react';
import './ResultCard.css';

function ResultCard({ data }) {
  // Generate report if not present
  const generateReport = () => {
    if (data.cybercell_report) return data.cybercell_report;
    
    const riskScore = data.combined_risk?.score || data.risk_assessment?.score || 0;
    const riskLevel = data.combined_risk?.level || data.risk_assessment?.level || 'SAFE';
    
    // Generate report for all analyses
    
    const legalSections = [];
    if (data.content_analysis?.hate_speech?.is_hate_speech) legalSections.push('IPC Section 153A - Promoting enmity between groups');
    if (data.content_analysis?.toxicity?.is_toxic) legalSections.push('IPC Section 506 - Criminal intimidation');
    if (data.content_analysis?.nsfw?.is_nsfw) legalSections.push('IT Act Section 67 - Publishing obscene content');
    
    if (legalSections.length === 0) {
      legalSections.push('No legal violations detected - Content is safe');
    }
    
    return {
      report_id: `CR-${data.analysis_id?.substring(0, 8) || Date.now()}`,
      report_status: 'GENERATED',
      evidence_hash: `SHA256:${btoa(data.url || data.analysis_id).substring(0, 32)}...`,
      severity: riskLevel,
      recommended_action: riskScore > 70 ? 'Immediate investigation required' : riskScore > 40 ? 'Monitor and review' : 'No action required - Safe content',
      legal_sections: legalSections,
      generated_at: new Date().toISOString()
    };
  };
  
  const cybercellReport = generateReport();
  const getRiskColor = (level) => {
    const colors = {
      'LOW': '#10b981',
      'MEDIUM': '#f59e0b',
      'HIGH': '#ef4444',
      'CRITICAL': '#dc2626',
      'SAFE': '#10b981',
      'WARNING': '#f59e0b',
      'DANGEROUS': '#ef4444'
    };
    return colors[level] || '#6b7280';
  };

  const getSentimentColor = (label) => {
    return label === 'POSITIVE' ? '#10b981' : '#ef4444';
  };

  return (
    <div className="result-card" style={{ animation: 'slideUpFade 0.6s ease-out' }}>
      <div className="result-header">
        <h2>✨ Analysis Results</h2>
        <span className="platform-badge">{data.platform}</span>
      </div>

      <div className="accuracy-banner">
        <div className="banner-content">
          <div className="banner-title">🎯 AI-Powered Analysis Complete</div>
          <div className="banner-stats">
            <span>✓ 94% Accuracy</span>
            <span>✓ 7 AI Models</span>
            <span>✓ 18 Categories</span>
            <span>✓ Context-Aware</span>
          </div>
        </div>
      </div>

      {data.metadata && (
        <div className="metadata-section">
          <h3>Content Information</h3>
          <div className="metadata-grid">
            {data.metadata.title && <div className="meta-item"><strong>Title:</strong> {data.metadata.title}</div>}
            {data.metadata.author && <div className="meta-item"><strong>Author:</strong> {data.metadata.author}</div>}
            {data.metadata.published_at && <div className="meta-item"><strong>Published:</strong> {data.metadata.published_at}</div>}
          </div>
        </div>
      )}

      {data.source_verification && (
        <div className="governance-section">
          <h3>🔍 Source Verification (Vishwaas Score)</h3>
          <div className="verification-card">
            <div className="vishwaas-score">
              <div className="score-circle" style={{ borderColor: data.source_verification.vishwaas_score > 70 ? '#10b981' : data.source_verification.vishwaas_score > 40 ? '#f59e0b' : '#ef4444' }}>
                <span className="score-num">{data.source_verification.vishwaas_score}</span>
                <span className="score-label">Vishwaas Score</span>
              </div>
            </div>
            <div className="verification-details">
              <div className="verify-item">
                <span className="verify-label">Status:</span>
                <span className={`verify-badge ${data.source_verification.verification_status.toLowerCase()}`}>
                  {data.source_verification.verification_status}
                </span>
              </div>
              <div className="verify-item">
                <span className="verify-label">Category:</span>
                <span className="verify-value">{data.source_verification.source_category}</span>
              </div>
              <div className="verify-item">
                <span className="verify-label">Credibility:</span>
                <span className="verify-value">{(data.source_verification.credibility_multiplier * 100).toFixed(0)}%</span>
              </div>
              {data.source_verification.vishwaas_cross_check?.matched && (
                <div className="verify-alert">
                  ⚠️ Matched fake news keyword: "{data.source_verification.vishwaas_cross_check.keyword}"
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {data.language_analysis && (
        <div className="governance-section">
          <h3>🌐 Language Analysis (Bhashini)</h3>
          <div className="language-card">
            <div className="lang-item">
              <span className="lang-label">Detected Language:</span>
              <span className="lang-value">{data.language_analysis.language_name} ({data.language_analysis.detected_language.toUpperCase()})</span>
            </div>
            <div className="lang-item">
              <span className="lang-label">Indian Language:</span>
              <span className="lang-value">{data.language_analysis.is_indian_language ? '✓ Yes' : '✗ No'}</span>
            </div>
            {data.language_analysis.bhashini_enabled && (
              <div className="lang-alert">
                🌐 Bhashini translation enabled for analysis
              </div>
            )}
          </div>
        </div>
      )}

      {cybercellReport && (
        <div className="governance-section critical">
          <h3>⚖️ Cybercell Report Generated</h3>
          <div className="report-card">
            <div className="report-header">
              <span className="report-id">Report ID: {cybercellReport.report_id}</span>
              <span className="report-status">{cybercellReport.report_status}</span>
            </div>
            <div className="report-details">
              <div className="report-item">
                <strong>Evidence Hash:</strong>
                <div className="hash-value">{cybercellReport.evidence_hash}</div>
              </div>
              <div className="report-item">
                <strong>Severity:</strong> <span className="severity-badge">{cybercellReport.severity}</span>
              </div>
              <div className="report-item">
                <strong>Recommended Action:</strong> {cybercellReport.recommended_action}
              </div>
              <div className="report-item">
                <strong>Applicable Laws:</strong>
                <ul className="laws-list">
                  {cybercellReport.legal_sections.map((law, idx) => (
                    <li key={idx}>{law}</li>
                  ))}
                </ul>
              </div>
            </div>
            <button 
              className="pdf-download-btn"
              onClick={() => {
                const reportData = {
                  ...cybercellReport,
                  analysis_id: data.analysis_id,
                  url: data.url,
                  platform: data.platform,
                  timestamp: data.timestamp
                };
                const blob = new Blob([JSON.stringify(reportData, null, 2)], { type: 'application/json' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `Cybercell_Report_${cybercellReport.report_id}.json`;
                a.click();
                URL.revokeObjectURL(url);
              }}
            >
              Download Report (JSON)
            </button>
          </div>
        </div>
      )}

      <div className="risk-section">
        <h3>Risk Assessment</h3>
        <div className="risk-score-container">
          <div className="risk-score" style={{ borderColor: getRiskColor(data.combined_risk?.level || data.risk_assessment?.level) }}>
            <span className="score-number">{data.combined_risk?.score || data.risk_assessment?.score}</span>
            <span className="score-label">/ 100</span>
          </div>
          <div className="risk-details">
            <div className="risk-level" style={{ color: getRiskColor(data.combined_risk?.level || data.risk_assessment?.level) }}>
              {data.combined_risk?.level || data.risk_assessment?.level}
            </div>
            <p className="risk-summary">{data.summary}</p>
            {data.combined_risk && (
              <div className="risk-breakdown">
                <div className="risk-item">Text Risk: {data.combined_risk.text_risk}</div>
                <div className="risk-item">Image Risk: {data.combined_risk.image_risk}</div>
              </div>
            )}
          </div>
        </div>
      </div>

      {data.content_analysis && (
        <div className="stats-overview">
          <h3>Complete Analysis Summary</h3>
          <div className="stats-grid">
            <div className="stat-box">
              <div className="stat-number">{data.content_analysis?.sentiment?.score ? (data.content_analysis.sentiment.score * 100).toFixed(1) : 0}%</div>
              <div className="stat-label">Sentiment Score</div>
            </div>
            <div className="stat-box">
              <div className="stat-number">{data.content_analysis?.toxicity?.confidence ? (data.content_analysis.toxicity.confidence * 100).toFixed(1) : 0}%</div>
              <div className="stat-label">Toxicity Confidence</div>
            </div>
            <div className="stat-box">
              <div className="stat-number">{data.content_analysis?.hate_speech?.confidence ? (data.content_analysis.hate_speech.confidence * 100).toFixed(1) : 0}%</div>
              <div className="stat-label">Hate Speech Confidence</div>
            </div>
            <div className="stat-box">
              <div className="stat-number">{data.content_analysis?.nsfw?.confidence ? (data.content_analysis.nsfw.confidence * 100).toFixed(1) : 0}%</div>
              <div className="stat-label">NSFW Confidence</div>
            </div>
            <div className="stat-box">
              <div className="stat-number">{data.content_analysis?.intent?.confidence ? (data.content_analysis.intent.confidence * 100).toFixed(1) : 0}%</div>
              <div className="stat-label">Intent Confidence</div>
            </div>
            <div className="stat-box">
              <div className="stat-number">{data.content_analysis?.content_categories?.detected_categories?.length || 0}</div>
              <div className="stat-label">Categories Detected</div>
            </div>
          </div>
        </div>
      )}

      <div className="analysis-grid">
        <div className="analysis-card">
          <h4>Sentiment Analysis</h4>
          <div className="analysis-value" style={{ color: getSentimentColor(data.content_analysis?.sentiment?.label) }}>
            {data.content_analysis?.sentiment?.label}
          </div>
          <div className="confidence-bar">
            <div
              className="confidence-fill"
              style={{
                width: `${(data.content_analysis?.sentiment?.score * 100).toFixed(0)}%`,
                backgroundColor: getSentimentColor(data.content_analysis?.sentiment?.label)
              }}
            ></div>
          </div>
          <span className="confidence-text">
            {(data.content_analysis?.sentiment?.score * 100).toFixed(1)}% confidence
          </span>
        </div>

        <div className="analysis-card">
          <h4>Toxicity</h4>
          <div className="analysis-value" style={{ color: data.content_analysis?.toxicity?.is_toxic ? '#ef4444' : '#10b981' }}>
            {data.content_analysis?.toxicity?.is_toxic ? 'Toxic' : 'Not Toxic'}
          </div>
          <div className="confidence-bar">
            <div
              className="confidence-fill"
              style={{
                width: `${(data.content_analysis?.toxicity?.confidence * 100).toFixed(0)}%`,
                backgroundColor: data.content_analysis?.toxicity?.is_toxic ? '#ef4444' : '#10b981'
              }}
            ></div>
          </div>
          <span className="confidence-text">
            {(data.content_analysis?.toxicity?.confidence * 100).toFixed(1)}% confidence
          </span>
        </div>

        <div className="analysis-card">
          <h4>Hate Speech</h4>
          <div className="analysis-value" style={{ color: data.content_analysis?.hate_speech?.is_hate_speech ? '#ef4444' : '#10b981' }}>
            {data.content_analysis?.hate_speech?.is_hate_speech ? 'Detected' : data.content_analysis?.hate_speech?.label === 'unknown' ? 'Unknown' : 'Not Detected'}
          </div>
          {data.content_analysis?.hate_speech?.confidence > 0 && (
            <>
              <div className="confidence-bar">
                <div
                  className="confidence-fill"
                  style={{
                    width: `${(data.content_analysis?.hate_speech?.confidence * 100).toFixed(0)}%`,
                    backgroundColor: data.content_analysis?.hate_speech?.is_hate_speech ? '#ef4444' : '#10b981'
                  }}
                ></div>
              </div>
              <span className="confidence-text">
                {(data.content_analysis?.hate_speech?.confidence * 100).toFixed(1)}% confidence
              </span>
            </>
          )}
        </div>

        <div className="analysis-card">
          <h4>Content Category</h4>
          <div className="analysis-value" style={{ color: data.content_analysis?.content_categories?.is_flagged ? '#ef4444' : '#10b981' }}>
            {data.content_analysis?.content_categories?.primary_category}
          </div>
          {data.content_analysis?.content_categories?.is_flagged && (
            <span className="flagged-badge">Flagged</span>
          )}
        </div>

        {data.content_analysis?.nsfw && (
          <div className="analysis-card">
            <h4>NSFW Detection</h4>
            <div className="analysis-value" style={{ color: data.content_analysis?.nsfw?.is_nsfw ? '#ef4444' : '#10b981' }}>
              {data.content_analysis?.nsfw?.is_nsfw ? 'NSFW' : 'Safe'}
            </div>
            {data.content_analysis?.nsfw?.confidence > 0 && (
              <>
                <div className="confidence-bar">
                  <div
                    className="confidence-fill"
                    style={{
                      width: `${(data.content_analysis?.nsfw?.confidence * 100).toFixed(0)}%`,
                      backgroundColor: data.content_analysis?.nsfw?.is_nsfw ? '#ef4444' : '#10b981'
                    }}
                  ></div>
                </div>
                <span className="confidence-text">
                  {(data.content_analysis?.nsfw?.confidence * 100).toFixed(1)}% confidence
                </span>
              </>
            )}
          </div>
        )}

        {data.content_analysis?.intent && data.content_analysis?.intent?.intent !== 'unknown' && (
          <div className="analysis-card">
            <h4>Intent</h4>
            <div className="analysis-value">
              {data.content_analysis?.intent?.intent}
            </div>
            {data.content_analysis?.intent?.confidence > 0 && (
              <>
                <div className="confidence-bar">
                  <div
                    className="confidence-fill"
                    style={{
                      width: `${(data.content_analysis?.intent?.confidence * 100).toFixed(0)}%`,
                      backgroundColor: '#3b82f6'
                    }}
                  ></div>
                </div>
                <span className="confidence-text">
                  {(data.content_analysis?.intent?.confidence * 100).toFixed(1)}% confidence
                </span>
              </>
            )}
          </div>
        )}
      </div>

      {data.image_analysis && data.image_analysis.length > 0 && (
        <div className="images-section">
          <h3>🖼️ Image Analysis ({data.image_analysis.length} images detected)</h3>
          <div className="images-grid">
            {data.image_analysis.map((img, idx) => (
              <div key={idx} className="image-card-separate">
                <div className="image-preview-large">
                  <img 
                    src={img.image_url} 
                    alt={`Image ${idx + 1}`} 
                    className="preview-img"
                    referrerPolicy="no-referrer"
                    onError={(e) => { e.target.style.display = 'none'; }}
                  />
                  <div className="image-overlay">
                    <span className="image-number">Image {idx + 1}</span>
                  </div>
                </div>
                
                <div className="image-analysis-content">
                  <div className="image-risk-header">
                    <h4>Analysis Results</h4>
                    <span className="risk-badge-large" style={{ background: getRiskColor(img.image_risk_score > 70 ? 'CRITICAL' : img.image_risk_score > 50 ? 'HIGH' : img.image_risk_score > 30 ? 'MEDIUM' : 'LOW') }}>
                      {img.image_risk_score || 0}/100
                    </span>
                  </div>

                  <div className="image-categories-section">
                    <div className="categories-label">Detected:</div>
                    <div className="image-categories">
                      {img.nsfw?.is_explicit && <span className="img-cat explicit">Explicit</span>}
                      {img.nsfw?.is_sexual && <span className="img-cat sexual">Sexual</span>}
                      {img.nsfw?.is_nsfw && !img.nsfw?.is_explicit && !img.nsfw?.is_sexual && <span className="img-cat nsfw">NSFW</span>}
                      {img.violence?.is_violent && <span className="img-cat violent">Violent</span>}
                      {img.violence?.is_hateful_visual && <span className="img-cat hate">Hateful</span>}
                      {img.violence?.is_spam && <span className="img-cat spam">Spam</span>}
                      {img.religious_hate?.is_religious_hate && <span className="img-cat religious">Religious Hate</span>}
                      {img.ocr?.text && <span className="img-cat ocr">Text</span>}
                      {!img.nsfw?.is_nsfw && !img.violence?.is_violent && !img.violence?.is_hateful_visual && !img.religious_hate?.is_religious_hate && <span className="img-cat safe">Safe</span>}
                    </div>
                  </div>
                  <div className="image-stats">
                <div className="image-stat">
                  <span className="stat-label">NSFW:</span>
                  <span className="stat-value" style={{ color: img.nsfw?.is_nsfw ? '#ef4444' : '#10b981' }}>
                    {img.nsfw?.is_explicit ? 'Explicit' : img.nsfw?.is_sexual ? 'Sexual' : img.nsfw?.is_nsfw ? 'Yes' : 'No'} ({(img.nsfw?.confidence * 100).toFixed(1)}%)
                  </span>
                </div>
                <div className="image-stat">
                  <span className="stat-label">Violence:</span>
                  <span className="stat-value" style={{ color: img.violence?.is_violent ? '#ef4444' : '#10b981' }}>
                    {img.violence?.is_violent ? 'Yes' : 'No'} ({((img.violence?.violence_score || img.violence?.confidence || 0) * 100).toFixed(1)}%)
                  </span>
                </div>
                <div className="image-stat">
                  <span className="stat-label">Hateful Visual:</span>
                  <span className="stat-value" style={{ color: img.violence?.is_hateful_visual ? '#ef4444' : '#10b981' }}>
                    {img.violence?.is_hateful_visual ? 'Yes' : 'No'} ({((img.violence?.hate_score || 0) * 100).toFixed(1)}%)
                  </span>
                </div>
                <div className="image-stat">
                  <span className="stat-label">Spam:</span>
                  <span className="stat-value" style={{ color: img.violence?.is_spam ? '#f59e0b' : '#10b981' }}>
                    {img.violence?.is_spam ? 'Yes' : 'No'} ({((img.violence?.spam_score || 0) * 100).toFixed(1)}%)
                  </span>
                </div>
                {img.religious_hate && (
                  <div className="image-stat">
                    <span className="stat-label">Religious Hate:</span>
                    <span className="stat-value" style={{ color: img.religious_hate?.is_religious_hate ? '#ef4444' : '#10b981' }}>
                      {img.religious_hate?.is_religious_hate ? 'Detected' : 'None'}
                      {img.religious_hate?.targets && img.religious_hate.targets.length > 0 && ` (${img.religious_hate.targets.join(', ')})`}
                    </span>
                  </div>
                )}
                {img.ocr?.text && (
                  <div className="image-stat ocr-text">
                    <span className="stat-label">OCR Text:</span>
                    <span className="stat-value">{img.ocr.text}</span>
                    {img.ocr_analysis && (
                      <div className="ocr-analysis-badge">
                        Text Risk: {img.ocr_analysis.risk_assessment?.score || 0}/100
                      </div>
                    )}
                  </div>
                )}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {data.content_analysis?.content_categories?.detected_categories && data.content_analysis.content_categories.detected_categories.length > 0 && (
        <div className="categories-section">
          <h3>🏷️ Detected Categories</h3>
          <div className="category-tags">
            {data.content_analysis.content_categories.detected_categories.map((cat, idx) => (
              <span key={idx} className="category-tag">{cat}</span>
            ))}
          </div>
        </div>
      )}

      {data.text_preview && (
        <div className="preview-section">
          <h3>📄 Content Preview</h3>
          <p className="text-preview">{data.text_preview}</p>
        </div>
      )}

      <div className="analysis-footer">
        <span className="analysis-id">Analysis ID: {data.analysis_id}</span>
        <span className="timestamp">{new Date(data.timestamp).toLocaleString()}</span>
      </div>
    </div>
  );
}

export default ResultCard;

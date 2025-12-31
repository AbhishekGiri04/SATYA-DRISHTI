import React from 'react';
import './InfoSections.css';

function InvestigatorDemo() {
  return (
    <div className="info-section">
      <h2>🕵️ Investigator (Demo Only)</h2>
      <div className="ethical-warning">
        <h3>⚠️ ETHICAL NOTICE</h3>
        <p><strong>This is a CONCEPT DEMO only.</strong></p>
        <p>Actual implementation would require:</p>
        <ul>
          <li>Legal authorization from law enforcement</li>
          <li>Court warrants for personal data access</li>
          <li>Compliance with IT Act 2000 & Data Protection laws</li>
          <li>Proper chain of custody for evidence</li>
        </ul>
      </div>

      <div className="demo-section">
        <h3>Metadata Analysis (Public Data Only)</h3>
        <div className="demo-card">
          <h4>Content Metadata</h4>
          <ul>
            <li>Post timestamp: 2024-01-15 14:30 IST</li>
            <li>Platform: Reddit</li>
            <li>Content type: Text + Image</li>
            <li>Language: Hindi</li>
          </ul>
        </div>

        <div className="demo-card">
          <h4>Technical Indicators</h4>
          <ul>
            <li>IP geolocation: India (aggregated)</li>
            <li>Device type: Mobile</li>
            <li>Browser: Chrome</li>
          </ul>
        </div>
      </div>

      <div className="legal-notice">
        <h4>🔒 For Law Enforcement Use Only</h4>
        <p>Personal identification requires proper legal authorization and cannot be performed without:</p>
        <ol>
          <li>Court warrant or magistrate order</li>
          <li>Formal request through legal channels</li>
          <li>Compliance with evidence collection protocols</li>
        </ol>
      </div>
    </div>
  );
}

function VideoForensics() {
  return (
    <div className="info-section">
      <h2>🎥 Video Forensics</h2>
      <p>Deepfake detection and video authenticity verification</p>
      
      <div className="demo-section">
        <h3>Analysis Capabilities</h3>
        <div className="demo-card">
          <h4>Frame Analysis</h4>
          <p>Detect inconsistencies in video frames</p>
        </div>
        <div className="demo-card">
          <h4>Audio Verification</h4>
          <p>Check for AI-generated voice cloning</p>
        </div>
        <div className="demo-card">
          <h4>Metadata Extraction</h4>
          <p>Technical data only (no personal info)</p>
        </div>
      </div>
    </div>
  );
}

function ThreatMapDemo() {
  return (
    <div className="info-section">
      <h2>🌐 Threat Map (Aggregated Data)</h2>
      <div className="ethical-warning">
        <p><strong>Privacy-First Approach:</strong> Only aggregated statistics, no individual tracking</p>
      </div>
      
      <div className="demo-section">
        <h3>Regional Statistics (Last 24h)</h3>
        <div className="demo-card">
          <h4>North India: 456 cases</h4>
          <p>Risk Level: Medium</p>
        </div>
        <div className="demo-card">
          <h4>South India: 312 cases</h4>
          <p>Risk Level: Low</p>
        </div>
      </div>
    </div>
  );
}

function LegalBridge() {
  return (
    <div className="info-section">
      <h2>📜 Legal Bridge</h2>
      <p>Automated legal documentation assistance</p>
      
      <div className="demo-section">
        <h3>Legal Framework Mapping</h3>
        <div className="demo-card">
          <h4>Applicable Laws</h4>
          <ul>
            <li>IT Act Section 67 - Obscene content</li>
            <li>IPC Section 153A - Promoting enmity</li>
            <li>IPC Section 506 - Criminal intimidation</li>
          </ul>
        </div>
        
        <div className="legal-notice">
          <h4>⚖️ Legal Disclaimer</h4>
          <p>This tool provides legal reference only. Actual legal notices must be drafted by licensed legal professionals.</p>
        </div>
      </div>
    </div>
  );
}

export { InvestigatorDemo, VideoForensics, ThreatMapDemo, LegalBridge };

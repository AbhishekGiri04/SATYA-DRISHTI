import React, { useState, useEffect } from 'react';
import './ThreatMap.css';

function ThreatMap() {
  const [stats, setStats] = useState({
    totalAnalyzed: 0,
    highRisk: 0,
    regions: []
  });

  useEffect(() => {
    // Simulated aggregated statistics (no personal data)
    setStats({
      totalAnalyzed: 124567,
      highRisk: 2847,
      regions: [
        { state: 'Maharashtra', count: 456, risk: 'medium' },
        { state: 'Delhi', count: 389, risk: 'high' },
        { state: 'Karnataka', count: 312, risk: 'medium' },
        { state: 'Tamil Nadu', count: 267, risk: 'low' }
      ]
    });
  }, []);

  return (
    <div className="threat-map">
      <h2>📊 Threat Intelligence Dashboard</h2>
      <p className="disclaimer">Aggregated statistics only - No personal data collected</p>
      
      <div className="stats-overview">
        <div className="stat-card">
          <h3>{stats.totalAnalyzed.toLocaleString()}</h3>
          <p>Content Analyzed (24h)</p>
        </div>
        <div className="stat-card critical">
          <h3>{stats.highRisk.toLocaleString()}</h3>
          <p>High Risk Detected</p>
        </div>
        <div className="stat-card success">
          <h3>{((1 - stats.highRisk/stats.totalAnalyzed) * 100).toFixed(1)}%</h3>
          <p>Safe Content</p>
        </div>
      </div>

      <div className="regional-stats">
        <h3>Regional Content Analysis (Aggregated)</h3>
        {stats.regions.map((region, idx) => (
          <div key={idx} className={`region-item ${region.risk}`}>
            <span className="region-name">{region.state}</span>
            <div className="region-bar">
              <div className="bar-fill" style={{width: `${(region.count/500)*100}%`}}></div>
            </div>
            <span className="region-count">{region.count} cases</span>
          </div>
        ))}
      </div>

      <div className="ethical-notice">
        <h4>🔒 Privacy & Ethics</h4>
        <ul>
          <li>No personal information collected or stored</li>
          <li>Only content analysis, not user tracking</li>
          <li>Compliant with IT Act 2000 & Data Protection laws</li>
          <li>For law enforcement use only with proper authorization</li>
        </ul>
      </div>
    </div>
  );
}

export default ThreatMap;

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './GovernanceDashboard.css';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8001';

function GovernanceDashboard() {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchStats();
    const interval = setInterval(fetchStats, 5000); // Refresh every 5 seconds
    return () => clearInterval(interval);
  }, []);

  const fetchStats = async () => {
    try {
      const response = await axios.get(`${API_URL}/governance/stats/dashboard`);
      setStats(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Failed to fetch stats:', error);
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading">Loading dashboard...</div>;
  }

  return (
    <div className="governance-dashboard">
      <div className="dashboard-header">
        <h1>🏛️ Governance Dashboard</h1>
        <p className="subtitle">Real-time Content Moderation Analytics for Law Enforcement</p>
      </div>

      <div className="stats-grid">
        <div className="stat-card primary">
          <div className="stat-icon">📊</div>
          <div className="stat-content">
            <div className="stat-value">{stats?.daily_analysis?.total_content_analyzed || 0}</div>
            <div className="stat-label">Total Content Analyzed</div>
          </div>
        </div>

        <div className="stat-card danger">
          <div className="stat-icon">⚠️</div>
          <div className="stat-content">
            <div className="stat-value">{stats?.daily_analysis?.high_risk_detected || 0}</div>
            <div className="stat-label">High Risk Detected</div>
          </div>
        </div>

        <div className="stat-card success">
          <div className="stat-icon">📋</div>
          <div className="stat-content">
            <div className="stat-value">{stats?.daily_analysis?.reports_generated || 0}</div>
            <div className="stat-label">Reports Generated</div>
          </div>
        </div>

        <div className="stat-card info">
          <div className="stat-icon">✓</div>
          <div className="stat-content">
            <div className="stat-value">{stats?.daily_analysis?.false_positives || 0}</div>
            <div className="stat-label">False Positives</div>
          </div>
        </div>
      </div>

      <div className="dashboard-sections">
        <div className="section">
          <h3>🎯 Threat Categories</h3>
          <div className="category-list">
            {stats?.threat_categories && Object.keys(stats.threat_categories).length > 0 ? (
              Object.entries(stats.threat_categories).map(([category, count]) => (
                <div key={category} className="category-item">
                  <span className="category-name">{category.replace(/_/g, ' ')}</span>
                  <span className="category-count">{count}</span>
                </div>
              ))
            ) : (
              <p className="no-data">No threats detected yet</p>
            )}
          </div>
        </div>

        <div className="section">
          <h3>🌐 Language Distribution</h3>
          <div className="language-list">
            {stats?.language_distribution && Object.keys(stats.language_distribution).length > 0 ? (
              Object.entries(stats.language_distribution).map(([lang, count]) => (
                <div key={lang} className="language-item">
                  <span className="language-code">{lang.toUpperCase()}</span>
                  <div className="language-bar">
                    <div 
                      className="language-fill" 
                      style={{ width: `${(count / stats.daily_analysis.total_content_analyzed) * 100}%` }}
                    ></div>
                  </div>
                  <span className="language-count">{count}</span>
                </div>
              ))
            ) : (
              <p className="no-data">No language data yet</p>
            )}
          </div>
        </div>
      </div>

      <div className="features-section">
        <h3>🛡️ Active Features</h3>
        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon">✓</div>
            <div className="feature-name">Source Verification</div>
            <div className="feature-status active">Active</div>
          </div>
          <div className="feature-card">
            <div className="feature-icon">✓</div>
            <div className="feature-name">Multilingual Support</div>
            <div className="feature-status active">Active</div>
          </div>
          <div className="feature-card">
            <div className="feature-icon">✓</div>
            <div className="feature-name">Cybercell Reports</div>
            <div className="feature-status active">Active</div>
          </div>
          <div className="feature-card">
            <div className="feature-icon">✓</div>
            <div className="feature-name">Legal Compliance</div>
            <div className="feature-status active">Active</div>
          </div>
        </div>
      </div>

      <div className="timestamp">
        Last updated: {stats?.timestamp ? new Date(stats.timestamp).toLocaleString() : 'N/A'}
      </div>
    </div>
  );
}

export default GovernanceDashboard;

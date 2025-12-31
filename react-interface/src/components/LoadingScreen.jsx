import React, { useEffect, useState } from 'react';
import './LoadingScreen.css';

const LoadingScreen = ({ onComplete }) => {
  useEffect(() => {
    const timer = setTimeout(() => {
      onComplete();
    }, 3000);

    return () => clearTimeout(timer);
  }, [onComplete]);

  return (
    <div className="loading-screen">
      <div className="loading-content">
        <img 
          src="https://seceon.com/wp-content/uploads/2024/09/government.gif" 
          alt="Loading" 
          className="loading-gif"
        />
        <h1 className="loading-title">SATYA-DRISHTI</h1>
        <p className="loading-subtitle">Digital Suraksha</p>
        <div className="loading-spinner">
          <div className="spinner-dot"></div>
          <div className="spinner-dot"></div>
          <div className="spinner-dot"></div>
        </div>
      </div>
    </div>
  );
};

export default LoadingScreen;

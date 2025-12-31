#!/bin/bash
set -e

echo "🇮🇳 SATYA-DRISHTI - Digital Suraksha Framework"
echo "Developer: Abhishek Giri | GitHub: abhishekgiri04"
echo "================================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.8+"
    exit 1
fi

# Check Node
if ! command -v npm &> /dev/null; then
    echo "❌ Node.js/npm not found. Please install Node.js 16+"
    exit 1
fi

echo "✅ Prerequisites check passed"
echo ""

# Backend Setup
echo "📦 Setting up Backend API..."
cd "$(dirname "$0")/social-intel-agent"

if [ -d "venv" ]; then
    echo "   Removing old virtual environment..."
    rm -rf venv
fi

echo "   Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "   Installing Python dependencies..."
pip install --upgrade pip setuptools wheel -q
pip install -r requirements.txt -q

echo "   Installing Playwright browser..."
playwright install chromium --with-deps

echo "   ✅ Backend ready"
echo ""

# Frontend Setup
echo "📦 Setting up Frontend Dashboard..."
cd ../react-interface

echo "   Installing Node dependencies..."
npm install --silent

echo "   ✅ Frontend ready"
echo ""

# Success
echo "================================================"
echo "✅ Installation Complete!"
echo "================================================"
echo ""
echo "🚀 Start the application:"
echo "   ./run.sh"
echo ""
echo "📡 Access Points:"
echo "   Backend API:  http://localhost:8001"
echo "   Frontend App: http://localhost:5173"
echo ""
echo "📚 Documentation: README.md"
echo "🇮🇳 Built for Digital India"

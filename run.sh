#!/bin/bash

echo "🇮🇳 Starting SATYA-DRISHTI - Digital Suraksha Framework"
echo "Developer: Abhishek Giri | GitHub: abhishekgiri04"
echo "===================================================="
echo ""

# Cleanup existing processes
echo "🧹 Cleaning up existing processes..."
lsof -ti:8001 | xargs kill -9 2>/dev/null || true
lsof -ti:5173 | xargs kill -9 2>/dev/null || true
echo "   ✅ Ports cleared"
echo ""

# Start Backend
echo "🚀 Starting Backend API..."
cd "$(dirname "$0")/social-intel-agent"

if [ ! -d "venv" ]; then
    echo "   ❌ Virtual environment not found!"
    echo "   Run: ./INSTALL.sh first"
    exit 1
fi

source venv/bin/activate
uvicorn src.app:app --port 8001 --reload &
BACKEND_PID=$!
echo "   ✅ Backend started (PID: $BACKEND_PID)"
echo "   📡 API: http://localhost:8001"
echo ""

sleep 3

# Start Frontend
echo "🚀 Starting Frontend Dashboard..."
cd ../react-interface

if [ ! -d "node_modules" ]; then
    echo "   ❌ Node modules not found!"
    echo "   Run: ./INSTALL.sh first"
    kill $BACKEND_PID 2>/dev/null
    exit 1
fi

npm run dev &
FRONTEND_PID=$!
echo "   ✅ Frontend started (PID: $FRONTEND_PID)"
echo "   📡 Dashboard: http://localhost:5173"
echo ""

# Success message
echo "===================================================="
echo "✅ SATYA-DRISHTI is running!"
echo "===================================================="
echo ""
echo "📊 Access Points:"
echo "   Backend API:       http://localhost:8001"
echo "   Frontend Dashboard: http://localhost:5173"
echo "   API Docs:          http://localhost:8001/docs"
echo ""
echo "🔍 Features:"
echo "   • Source Verification (Vishwaas Score)"
echo "   • Multilingual Support (Bhashini)"
echo "   • Cybercell Reports"
echo "   • 7 AI Models (950MB)"
echo ""
echo "⏸️  Press Ctrl+C to stop both services"
echo ""

# Trap to cleanup on exit
trap "echo ''; echo '🛑 Stopping services...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; echo '✅ Stopped'; exit" INT

# Wait for processes
wait

#!/bin/bash

echo "🚀 SongGen Deployment Script"
echo "=============================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 ไม่ได้ติดตั้ง กรุณาติดตั้ง Python3 ก่อน"
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 ไม่ได้ติดตั้ง กรุณาติดตั้ง pip3 ก่อน"
    exit 1
fi

echo "✅ Python3 และ pip3 พร้อมใช้งาน"

# Install dependencies
echo "📦 ติดตั้ง dependencies..."
pip3 install -r requirements.txt

# Create output directory
echo "📁 สร้างโฟลเดอร์ output..."
mkdir -p static/output

# Check if port 5001 is available
if lsof -Pi :5001 -sTCP:LISTEN -t >/dev/null ; then
    echo "⚠️  Port 5001 ถูกใช้งานอยู่ เปลี่ยนเป็น port 5002"
    PORT=5002
else
    PORT=5001
fi

echo "🎵 เริ่มต้น SongGen ที่ port $PORT..."
echo "🌐 เปิดเว็บเบราว์เซอร์ไปที่: http://localhost:$PORT"
echo "⏹️  กด Ctrl+C เพื่อหยุดโปรแกรม"
echo ""

# Run the application
python3 app.py 
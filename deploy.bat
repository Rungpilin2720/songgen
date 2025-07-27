@echo off
echo 🚀 SongGen Deployment Script
echo ==============================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python ไม่ได้ติดตั้ง กรุณาติดตั้ง Python ก่อน
    pause
    exit /b 1
)

echo ✅ Python พร้อมใช้งาน

REM Install dependencies
echo 📦 ติดตั้ง dependencies...
pip install -r requirements.txt

REM Create output directory
echo 📁 สร้างโฟลเดอร์ output...
if not exist "static\output" mkdir static\output

echo 🎵 เริ่มต้น SongGen...
echo 🌐 เปิดเว็บเบราว์เซอร์ไปที่: http://localhost:5001
echo ⏹️  กด Ctrl+C เพื่อหยุดโปรแกรม
echo.

REM Run the application
python app.py 
# SongGen Deployment Guide

## วิธี Deploy SongGen

### 1. Deploy บน Railway (แนะนำ - ง่ายที่สุด)

1. สร้างบัญชีที่ [Railway](https://railway.app/)
2. Connect GitHub repository
3. Railway จะ auto-detect และ deploy โดยอัตโนมัติ
4. ใช้ไฟล์ `Procfile` และ `runtime.txt` ที่มีอยู่แล้ว

### 2. Deploy บน Render

1. สร้างบัญชีที่ [Render](https://render.com/)
2. Connect GitHub repository
3. เลือก "Web Service"
4. ใช้ไฟล์ `render.yaml` ที่มีอยู่แล้ว

### 3. Deploy บน VPS/Server

#### ใช้ Docker:
```bash
# Build Docker image
docker build -t songgen-app .

# Run container
docker run -p 8000:8000 songgen-app
```

#### ใช้ Gunicorn:
```bash
# Install dependencies
pip install -r requirements.txt

# Run with Gunicorn
gunicorn --config gunicorn_config.py wsgi:app
```

### 4. Deploy บน Heroku

1. สร้างบัญชีที่ [Heroku](https://heroku.com/)
2. Install Heroku CLI
3. รันคำสั่ง:
```bash
heroku create your-app-name
git push heroku main
```

### 5. Deploy บน Google Cloud Run

1. สร้างบัญชี Google Cloud
2. Enable Cloud Run API
3. รันคำสั่ง:
```bash
gcloud builds submit --tag gcr.io/PROJECT-ID/songgen
gcloud run deploy --image gcr.io/PROJECT-ID/songgen --platform managed
```

## หมายเหตุสำคัญ

- โปรแกรมนี้ใช้ AI model ขนาดใหญ่ (1.3B parameters)
- ต้องใช้ RAM อย่างน้อย 4GB
- การ generate เพลงอาจใช้เวลา 30-60 วินาที
- ควรใช้ GPU สำหรับ performance ที่ดีขึ้น

## Environment Variables

- `PORT`: Port ที่จะรัน application (default: 5001)
- `DEBUG`: Set เป็น `False` สำหรับ production 
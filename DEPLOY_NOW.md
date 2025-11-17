# 🚀 Deploy SongGen ตอนนี้! (คำแนะนำฉบับย่อ)

## ⚠️ ปัญหาที่เจอ
Cloudflare tunnel URL หมดอายุแล้ว (DNS_PROBE_FINISHED_NXDOMAIN)

## ✅ วิธีแก้ไข - Deploy ใหม่

### วิธีที่ 1: Railway (แนะนำ - ง่ายที่สุด, ฟรี)

1. **ไปที่**: https://railway.app/
2. **สร้างบัญชี** (ใช้ GitHub login ได้)
3. **กด "New Project"** → เลือก "Deploy from GitHub repo"
4. **เลือก repository** ที่มีโค้ด SongGen
5. **Railway จะ deploy อัตโนมัติ** (ใช้ `Procfile` และ `runtime.txt`)
6. **ได้ URL ทันที** เช่น: `https://songgen-production.up.railway.app`

**ข้อดี:**
- ฟรี $5/เดือน
- Deploy อัตโนมัติเมื่อ push code
- ไม่ต้องตั้งค่าเอง

---

### วิธีที่ 2: Render (ฟรี, เสถียร)

1. **ไปที่**: https://render.com/
2. **สร้างบัญชี** (ใช้ GitHub login ได้)
3. **กด "New +"** → เลือก "Web Service"
4. **Connect GitHub** → เลือก repository
5. **ตั้งค่า**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python3 app.py`
   - Environment: Python 3
6. **กด "Create Web Service"**
7. **ได้ URL** เช่น: `https://songgen.onrender.com`

**หมายเหตุ:** ฟรี tier จะ sleep หลัง 15 นาทีไม่ใช้งาน

---

### วิธีที่ 3: Streamlit Cloud (ถ้าใช้ Streamlit)

1. **ไปที่**: https://share.streamlit.io/
2. **Login ด้วย GitHub**
3. **กด "New app"**
4. **เลือก repository** และไฟล์ `streamlit_app.py`
5. **กด "Deploy"**
6. **ได้ URL** เช่น: `https://songgen.streamlit.app`

---

### วิธีที่ 4: Cloudflare Tunnel (ถ้าต้องการใช้ต่อ)

1. **ติดตั้ง Cloudflare Tunnel**:
   ```bash
   brew install cloudflare/cloudflare/cloudflared  # macOS
   # หรือ
   wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
   ```

2. **Login**:
   ```bash
   cloudflared tunnel login
   ```

3. **สร้าง tunnel ใหม่**:
   ```bash
   cloudflared tunnel create songgen-tunnel
   ```

4. **รัน tunnel**:
   ```bash
   cloudflared tunnel --url http://localhost:5001
   ```

5. **ได้ URL ใหม่** (จะเปลี่ยนทุกครั้งที่รัน)

---

## 🔧 ตรวจสอบก่อน Deploy

### 1. ตรวจสอบว่า app รันได้ในเครื่อง:
```bash
# ติดตั้ง dependencies
pip install -r requirements.txt

# รัน app
python3 app.py
```

### 2. ตรวจสอบ port:
- Flask app ใช้ port จาก environment variable `PORT` (default: 5001)
- สำหรับ deployment platforms จะ set `PORT` ให้อัตโนมัติ

### 3. ตรวจสอบไฟล์ที่จำเป็น:
- ✅ `app.py` - Flask application
- ✅ `requirements.txt` - Dependencies (อัปเดตแล้ว)
- ✅ `Procfile` - สำหรับ Railway/Heroku
- ✅ `runtime.txt` - Python version
- ✅ `wsgi.py` - WSGI entry point
- ✅ `gunicorn_config.py` - Gunicorn config

---

## 📝 Environment Variables (ถ้าจำเป็น)

สำหรับ production, อาจต้องตั้งค่า:
- `PORT`: Port ที่จะรัน (platform จะ set ให้อัตโนมัติ)
- `DEBUG`: `False` สำหรับ production

---

## 🎯 หลัง Deploy สำเร็จ

1. **ทดสอบ URL** ที่ได้
2. **ทดสอบการสร้างเพลง**
3. **แชร์ URL** ให้คนอื่นใช้งาน

---

## ❓ ปัญหาที่อาจเจอ

### App ไม่รัน
- ตรวจสอบ logs ใน platform (Railway/Render)
- ตรวจสอบว่า dependencies ติดตั้งครบ

### Model โหลดไม่ได้
- ตรวจสอบว่า platform มี RAM เพียงพอ (อย่างน้อย 4GB)
- อาจต้องใช้ platform ที่มี GPU

### Timeout
- เพิ่ม timeout ใน `gunicorn_config.py` (ตั้งไว้ 300 วินาทีแล้ว)

---

## 🆘 ต้องการความช่วยเหลือ?

- Railway Docs: https://docs.railway.app/
- Render Docs: https://render.com/docs
- Streamlit Cloud: https://docs.streamlit.io/streamlit-community-cloud


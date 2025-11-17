# ⚠️ ปัญหา Streamlit Cloud กับ PyTorch

## ปัญหา:
Streamlit Cloud ไม่สามารถติดตั้ง PyTorch และ transformers ได้เพราะ:
- PyTorch ใหญ่มาก (หลาย GB)
- Streamlit Cloud มี memory/timeout limits
- การติดตั้งใช้เวลานานเกินไป

## ✅ วิธีแก้ไข: ใช้ Hugging Face Spaces แทน (แนะนำ!)

Hugging Face Spaces เหมาะกับ AI apps มากกว่าเพราะ:
- ✅ มี GPU ฟรี
- ✅ รองรับ PyTorch/transformers ได้ดี
- ✅ ไม่มีปัญหา timeout
- ✅ Auto-deploy เมื่อ push code

### ขั้นตอน:

1. **ไปที่**: https://huggingface.co/spaces
2. **Login** ด้วย GitHub
3. **กด "Create new Space"**
4. **ตั้งค่า**:
   - Space name: `songgen-ai`
   - SDK: `Streamlit`
   - Visibility: `Public`
5. **Connect GitHub**:
   - เลือก repository: `Rungpilin2720/songgen`
   - Branch: `main`
   - Main file: `streamlit_app.py`
6. **Deploy** - Hugging Face จะ deploy อัตโนมัติ
7. **ได้ URL**: `https://huggingface.co/spaces/your-username/songgen-ai`

---

## หรือลองแก้ไข requirements.txt ให้เบากว่า:

ถ้ายังต้องการใช้ Streamlit Cloud อาจต้อง:
1. ลด dependencies ที่ไม่จำเป็น
2. ใช้ PyTorch CPU-only version
3. หรือใช้ model ที่เล็กกว่า

แต่แนะนำใช้ Hugging Face Spaces มากกว่า!


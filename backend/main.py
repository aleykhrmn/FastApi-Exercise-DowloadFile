from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# CORS ayarları (React frontend'den gelen talepleri kabul etmek için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # "*" tüm kökenlere izin verir
    allow_credentials=True,
    allow_methods=["*"],  # Tüm HTTP metodlarına izin verir
    allow_headers=["*"],  # Tüm headerlara izin verir
)

# Dosyaların kaydedileceği klasör
UPLOAD_FOLDER = "./uploads"

# Klasörü oluştur (eğer yoksa)
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Klasöre yazma izni ver
os.chmod(UPLOAD_FOLDER, 0o755)

@app.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Dosyanın adını al
        file_location = os.path.join(UPLOAD_FOLDER, file.filename)
        
        # Dosyayı kaydet
        with open(file_location, "wb") as f:
            f.write(await file.read())
        
        # Başarı mesajı döndür
        return JSONResponse(content={"message": "Dosya başarıyla yüklendi"}, status_code=200)

    except Exception as e:
        # Hata durumunda mesaj döndür
        return JSONResponse(content={"message": str(e)}, status_code=500)

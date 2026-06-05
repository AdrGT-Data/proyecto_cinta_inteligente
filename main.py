import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
from datetime import datetime

# Inicializamos el microservicio
app = FastAPI(title="Cinta Seleccionadora - API MLOps")

# Definimos las rutas de nuestra arquitectura de carpetas
PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

@app.post("/process-image")
async def process_image(file: UploadFile = File(...)):
    # 1. Ingesta: Leer los bytes puros de la imagen recibida
    contents = await file.read()
    
    # 2. Transformación: Convertir bytes a matriz NumPy para que OpenCV pueda leerla
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        return JSONResponse(status_code=400, content={"error": "Archivo no válido o imagen corrupta"})

    # 3. Preprocesamiento de Visión Artificial (Preparando el Tensor)
    # Las CNNs suelen exigir entradas cuadradas (ej. 224x224)
    img_resized = cv2.resize(img, (224, 224))
    
    # 4. Patrón Claim-Check: Guardamos la imagen pesada en disco local
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"img_{timestamp}_{file.filename}"
    filepath = os.path.join(PROCESSED_DIR, filename)
    
    cv2.imwrite(filepath, img_resized)
    
    # 5. Salida: Generar el JSON ultraligero
    # Aquí es donde, en el futuro, la CNN inyectará su predicción real.
    # Por ahora mockeamos (simulamos) la respuesta.
    mock_color = "Pendiente_de_Inferencia" 
    mock_probabilidad = 0.0
    
    mensaje_kafka = {
        "timestamp": timestamp,
        "filename": filename,
        "ruta_disco": filepath,
        "color_predicho": mock_color,
        "probabilidad": mock_probabilidad,
        "estado": "procesado_ok"
    }
    
    # Este JSON es lo que enviaremos a Kafka más adelante
    return JSONResponse(content=mensaje_kafka)
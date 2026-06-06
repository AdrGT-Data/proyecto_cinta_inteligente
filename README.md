# Proyecto: Cinta Seleccionadora Inteligente (Edge-to-Cloud MLOps)

Este proyecto es un sistema autónomo de clasificación de objetos basado en visión artificial y arquitectura de datos distribuida. Desarrollado como parte de un sistema MLOps que integra hardware de borde (IoT), inferencia local y analítica en tiempo real.

## Arquitectura del Sistema
El sistema se divide en tres capas fundamentales:
1. **Edge (IoT):** ESP32-CAM y sensores ultrasónicos para la captura de eventos en tiempo real.
2. **Backend (Python/FastAPI):** Ingesta de imágenes, preprocesamiento con OpenCV e inferencia de modelos CNN (ONNX).
3. **Data Pipeline:** Integración con Apache Kafka y Spark Streaming para el procesamiento de eventos y monitorización en tiempo real.

## Módulos Actuales
- [/main.py](main.py): Microservicio FastAPI para la recepción y preprocesamiento de imágenes(En desarrollo).
- [/data/raw](data/raw/): Almacenamiento local de datos crudos (Ingesta).
- [/data/processed](data/processed/): Almacenamiento de datos transformados para entrenamiento/inferencia.

## Stack Tecnológico
- **Lenguaje:** Python 3.12+ (Gestionado con `uv`)
- **Visión Artificial:** OpenCV
- **Backend:** FastAPI
- **Infraestructura:** Apache Kafka & Spark Streaming (En desarrollo)
- **Modelado:** ONNX Runtime (CNNs de clasificación)

## Montaje Mecánico (MVP)
Diseño minimalista basado en impresiones 3D, poleas GT2 y motores NEMA 17. 

---
*Documentación desarrollada por Adrián para la participación en el IBM AI Builders Challenge 2026.*

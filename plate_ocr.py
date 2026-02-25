import os
import re
import base64
import cv2
import numpy as np
from ultralytics import YOLO
import easyocr
# 1. First, define where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---- configuration ----
# Connectivity: This looks for the .pt file in the same backend folder
YOLO_MODEL_PATH = os.path.join(BASE_DIR, "yolov8n.pt")
OCR_LANGS = os.getenv("OCR_LANGS", "en").split(",")
MIN_OCR_CONF = float(os.getenv("MIN_OCR_CONF", "0.4"))

# Load models into memory
_plate_detector = YOLO(YOLO_MODEL_PATH)
_ocr_reader = easyocr.Reader(OCR_LANGS, gpu=False) # Set gpu=True if you have CUDA

def extract_plate_from_base64(image_base64: str) -> dict:
    """
    Decodes base64 image, detects plate with YOLOv8, and extracts text via EasyOCR.
    Connectivity: This is called by the /api/visits route in app.py
    """
    try:
        _plate_detector = YOLO(YOLO_MODEL_PATH)
    # Indent this line by 4 spaces
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        _plate_detector = YOLO('yolov8n.pt')
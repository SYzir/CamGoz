import cv2
import pytesseract
from PIL import Image
import numpy as np

def ocr_detect():
    cap = cv2.VideoCapture(0) 
    if not cap.isOpened():
        print("Kamera açılamadı. Çıkılıyor...")
        return None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kameradan görüntü alınamadı.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(gray, lang='eng')
        
        cv2.putText(frame, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow("Realtime OCR", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return text

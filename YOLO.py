from ultralytics import YOLO
import cv2

def yolo_detect(frame,target_object=None, confidence_threshold=0.7):

    model = YOLO("yolo11n.pt")

    results = model.predict(source=frame, show=False, save=False)

    for result in results:
        for box in result.boxes:
            cls = box.cls[0]  
            confidence = box.conf[0]  

            if confidence >= confidence_threshold and model.names[int(cls)] == target_object:
                return model.names[int(cls)], confidence

    return None
    
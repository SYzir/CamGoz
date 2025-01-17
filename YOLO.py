from ultralytics import YOLO
import cv2

from ultralytics import YOLO
import cv2

def yolo_detect(target_object=None, confidence_threshold=0.7):

    model = YOLO("yolo11n.pt")

    
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Kamera açılamadı. Lütfen bağlantıyı kontrol edin.")
        return

    if target_object:
        print(f"Tespit edilecek nesne: {target_object}, Doğruluk eşiği: {confidence_threshold}")
    else:
        print(f"Tüm nesneler tespit edilecek, Doğruluk eşiği: {confidence_threshold}")

    while True:
        
        ret, frame = cap.read()

        if not ret:
            print("Kameradan görüntü alınamadı.")
            break

        
        results = model.predict(source=frame, show=False, save=False)

    
        detected_objects = []

        
        for result in results:
            for box in result.boxes:
                cls = box.cls[0]  
                confidence = box.conf[0]  

                if confidence >= confidence_threshold:
                    
                    if target_object and model.names[int(cls)] != target_object:
                        continue

                    
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    label = f"{model.names[int(cls)]}: {confidence * 100:.1f}%"

                    
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                    
                    print(f"Nesne: {model.names[int(cls)]}, Doğruluk: {confidence * 100:.1f}%")
                    detected_objects.append((model.names[int(cls)], confidence))

        
        if detected_objects:
            print("Tespit edilen nesneler:", detected_objects)


        cv2.imshow("Kamera - YOLO Nesne Tespiti", frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    
    cap.release()
    cv2.destroyAllWindows()

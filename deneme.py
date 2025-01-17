import cv2
from YOLO import yolo_detect

image_path = "insan.jpg"

result = yolo_detect(image_path)

print(result)
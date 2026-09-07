import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
EXCLUDE = {'person'}

TRASH_MAP = {
    'bottle': 'plastic', 'wine glass': 'glass', 'cup': 'general',
    'fork': 'general', 'knife': 'general', 'spoon': 'general',
    'bowl': 'general', 'banana': 'general', 'apple': 'general',
    'sandwich': 'general', 'orange': 'general', 'book': 'paper',
    'scissors': 'general', 'vase': 'glass', 'can': 'metal',
}

IMGSZ = 320

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

WIN = 'trash detector'
cv2.namedWindow(WIN, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(WIN, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, imgsz=IMGSZ, verbose=False)[0]

    for box in results.boxes:
        cls_name = model.names[int(box.cls[0])]
        if cls_name in EXCLUDE:
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0]) * 100
        trash_type = TRASH_MAP.get(cls_name, cls_name)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (140, 101, 104), 2)
        text = f'{trash_type} ({conf:.0f}%)'
        cv2.putText(frame, text, (x1, y1 - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (140, 101, 104), 2)

    cv2.imshow(WIN, frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
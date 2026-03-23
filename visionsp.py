import cv2
import pyttsx3
from ultralytics import YOLO
import threading
import time

# 1. Voice Function (Thread Safe)
def speak(text):
    local_engine = pyttsx3.init() 
    local_engine.say(text)
    local_engine.runAndWait()
    local_engine.stop()

# 2. AI Model Load
model = YOLO('yolov8n.pt') 

# 3. Camera Setup
cap = cv2.VideoCapture(0)
last_seen_time = 0

print("Assistant starts... Press 'q' to stop.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # AI Detection
    results = model(frame, conf=0.5, verbose=False)
    
    found_info = [] # Ikkada object name and distance rendu store chestham
    
    for r in results:
        for box in r.boxes:
            # Object Name
            c = int(box.cls)
            name = model.names[c]
            
            # --- DISTANCE ESTIMATION LOGIC ---
            # Box coordinates: x1, y1 (top-left), x2, y2 (bottom-right)
            x1, y1, x2, y2 = box.xyxy[0]
            pixel_width = x2 - x1 # Box entha vedalpu undo pixels lo
            
            # Thresholds (Ee numbers nee camera focal length batti adjust cheskovachu)
            if pixel_width > 350:
                distance = "Very Close"
            elif pixel_width > 150:
                distance = "Near"
            else:
                distance = "Far"
            
            found_info.append(f"{name} is {distance}")

    # 4. Voice Alert Logic
    current_time = time.time()
    if found_info and (current_time - last_seen_time > 4): # Gap 4 seconds ki pencha clear ga undadaniki
        # Unique alerts matrame pampali
        unique_alerts = list(set(found_info))
        speech_text = "I see " + ", and ".join(unique_alerts)
        
        # Background Thread Start
        t = threading.Thread(target=speak, args=(speech_text,))
        t.daemon = True
        t.start()
        
        last_seen_time = current_time

    # Screen Display (Optional: Box paina distance rayadam)
    annotated_frame = results[0].plot()
    cv2.imshow("AI Vision Assistant", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
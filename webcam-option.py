import cv2
from ultralytics import YOLO
import math
import time

# model stuff
model = YOLO("yolo-Weights/yolov8n.pt")
classID = 0 # ["person"] class label for YOLO

# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

person_counter = 0

# timer stuff 
# Timer setup
last_run_time = time.time()  # last execution time
interval = 20  # 20-second interval

while True:
    success, img = cap.read()
    
    
    current_time = time.time()
    if (current_time - last_run_time) >= interval:
        last_run_time = current_time
        
        results = model(img, stream=True, verbose=False)
        
        #person_count = sum(1 for box in results[0].boxes if int(box.cls[0]) == PERSON_CLASS_ID)
        
        #print(f"Number of persons detected: {person_count}")

        # coordinates
        for r in results:
            boxes = r.boxes

            for box in boxes:
                cls = int(box.cls[0])
                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values
                
                if cls == classID:
                    person_counter += 1
                    x1, y1, x2, y2 = map(int, box.xyxy[0])  # Convert to int values

                    # put box in cam
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                    # confidence
                    print("Person detected")
                    confidence = math.ceil((box.conf[0]*100))/100
                    print("Confidence --->",confidence)

                    # object details
                    org = [x1, y1]
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    fontScale = 1
                    color = (255, 0, 0)
                    thickness = 2
                    
                    label = f"Person {confidence:.2f}"
                    cv2.putText(img, label, org, font, fontScale, color, thickness)
            
            print("Total people in frame: ", person_counter)
            person_counter = 0 # reset counter


    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

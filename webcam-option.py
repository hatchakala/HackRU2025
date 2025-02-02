import cv2
from ultralytics import YOLO
import math
import time
import os

# model stuff
model = YOLO("yolo-Weights/yolov8n.pt")
classID = 0  # ["person"] class label for YOLO

# start webcam
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)

person_counter = 0
person_list = []
person_average = 0  # AVERAGE OF 1 MINUTE --> NEEDS TO BE SENT TO MONGODB

# timer stuff
# timer setup
last_run_time = time.time()  # last execution time
interval = 20  # 20-second interval


while True:
    # success, img = cap.read()

    os.system("rpicam-still --nopreview --output /dev/shm/test.jpg")

    img = cv2.imread("/dev/shm/test.jpg")

    current_time = time.time()
    if (current_time - last_run_time) >= interval:
        last_run_time = current_time  # update last run time
        results = model(img, stream=True, verbose=False)

        # coordinates
        for r in results:
            boxes = r.boxes

            for box in boxes:
                cls = int(box.cls[0])
                # # bounding box
                # x1, y1, x2, y2 = box.xyxy[0]
                # x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                if cls == classID:
                    person_counter += 1

                    # # put box in cam
                    # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                    # confidence
                    print("Person detected")
                    confidence = math.ceil((box.conf[0] * 100)) / 100
                    print("Confidence --->", confidence)

                    # # object details --> to show bounding box
                    # org = [x1, y1]
                    # font = cv2.FONT_HERSHEY_SIMPLEX
                    # fontScale = 1
                    # color = (255, 0, 0)
                    # thickness = 2

                    label = f"Person {confidence:.2f}"
                    # cv2.putText(img, label, org, font, fontScale, color, thickness)

            print("Total people in frame: ", person_counter)
            person_list.append(person_counter)
            person_counter = 0  # reset counter

        if len(person_list) == 3:  # 20 * 3 = 60 seconds (so after 1 minute has passed)
            print(person_list)
            person_average = math.ceil(
                sum(person_list) / len(person_list)
            )  # THIS is the data point that needs to be sent to MongoDB
            print(" (1-MINUTE) Average people in frame: ", person_average)
            person_list.clear()

    #cv2.imshow("Webcam", img)
    # if cv2.waitKey(1) == ord("q"):
    #     break

# cap.release()
# cv2.destroyAllWindows()

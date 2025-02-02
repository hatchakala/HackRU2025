import cv2
from ultralytics import YOLO
import math
import time
from picamera import PiCamera
from picamera.array import PiRGBArray


# --- Model Setup ---
model = YOLO("yolo-Weights/yolov8n.pt")
classID = 0  # Class label for "person" in YOLO

# --- PiCamera Setup ---
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32  # Adjust as needed
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)  # Allow the camera to warm up

# --- Counters and Timer Setup ---
person_counter = 0
person_list = []
person_average = 0  # This average (1 minute) could be sent to MongoDB

last_run_time = time.time()  # For tracking the interval execution
interval = 20  # seconds

# --- Main Loop ---
# Capture frames continuously from the PiCamera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    img = frame.array  # Obtain the image as a NumPy array
    current_time = time.time()

    # Run detection at defined intervals (every 20 seconds)
    if (current_time - last_run_time) >= interval:
        last_run_time = current_time  # Update the last run time
        results = model(img, stream=True, verbose=False)

        # Process each detection result
        for r in results:
            boxes = r.boxes

            for box in boxes:
                cls = int(box.cls[0])
                if cls == classID:
                    person_counter += 1
                    print("Person detected")
                    confidence = math.ceil(box.conf[0] * 100) / 100
                    print("Confidence --->", confidence)

            print("Total people in frame:", person_counter)
            person_list.append(person_counter)
            person_counter = 0  # Reset for the next frame

        # Every 1 minute (3 intervals of 20 seconds), calculate the average
        if len(person_list) == 3:
            print("Counts per interval:", person_list)
            person_average = math.ceil(sum(person_list) / len(person_list))
            print(" (1-MINUTE) Average people in frame:", person_average)
            # Here you can add your code to send 'person_average' to MongoDB
            person_list.clear()  # Reset the list for the next minute

    # Display the frame (optional)
    #cv2.imshow("PiCamera", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

    # Clear the stream for the next frame
    rawCapture.truncate(0)

# Clean up
cv2.destroyAllWindows()

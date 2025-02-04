import cv2
from ultralytics import YOLO
import math
import time
import audioop
import pyaudio
import numpy as np

from db import insert_lounge_data


def yap_meter(rms_average):
    if rms_average < 250:
        return 0
    elif rms_average < 450:
        return 1
    elif rms_average < 850:
        return 2
    else:
        return 3


# lounge id
lounge_id = 11
# yap level
yap_level = 0
# db stuff
db_list = []

# Model stuff
model = YOLO("yolo-Weights/yolov8n.pt")
classID = 0  # ["person"] class label for YOLO

# Webcam setup
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

person_counter = 0
person_list = []
person_average = 0  # AVERAGE OF 1 MINUTE --> NEEDS TO BE SENT TO MONGODB

# Timer setup
# last_run_time = time.time()  # last execution time
last_run_time = 0
interval = 20  # 20-second interval

# Audio setup
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2  # recording in stereo --> 2 channels --> left & right
RATE = 44100
RECORD_SECONDS = 10  # audio record for 10 seconds
WAIT_SECONDS = 10  # wait for 10 seconds after audio recording
FRAMES_PER_10_SEC = (RATE * RECORD_SECONDS) // CHUNK

rms_list = []
rms_average = 0  # AVERAGE OF 1 MINUTE --> NEEDS TO BE SENT TO MONGODB

# Initialize pyaudio
p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
)

while True:
    success, img = cap.read()

    # Webcam processing: person detection every 20 seconds
    current_time = time.time()
    buffer = 1  # had to add (plus or minus) buffer to hit intervals correctly (1 second time)
    print(str((current_time + buffer) - last_run_time))
    if (((current_time + buffer) - last_run_time) >= interval) or (last_run_time == 0):
        last_run_time = current_time  # update last run time
        results = model(img, stream=True, verbose=False)

        # coordinates
        for r in results:
            boxes = r.boxes

            for box in boxes:
                cls = int(box.cls[0])
                if cls == classID:
                    person_counter += 1
                    # print("Person detected")
                    confidence = math.ceil((box.conf[0] * 100)) / 100
                    # print("Confidence --->", confidence)

            print("Total people in frame: ", person_counter)
            person_list.append(person_counter)
            person_counter = 0  # reset counter

        # ?? amount of seconds have now passed

        if len(person_list) == 3:  # 20 * 3 = 60 seconds (so after 1 minute has passed)
            print(person_list)
            person_average = math.ceil(
                sum(person_list) / len(person_list)
            )  # THIS is the data point that needs to be sent to MongoDB
            print(" (1-MINUTE) Average people in frame: ", person_average)
            person_list.clear()

    # Audio processing: volume recording every 10 seconds
    print("Recording for 10 seconds...")
    frames = []

    # Record 10 seconds of audio
    for _ in range(FRAMES_PER_10_SEC):
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)

    # Process 10-second chunk
    full_data = b"".join(frames)
    samples = np.frombuffer(data, dtype=np.int16)  # raw data to numpy array
    rms_volume = audioop.rms(full_data, 2)  # root mean square

    print(
        "Average volume in last 10 seconds:", rms_volume
    )  # audioop.rms(fragment, width) --> width is number of channels
    rms_list.append(rms_volume)

    if len(rms_list) == 3:
        print(rms_list)
        rms_average = math.ceil(
            sum(rms_list) / len(rms_list)
        )  # THIS is the data point that needs to be sent to MongoDB
        print(" (1-MINUTE) Average volume: ", rms_average)
        rms_list.clear()
        # person detection is completed last, so this is when all MongoDB needs to be sent
        # MONGODB DATA SENDING
        yap_level = yap_meter(rms_average)
        print("1 MINUTE DATA TO SEND:")
        db_list = [lounge_id, person_average, yap_level]
        print(db_list)
        insert_lounge_data(lounge_id, person_average, yap_level) # MONGODB not working correctly for some reason

    # wait 20 seconds before recording again
    print("Waiting for 10 seconds before restarting...")
    time.sleep(WAIT_SECONDS)

    # exit on 'q' key press for webcam feed
    #cv2.imshow("Webcam", img)
    if cv2.waitKey(1) == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

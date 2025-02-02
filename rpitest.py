import cv2

gst_pipeline = "libcamerasrc ! video/x-raw, width=640, height=480, framerate=30/1 ! videoconvert ! appsink"
cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    ret, img = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
    else:
        cv2.imshow("Webcam", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

cap.release()

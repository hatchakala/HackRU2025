import cv2

cap = cv2.VideoCapture(1)

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

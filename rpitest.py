import cv2
import math
import time

# model stuff

# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)

while True:
    success, img = cap.read()

    print("Success: ", success)

    cv2.imshow("Webcam", img)

    #cv2.imshow("Webcam", img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

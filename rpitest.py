import cv2
import os

os.system("rpicam-still --nopreview --output test.jpg")

image = cv2.imread("test.jpg")

cv2.imshow("Image", image)
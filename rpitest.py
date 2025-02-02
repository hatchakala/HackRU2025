import cv2
import os

os.system("rpicam-still --nopreview --output test.jpg")

cv2.imshow("Image", cv2.imread("test.jpg"))
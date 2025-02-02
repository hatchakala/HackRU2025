import cv2
import os
import matplotlib.pyplot as plt

os.system("rpicam-jpeg --nopreview --timelapse 10 --output /dev/shm/image.jpg")

while not os.path.exists("/dev/shm/image.jpg"):
    pass

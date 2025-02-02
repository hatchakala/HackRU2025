import cv2
import os
import matplotlib.pyplot as plt

os.system("rpicam-still --timeout 30000 --timelapse 2000 -o /dev/shm/image%04d.jpg")

while not os.path.exists("/dev/shm/image%04d.jpg"):
    pass

while True:

    image = cv2.imread("/dev/shm/image%04d.jpg")

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Hide axes
    plt.show()


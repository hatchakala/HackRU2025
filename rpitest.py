import cv2
import os
import matplotlib.pyplot as plt

while True:
    os.system("rpicam-jpeg --nopreview --output /dev/shm/image.jpg")

    while not os.path.exists("/dev/shm/image.jpg"):
        pass

    image = cv2.imread("/dev/shm/image.jpg")

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Hide axes
    plt.show()


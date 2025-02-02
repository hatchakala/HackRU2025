import cv2
import os
import matplotlib.pyplot as plt

os.system("rpicam-jpeg --nopreview --timelapse 10 --output /dev/shm/capture/image.jpg")

# while not os.path.exists("/dev/shm/capture/image.jpg"):
image = cv2.imread("/dev/shm/capture/image.jpg")

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')  # Hide axes
plt.show()


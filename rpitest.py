from picamera import PiCamera
import time

camera = PiCamera()
camera.start_preview()  # Optional: displays a preview on the screen
time.sleep(2)  # Give the camera time to adjust
camera.capture('/home/pi/Pictures/image.jpg')
camera.stop_preview()  # Optional: stops the preview
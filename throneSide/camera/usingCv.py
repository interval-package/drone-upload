import cv2
import picamera
# import numpy
import time
from picamera.array import PiRGBArray

# init the cam
camera = picamera.PiCamera()
camera.resolution = (640,480)
camera.framerate = 20
# camera.hflip = True
# camera.vflip = True
rawCapture = PiRGBArray(camera, size = (640,480))

time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
import sys

import cv2 as cv
from ultralytics import YOLO

# Load a model
model = YOLO("models/v3/best.pt")  # pretrained YOLO11n model

img = cv.imread(cv.samples.findFile("dataoutput/img.png"))

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("starry_night.png", img)

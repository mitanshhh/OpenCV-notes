import cv2 as cv
import matplotlib.pyplot as plt

vid = r"Media\car_race.mp4"

source = cv.VideoCapture(vid)

if not source.isOpened():
    print("Error opening video or file")
    exit()

ret , frame = source.read()

plt.imshow(frame[...,::-1])
plt.show()

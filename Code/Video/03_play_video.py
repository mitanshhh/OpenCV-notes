import cv2 as cv
import matplotlib.pyplot as plt

vid = r"Media\car_race.mp4"

source = cv.VideoCapture(vid)

if not source.isOpened():
    print("Error opening video or file")
    exit()
while True:
    ret , frame = source.read()

    if not ret:
        break

    cv.imshow("Playing Video",frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

# Release video and close window
source.release()
cv.destroyAllWindows()
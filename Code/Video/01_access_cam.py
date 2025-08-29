import sys
import cv2

s = 0
#IF MORE THAN 1 SOURCE
# if len(sys.argv) > 1:
#     arg = sys.argv[1]
#     if arg.isdigit():
#         s = int(arg)
#     else:
#         s = arg

source = cv2.VideoCapture(s)
if not source.isOpened():
    print("Cannot open camera or video")
    exit()

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while True:
    has_frame, frame = source.read()
    if not has_frame:
        break
    
    cv2.imshow(win_name, frame)
    if cv2.waitKey(1) == 27:  # ESC
        break

source.release()
cv2.destroyAllWindows()

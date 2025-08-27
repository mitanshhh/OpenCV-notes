import cv2 as cv
import matplotlib.pyplot as plt

cb_img = cv.imread(r"Media\checkboard_84x84.jpg",0)
print(cb_img)

#IMAGE DETAILS
print("Image size: ",cb_img.size)
print("Image type: ",cb_img.dtype)

cv.imshow("Original",cb_img)
cv.waitKey(0)
cv.destroyAllWindows()

plt.imshow(cb_img) #diff colour
plt.show()
plt.imshow(cb_img,cmap="gray") #same colour


#BIGGER CHESS BOARD WITH MORE COLOURS
cb_fuzzy_img = cv.imread(r"Media\fuzzy_cb.png",1)
print(cb_fuzzy_img)

plt.imshow(cb_fuzzy_img,cmap="gray")
plt.show()

#IMSHOW WITH LOOP
w4 = cv.namedWindow("w4")
while True:
    cv.imshow(w4,cb_img)
    keypress = cv.waitKey(1)
    if keypress == ord('q'):
        break
cv.destroyAllWindows()

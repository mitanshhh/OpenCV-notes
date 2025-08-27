import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread(r"Media\rose.jpg")
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

h,s,v = cv.split(image_hsv)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h,cmap="gray");plt.title("H Channel")
plt.subplot(142);plt.imshow(s,cmap="gray");plt.title("S Channel")
plt.subplot(143);plt.imshow(v,cmap="gray");plt.title("V Channel")
plt.subplot(144);plt.imshow(image_rgb,cmap="gray");plt.title("Original Image")

plt.show()
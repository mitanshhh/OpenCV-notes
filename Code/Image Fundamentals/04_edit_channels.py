import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread(r"Media\rose.jpg")
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

h,s,v = cv.split(image_hsv)
h_new = h+20 #ADD 20 HUE

#MERGE INTO A NEW IMAGE 
image_new_hsv = cv.merge((h_new,s,v))
image_new_hsv_to_rgb = cv.cvtColor(image_new_hsv, cv.COLOR_HSV2RGB) #CONVERT IT BACK TO RGB

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h,cmap="gray");plt.title("H Channel")
plt.subplot(142);plt.imshow(s,cmap="gray");plt.title("S Channel")
plt.subplot(143);plt.imshow(v,cmap="gray");plt.title("V Channel")
plt.subplot(144);plt.imshow(image_new_hsv_to_rgb,cmap="gray");plt.title("NEW HSV Image")
plt.show()
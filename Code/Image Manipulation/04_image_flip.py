import matplotlib.pyplot as plt
import cv2 as cv

image = cv.imread(r"Media\rose.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

image_hf = cv.flip(image,1)
image_vf = cv.flip(image,0)
image_hvf = cv.flip(image,-1)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(image,cmap="gray");plt.title("Original Image")
plt.subplot(142);plt.imshow(image_hf,cmap="gray");plt.title("Horizonta Flip Image")
plt.subplot(143);plt.imshow(image_vf,cmap="gray");plt.title("Vertical Flip Image")
plt.subplot(144);plt.imshow(image_hvf,cmap="gray");plt.title("Both H&V Image")
plt.show()
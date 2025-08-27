import matplotlib.pyplot as plt
import cv2 as cv

image = cv.imread(r"Media\rose.jpg")
image_to_rgb = cv.cvtColor(image,cv.COLOR_BGR2RGB)

cropped_rose = image_to_rgb[1000:3200,1200:4200]

plt.subplot(121);plt.imshow(image_to_rgb,cmap="gray");plt.title("Original Image")
plt.subplot(122);plt.imshow(cropped_rose,cmap="gray");plt.title("Cropped Image")
plt.show()
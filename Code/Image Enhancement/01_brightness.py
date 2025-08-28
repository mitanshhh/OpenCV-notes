import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

image = cv.imread(r"Media\rose.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

matrix = np.ones(image.shape, dtype="uint8") * 50

image_bright = cv.add(image, matrix) 
image_dark = cv.subtract(image, matrix) 

plt.figure(figsize=[20,5])
plt.subplot(131);plt.imshow(image_bright);plt.title("Bright Image")
plt.subplot(132);plt.imshow(image);plt.title("Original Image")
plt.subplot(133);plt.imshow(image_dark);plt.title("Dark Image")
plt.show()
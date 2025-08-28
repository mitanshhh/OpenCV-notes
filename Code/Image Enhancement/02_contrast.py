import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

image = cv.imread(r"Media\rose.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

matrix1 = np.ones(image.shape, dtype="uint8") * 0.8
matrix2 = np.ones(image.shape, dtype="uint8") * 1.2

image_lower_contrast = np.uint8(cv.multiply(np.float64(image),matrix1))
image_higher_contrast = np.uint8(np.clip(cv.multiply(np.float64(image),matrix2),0,255))

plt.figure(figsize=[20,5])
plt.subplot(131);plt.imshow(image_higher_contrast);plt.title("High contrast Image")
plt.subplot(132);plt.imshow(image);plt.title("Original Image")
plt.subplot(133);plt.imshow(image_lower_contrast);plt.title("Low contrast Image")
plt.show()
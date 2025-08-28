import cv2 as cv
import matplotlib.pyplot as plt

img_read = cv.imread(r"Media\construction.png", cv.IMREAD_GRAYSCALE)
plt.imshow(img_read,cmap="gray")
img_read = img_read[50:400, 0:600]

retval, img_thresh = cv.threshold(img_read, 100, 255, cv.THRESH_BINARY)

# Show the images
plt.figure(figsize=[18, 5])

plt.subplot(121);plt.imshow(img_read, cmap="gray");  plt.title("Original")
plt.subplot(122);plt.imshow(img_thresh, cmap="gray");plt.title("Thresholded")
plt.show()

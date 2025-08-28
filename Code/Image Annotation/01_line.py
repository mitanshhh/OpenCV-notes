import matplotlib.pyplot as plt
import cv2 as cv

image = cv.imread(r"Media\pslv.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image_copy = image.copy()
# plt.imshow(image,cmap="gray")


line_on_image = cv.line(image_copy,(25,50),(25,150),color=(255,0,0),thickness=4,lineType=cv.LINE_AA)

#PLOTTING IMAGES
plt.subplot(121);plt.imshow(image,cmap="gray");plt.title("Original Image")
plt.subplot(122);plt.imshow(line_on_image,cmap="gray");plt.title("Line on Image")
plt.show()


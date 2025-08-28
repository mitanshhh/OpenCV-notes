import matplotlib.pyplot as plt
import cv2 as cv

image = cv.imread(r"Media\pslv.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image_copy = image.copy()
# plt.imshow(image,cmap="gray")


circle_on_image = cv.circle(image_copy,(150,150),55,color=(255,0,0),thickness=1,lineType=cv.LINE_AA)

#PLOTTING IMAGES
plt.subplot(121);plt.imshow(image,cmap="gray");plt.title("Original Image")
plt.subplot(122);plt.imshow(circle_on_image,cmap="gray");plt.title("Circle on Image")
plt.show()
import matplotlib.pyplot as plt
import cv2 as cv

image = cv.imread(r"Media\pslv.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image_copy = image.copy()
# plt.imshow(image,cmap="gray")


rect_on_image = cv.rectangle(image_copy,(10,50),(170,100),color=(255,0,0),thickness=1,lineType=cv.LINE_AA)

#PLOTTING IMAGES
plt.subplot(121);plt.imshow(image,cmap="gray");plt.title("Original Image")
plt.subplot(122);plt.imshow(rect_on_image,cmap="gray");plt.title("Rectangle on Image")
plt.show()
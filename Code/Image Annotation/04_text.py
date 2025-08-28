import matplotlib.pyplot as plt
import cv2 as cv

image = cv.imread(r"Media\pslv.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image_copy = image.copy()
# plt.imshow(image,cmap="gray")

#DEFINE PARAMS
text = "Mission Mangalyaan"
fontScale = 0.1
fontFace = cv.FONT_HERSHEY_COMPLEX_SMALL

text_on_image = cv.putText(image_copy,text,(10,15),fontFace,fontScale,color=(0,0,0),thickness=1)

plt.subplot(121);plt.imshow(image,cmap="gray");plt.title("Original Image")
plt.subplot(122);plt.imshow(text_on_image,cmap="gray");plt.title("Text on Image")
plt.show()
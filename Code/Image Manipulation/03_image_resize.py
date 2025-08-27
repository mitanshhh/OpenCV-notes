import matplotlib.pyplot as plt
import cv2 as cv

image = cv.imread(r"Media\rose.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

#RESIZED USING fx fy
image_2x = cv.resize(image,None,fx=2,fy=2)

#RESIZED USING HEIGHT WIDTH
height = 200
width = 350
dim = (height,width)
image_resized = cv.resize(image,dsize=dim,interpolation=cv.INTER_AREA)

plt.figure(figsize=[20,5])
plt.subplot(131);plt.imshow(image,cmap="gray");plt.title("Original Image")
plt.subplot(132);plt.imshow(image_2x,cmap="gray");plt.title("Double Image")
plt.subplot(133);plt.imshow(image_resized,cmap="gray");plt.title("200x350 Image")
plt.show()
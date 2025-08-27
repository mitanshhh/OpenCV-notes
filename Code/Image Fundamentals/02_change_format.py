import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread(r"Media\rose.jpg")   
# cv.imshow('Grayscale Image', img1) SHOW ORIGINAL IMAGE
img2 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)


#SAVING GRAY IMAGE
cv.imwrite(r"Media\rose_formatted.png", img2)
# cv.waitKey(0)
# cv.destroyAllWindows()

plt.imshow(img1,cmap="gray")
plt.show()
plt.imshow(img2,cmap="gray")
plt.show()
import matplotlib.pyplot as plt
import cv2 as cv


img = cv.imread(r"Media\fuzzy_cb_formatted.jpg",0)
print(img)

cb_img_copy = img.copy()
cb_img_copy [2,2] = 200
cb_img_copy [2,3] = 200
cb_img_copy [3,2] = 200
cb_img_copy [3,3] = 200

plt.figure(figsize=[20,5])
plt.subplot(121);plt.imshow(img,cmap="gray");plt.title("Original Image")
plt.subplot(122);plt.imshow(cb_img_copy,cmap="gray");plt.title("Pixels Manipulated Image")
plt.show()
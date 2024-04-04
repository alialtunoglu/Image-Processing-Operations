import cv2
import matplotlib.pyplot as plt

# resmi içe aktar
img = cv2.imread("img1.jpg")

# burada anlatmak istediğim cv2 normal renklerini gösterir çağırdığımızda
# plt ise bgr olarak gösterir rgb olarak göstermesi için bgr2rgb yazmamız gerekir
cv2.imshow("winname", img)

print(img.shape) #1280*800 neredeyse 

plt.figure()
plt.imshow(img)
plt.show()

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")
plt.show()


# eşikleme
_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY)


plt.figure()
plt.imshow(thresh_img, cmap = "gray")
plt.axis("off")
plt.show()

# uyarlamalı eşik değeri
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,8)
plt.figure()
plt.imshow(thresh_img2, cmap = "gray")
plt.axis("off")
plt.show()


























import cv2
import matplotlib.pyplot as plt

img = cv2.imread("lenna.jpeg", 0)

# Gauss ile bulanıklaştır
blur = cv2.GaussianBlur(img, (5,5), 1)

# Keskinleştirme
sharp = cv2.addWeighted(img, 2.5, blur, -1.5, 0)

plt.figure(figsize=(12,4))
plt.subplot(1,3,1), plt.imshow(img, cmap='gray'), plt.title("Orijinal")
plt.subplot(1,3,2), plt.imshow(blur, cmap='gray'), plt.title("Bulanık")
plt.subplot(1,3,3), plt.imshow(sharp, cmap='gray'), plt.title("Keskinleştirilmiş")
plt.show()



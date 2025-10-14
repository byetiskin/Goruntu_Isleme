import cv2
import matplotlib.pyplot as plt

img = cv2.imread("lenna.jpeg", 0)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)

plt.figure(figsize=(12,8))
plt.subplot(1,2,1), plt.imshow(img, cmap='gray'), plt.title("Orijinal")
plt.subplot(1,2,2), plt.imshow(sobelx, cmap='gray'), plt.title("Sobel X (1B Türev)")
plt.show()
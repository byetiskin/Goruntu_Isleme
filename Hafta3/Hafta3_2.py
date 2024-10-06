import cv2
import matplotlib.pyplot as plt

# İki görüntüyü oku (Gri tonlamalı küçük test görüntüleri)
image1 = cv2.imread('cicek.jpg', 0)
image2 = cv2.imread('gunes.jpg', 0)

# Görüntülerin boyutlarını eşitle (resize işlemi)
image2_resized = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Toplama işlemi
added_image = cv2.add(image1, image2_resized)

# Çıkarma işlemi
subtracted_image = cv2.subtract(image1, image2_resized)

# Alpha blending
alpha = 0.7
blended_image = cv2.addWeighted(image1, alpha, image2_resized, 1-alpha, 0)

# Görüntüleri ekrana bas
plt.figure(figsize=(20, 15))

plt.subplot(2, 3, 1)
plt.imshow(image1, cmap='gray')
plt.title('Gri Çiçek Resmi')

plt.subplot(2, 3, 2)
plt.imshow(image2, cmap='gray')
plt.title('Gri Güneş Resmi')

plt.subplot(2, 3, 3)
plt.imshow(image2_resized, cmap='gray')
plt.title('Gri Güneş Resmi Boyutlandırılmış')

plt.subplot(2, 3, 4)
plt.imshow(added_image, cmap='gray')
plt.title('Toplama')

plt.subplot(2, 3, 5)
plt.imshow(subtracted_image, cmap='gray')
plt.title('Çıkarma')

plt.subplot(2, 3, 6)
plt.imshow(blended_image, cmap='gray')
plt.title('Alpha Blending')

plt.show()

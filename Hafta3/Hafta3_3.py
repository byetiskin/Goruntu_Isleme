import cv2
import matplotlib.pyplot as plt

# Görüntüyü oku (Renkli olarak)
image = cv2.imread('cicek.jpg', cv2.IMREAD_COLOR)

# Piksel çoğullama (yakınlaştırma - 4 kat)
resized_pixel_replicate = cv2.resize(image, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)

# En yakın komşu algoritmasıyla yeniden boyutlandırma (yakınlaştırma - 2 kat)
resized_nearest = cv2.resize(image, (0, 0), fx=2, fy=2, interpolation=cv2.INTER_NEAREST)

# Bilinear interpolasyonla yeniden boyutlandırma (yakınlaştırma - 2 kat)
resized_bilinear = cv2.resize(image, (0, 0), fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

# Bicubic interpolasyonla yeniden boyutlandırma (yakınlaştırma - 2 kat)
resized_bicubic = cv2.resize(image, (0, 0), fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Sonuçları matplotlib ile ekrana bas
plt.figure(figsize=(12, 8))

# Orijinal görüntü
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Orijinal Görüntü')

# Piksel çoğullama ile yeniden boyutlandırma
plt.subplot(2, 3, 2)
plt.imshow(cv2.cvtColor(resized_pixel_replicate, cv2.COLOR_BGR2RGB))
plt.title('Piksel Çoğullama (4x)')

# En yakın komşu algoritması
plt.subplot(2, 3, 3)
plt.imshow(cv2.cvtColor(resized_nearest, cv2.COLOR_BGR2RGB))
plt.title('En Yakın Komşu (2x)')

# Bilinear interpolasyon
plt.subplot(2, 3, 4)
plt.imshow(cv2.cvtColor(resized_bilinear, cv2.COLOR_BGR2RGB))
plt.title('Bilinear Interpolasyon (2x)')

# Bicubic interpolasyon
plt.subplot(2, 3, 5)
plt.imshow(cv2.cvtColor(resized_bicubic, cv2.COLOR_BGR2RGB))
plt.title('Bicubic Interpolasyon (2x)')

# Görüntüleri göster
plt.show()

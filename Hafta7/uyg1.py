import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü yükle ve griye çevir
img = cv2.imread('fruit.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (128, 128))

# 1. NOKTASAL DÖNÜŞÜM: Parlaklık ve kontrast ayarı (hazır fonksiyonsuz)
a = 1.3   # kontrast katsayısı
b = 40    # parlaklık değeri
transformed = np.zeros_like(img)

rows, cols = img.shape
for i in range(rows):
    for j in range(cols):
        val = a * img[i, j] + b
        if val > 255:
            val = 255
        elif val < 0:
            val = 0
        transformed[i, j] = val

# 2. K-MEANS SEGMENTASYON (hazır fonksiyonsuz)
pixels = transformed.reshape(-1, 1)
K = 2
centers = np.array([50, 200], dtype=np.float32)

for _ in range(10):
    distances = np.abs(pixels - centers.reshape(1, K))
    labels = np.argmin(distances, axis=1)
    for k in range(K):
        if np.any(labels == k):
            centers[k] = np.mean(pixels[labels == k])

segmented = centers[labels].reshape(img.shape).astype(np.uint8)

# Görselleri göster
plt.figure(figsize=(10,5))
plt.subplot(1,3,1); plt.imshow(img, cmap='gray'); plt.title("Orijinal")
plt.subplot(1,3,2); plt.imshow(transformed, cmap='gray'); plt.title("Noktasal Dönüşüm (a*r+b)")
plt.subplot(1,3,3); plt.imshow(segmented, cmap='gray'); plt.title("Segmentasyon Sonucu")
plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lenna.jpeg')

if img is None:
    raise FileNotFoundError("Lütfen 'lenna.jpeg' dosyasını bu dosya ile aynı klasöre ekleyin.")

# Gürültü ekleme (Salt & Pepper Noise)
noisy = img.copy()
rows, cols, _ = noisy.shape

# Rastgele 3000 pikseli beyaz (tuz)
for i in range(3000):
    x, y = np.random.randint(0, rows), np.random.randint(0, cols)
    noisy[x, y] = [255, 255, 255]

# Rastgele 3000 pikseli siyah (biber)
for i in range(3000):
    x, y = np.random.randint(0, rows), np.random.randint(0, cols)
    noisy[x, y] = [0, 0, 0]

# Median filtre, her 5x5 penceredeki ortanca değeri alır.
median = cv2.medianBlur(noisy, 5)

plt.figure(figsize=(12,5))

plt.subplot(1,3,1)
plt.title("Orijinal Görüntü")
plt.imshow(img)
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Gürültülü (Salt & Pepper)")
plt.imshow(noisy)
plt.axis('off')

plt.subplot(1,3,3)
plt.title("Median Filtre Sonucu")
plt.imshow(median)
plt.axis('off')

plt.tight_layout()
plt.show()

# Median filtre:
#   - Doğrusal olmayan bir filtredir.
#   - Komşuluk penceresindeki ortanca değeri alır.
#   - Tuz-biber (salt-pepper) gürültüsünü etkili biçimde temizler.
#   - Uç değerlerin (çok parlak veya çok koyu piksellerin) etkisini azaltır.

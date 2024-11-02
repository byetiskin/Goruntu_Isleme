import cv2
import numpy as np
import matplotlib.pyplot as plt

def compute_1d_derivative(image):
    # Görüntü boyutlarını al
    height, width = image.shape
    
    # Türev görüntüsü için boş bir dizi oluştur
    derivative_image = np.zeros((height, width), dtype=np.float32)
    
    # Merkezi fark maskesi
    mask = np.array([-1, 0, 1])
    
    # Görüntü üzerinde türev hesapla
    for y in range(height):
        for x in range(1, width - 1):  # Sınırları aşmamak için 1'den width - 1'e kadar
            derivative_image[y, x] = (mask[0] * image[y, x - 1] +
                                      mask[1] * image[y, x] +
                                      mask[2] * image[y, x + 1])
    
    # Türevi daha iyi görebilmek için değerleri normalize et
    derivative_image = cv2.normalize(derivative_image, None, 0, 255, cv2.NORM_MINMAX)
    derivative_image = np.uint8(derivative_image)
    
    return derivative_image

# Orijinal görüntüyü yükleyin (gri tonlamalı)
image = cv2.imread('biber.jpg', cv2.IMREAD_GRAYSCALE)

# 1D türevi hesaplayın
derivative_image = compute_1d_derivative(image)

# Sonuçları görselleştirin
plt.figure(figsize=(12, 6))

# Orijinal görüntü
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Orijinal Görüntü')
plt.axis('off')

# Türev Sonucu
plt.subplot(1, 2, 2)
plt.imshow(derivative_image, cmap='gray')
plt.title('1D Yatay Türev (Merkezi Fark)')
plt.axis('off')

plt.show()

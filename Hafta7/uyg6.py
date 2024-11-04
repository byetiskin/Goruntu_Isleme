import cv2
import numpy as np
import matplotlib.pyplot as plt

def compute_directional_derivative(image, angle):    
    # Açıyı radyana çevir
    theta = np.deg2rad(angle)
    
    # Yatay ve dikey türevleri hesapla
    dx = compute_1d_derivative(image, axis='x')
    dy = compute_1d_derivative(image, axis='y')
    
    # Yönsel türev formülünü uygula: D_theta = cos(theta) * dx + sin(theta) * dy
    directional_derivative = np.cos(theta) * dx + np.sin(theta) * dy
    
    # Yönsel türevi daha iyi görebilmek için normalize et
    directional_derivative = cv2.normalize(directional_derivative, None, 0, 255, cv2.NORM_MINMAX)
    return np.uint8(directional_derivative)

def compute_1d_derivative(image, axis='x'):
    height, width = image.shape
    derivative_image = np.zeros((height, width), dtype=np.float32)
    mask = np.array([-1, 0, 1])
    
    if axis == 'x':
        for y in range(height):
            for x in range(1, width - 1):
                derivative_image[y, x] = (mask[0] * image[y, x - 1] +
                                          mask[1] * image[y, x] +
                                          mask[2] * image[y, x + 1])
    elif axis == 'y':
        for y in range(1, height - 1):
            for x in range(width):
                derivative_image[y, x] = (mask[0] * image[y - 1, x] +
                                          mask[1] * image[y, x] +
                                          mask[2] * image[y + 1, x])

    derivative_image = cv2.normalize(derivative_image, None, 0, 255, cv2.NORM_MINMAX)
    return np.uint8(derivative_image)

# Orijinal görüntüyü yükleyin (gri tonlamalı)
image = cv2.imread('biber.jpg', cv2.IMREAD_GRAYSCALE)

# Örneğin 45 derece yönünde yönsel türev hesaplayın
angle = 45
directional_derivative = compute_directional_derivative(image, angle)

# Sonuçları görselleştirin
plt.figure(figsize=(12, 6))

# Orijinal görüntü
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Orijinal Görüntü')
plt.axis('off')

# Yönsel Türev Sonucu
plt.subplot(1, 2, 2)
plt.imshow(directional_derivative, cmap='gray')
plt.title(f'Yönsel Türev (Açı: {angle}°)')
plt.axis('off')

plt.show()

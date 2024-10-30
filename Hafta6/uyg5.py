import cv2
import numpy as np

def adjust_gamma(image, gamma):
    """
    Gamma ayarlama fonksiyonu.
    gamma: Gamma değeri
           - gamma > 1.0 görüntüyü aydınlatır (gamma artırma)
           - 0 < gamma < 1.0 görüntüyü karartır (gamma azaltma)
    """
    # Yeni bir görüntü oluştur (aynı boyutlarda ve aynı veri türünde)
    height, width, channels = image.shape
    adjusted_gamma = np.zeros((height, width, channels), dtype=np.uint8)
    
    # Her piksel üzerinde gamma işlemini uygula
    for r in range(height):
        for c in range(width):
            for k in range(channels):
                # Slayttaki formülü uygula: J(r, c) = 255 * [(I(r, c) / 255)^(1/gamma)]
                normalized_pixel = image[r, c, k] / 255.0
                adjusted_pixel = 255 * (normalized_pixel ** (1 / gamma))
                adjusted_gamma[r, c, k] = int(adjusted_pixel)
    
    return adjusted_gamma

# Örnek kullanım
image = cv2.imread('kus_kucuk.jpg')  # Görüntüyü yükle

# Gamma ayarı yapılmış görüntüleri oluştur
increased_gamma_image = adjust_gamma(image, gamma=1.5)  # Gamma artırma
decreased_gamma_image = adjust_gamma(image, gamma=0.5)  # Gamma azaltma

# Sonuçları göster
cv2.imshow('Original', image)
cv2.imshow('Increased Gamma', increased_gamma_image)
cv2.imshow('Decreased Gamma', decreased_gamma_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

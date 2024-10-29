import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('kus_kucuk.jpg')

def adjust_contrast(image, a):
    """    
    Kontrast ayarlama fonksiyonu.
    a: kontrast çarpanı
           - a > 1.0 kontrastı artırır
           - 0 < a < 1.0 kontrastı azaltır
    """
    # Yeni bir görüntü oluştur (aynı boyutlarda ve aynı veri türünde)
    height, width, channels = image.shape
    adjusted_contrast = np.zeros((height, width, channels), dtype=np.uint8)
    
    # Her piksel üzerinde kontrast artırma işlemini uygula
    for r in range(height):
        for c in range(width):
            for k in range(channels):
                # Slayttaki formülü uygula: T = a * (I - 127) + 127
                T = a * (image[r, c, k] - 127) + 127
                # Sonuçları sınırla (0-255 arası)
                if T < 0:
                    adjusted_contrast[r, c, k] = 0
                elif T > 255:
                    adjusted_contrast[r, c, k] = 255
                else:
                    adjusted_contrast[r, c, k] = int(T)
    
    return adjusted_contrast


# Kontrastı artırılmış ve azaltılmış görüntüleri oluştur
increased_contrast_image = adjust_contrast(image, a=1.5)  # Kontrast artırma
decreased_contrast_image = adjust_contrast(image, a=0.5)  # Kontrast azaltma

# Sonuçları göster
cv2.imshow('Original', image)
cv2.imshow('Increased Contrast', increased_contrast_image)
cv2.imshow('Decreased Contrast', decreased_contrast_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

# Görüntüyü yükle (renkli olarak)
image = cv2.imread('kus_kucuk.jpg')

# Parlaklık artırma fonksiyonu
def increase_brightness(image, g=50):
    # Yeni bir görüntü oluştur (aynı boyutlarda ve aynı veri türünde)
    brightened = np.zeros_like(image, dtype=np.uint8)
    
    # Her piksel ve her renk kanalı için parlaklığı artır
    for r in range(image.shape[0]):  # satırlar
        for c in range(image.shape[1]):  # sütunlar
            for k in range(3):  # renk kanalları (BGR)
                # Formüle göre parlaklığı artır (sınırlandırma ile)
                new_value = image[r, c, k] + g
                brightened[r, c, k] = min(new_value, 255)  # 255'i aşmaması için sınır koyuyoruz
                
    return brightened

# Parlaklık azaltma fonksiyonu
def decrease_brightness(image, g=50):
    # Yeni bir görüntü oluştur (aynı boyutlarda ve aynı veri türünde)
    darkened = np.zeros_like(image, dtype=np.uint8)
    
    # Her piksel ve her renk kanalı için parlaklığı azalt
    for r in range(image.shape[0]):  # satırlar
        for c in range(image.shape[1]):  # sütunlar
            for k in range(3):  # renk kanalları (BGR)
                # Formüle göre parlaklığı azalt (sınırlandırma ile)
                new_value = image[r, c, k] - g
                darkened[r, c, k] = max(new_value, 0)  # 0'ın altına düşmemesi için sınır koyuyoruz
                
    return darkened

# Parlaklık artırılmış ve azaltılmış görüntüleri oluştur
bright_image = increase_brightness(image, g=50)
dark_image = decrease_brightness(image, g=50)

# Görüntüleri göster
cv2.imshow('Original', image)
cv2.imshow('Brightened', bright_image)
cv2.imshow('Darkened', dark_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

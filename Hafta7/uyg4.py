import cv2
import numpy as np
import matplotlib.pyplot as plt

def template_matching_ncc(image, template):
    # Görüntü ve şablon boyutlarını al
    img_height, img_width, _ = image.shape
    template_height, template_width, _ = template.shape
    
    # En yüksek NCC skorunu ve en iyi eşleşen koordinatları takip et
    max_score = -float('inf')
    best_match = (0, 0)
    
    # Şablonu görüntü üzerinde kaydırarak her noktada korelasyonu skorunu hesapla
    for y in range(img_height - template_height + 1):
        for x in range(img_width - template_width + 1):
            score = 0
            for c in range(3):  # RGB kanalları için
                # Şablonun yerleştirileceği görüntüdeki bölgeyi al
                region = image[y:y + template_height, x:x + template_width, c]
                template_channel = template[:, :, c]
                
                # Görüntü bölgesi ve şablonun her kanalını normalize et
                region_mean = np.mean(region)
                template_mean = np.mean(template_channel)
                
                # Korelasyon hesaplama: (region - mean(region)) * (template - mean(template))
                numerator = np.sum((region - region_mean) * (template_channel - template_mean))
                
                # Normalizasyon için payda
                denominator = np.sqrt(np.sum((region - region_mean) ** 2) * np.sum((template_channel - template_mean) ** 2))
                
                # Sıfıra bölmeyi önlemek için kontrol
                if denominator != 0:
                    score += numerator / denominator
            
            # Eğer yeni bir en yüksek korelasyon skoru bulduysak, kaydet
            if score > max_score:
                max_score = score
                best_match = (y, x)
    
    return best_match

# Orijinal RGB görüntü ve şablonu yükleyin
image = cv2.imread('resim.png')
template = cv2.imread('sablon.png')

# Şablon eşleştirmeyi gerçekleştirin
best_y, best_x = template_matching_ncc(image, template)

# Sonuçları görselleştirin
plt.figure(figsize=(10, 6))

# Orijinal görüntü
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Orijinal RGB Görüntü')
plt.axis('off')

# Şablonun bulunduğu bölgeyi daha belirgin hale getirmek için kalın bir dikdörtgen çiz
image_with_rectangle = image.copy()

# Dış kalın çizgi (kalınlığı daha fazla belirgin hale getirmek için)
cv2.rectangle(image_with_rectangle, (best_x, best_y), 
              (best_x + template.shape[1], best_y + template.shape[0]), 
              (0, 255, 0), 5)  # 5 piksel kalınlık

# İç çizgi (daha belirgin hale getirmek için)
cv2.rectangle(image_with_rectangle, (best_x + 2, best_y + 2), 
              (best_x + template.shape[1] - 2, best_y + template.shape[0] - 2), 
              (255, 0, 0), 2)  # 2 piksel kalınlık

# Eşleşme Sonucu
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(image_with_rectangle, cv2.COLOR_BGR2RGB))
plt.title('Şablon Eşleşme Sonucu (NCC)')
plt.axis('off')

plt.show()

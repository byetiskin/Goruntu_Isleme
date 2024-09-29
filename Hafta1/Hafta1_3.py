# Gerekli kütüphaneleri içe aktarıyoruz
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Görüntü dosyasının yolunu belirtin 
image_path1 = 'C:/Users/Dell/Downloads/Asistanlık/Dersler/Görüntü İşleme/Uygulamalar-Yeni/kelebek.jpeg'
image_path2 = 'C:/Users/Dell/Downloads/Asistanlık/Dersler/Görüntü İşleme/Uygulamalar-Yeni/deniz.jpg'

# Görüntüleri açıyoruz
image1 = Image.open(image_path1)
image2 = Image.open(image_path2)

# Görüntüleri NumPy dizisine (matrisine) çeviriyoruz
fx1 = np.array(image1)
fx2 = np.array(image2)

# Görüntüleri ekranda gösteriyoruz
plt.subplot(1, 2, 1)
plt.imshow(fx1)
plt.title('Kelebek Orijinal Görüntüsü')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(fx2)
plt.title('Deniz Orijinal Görüntüsü')
plt.axis('off')
plt.show()

# Fonksiyon
def H(a):
    return 2 * a

# 1. Durum: Her iki görüntüyü ayrı ayrı fonksiyona sokup sonra toplama
result_1 = H(fx1) + H(fx2)

# 2. Durum: Görüntüleri toplayıp sonra fonksiyona sokma
result_2 = H(fx1 + fx2)

# Sonuçları görselleştirme
plt.figure(figsize=(10, 5))

# İlk sonucu göster
plt.subplot(1, 2, 1)
plt.imshow(result_1)
plt.title('H(fx1) + H(fx2)')
plt.axis('off')

# İkinci sonucu göster
plt.subplot(1, 2, 2)
plt.imshow(result_2)
plt.title('H(fx1 + fx2)')
plt.axis('off')
plt.show()

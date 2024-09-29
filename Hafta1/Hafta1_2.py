# Gerekli kütüphaneleri içe aktarıyoruz
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Görüntü dosyasının yolunu belirtin (dosya adı veya tam yol olabilir)
image_path = 'C:/Users/Dell/Downloads/Asistanlık/Dersler/Görüntü İşleme/Uygulamalar-Yeni/kelebek.jpeg'

# Görüntüyü açıyoruz
image = Image.open(image_path)

# Görüntüyü NumPy dizisine (matrisine) çeviriyoruz
image_matrix = np.array(image)

# Görüntüyü vektöre dönüştürüyoruz
# flatten() tüm matrisi tek boyutlu bir diziye (vektör) çevirir
image_vector = image_matrix.flatten()

# Matrisin ve vektörün boyutlarını yazdırıyoruz
print("Matris Boyutları: ", image_matrix.shape)
print("Vektör Boyutu: ", image_vector.shape)
print("Vektörün İlk 10 Elemanı: ", image_vector[:10])

plt.imshow(image_matrix)
plt.title('Orijinal Görüntü')
plt.axis('off')  # Eksenleri gizliyoruz
plt.show()

# RGB kanalları için ağırlıklar
weights = [0.2989, 0.5870, 0.1140]

# Renkli görüntüyü gri tonlamalı hale getiriyoruz
# NumPy dot (nokta) çarpım fonksiyonu ile matris çarpımı yapılıyor
gray_image = np.dot(image_matrix[..., :3], weights)

# Görüntüyü gösteriyoruz
plt.imshow(gray_image, cmap='gray')
plt.title('Siyah Beyaz Görüntü')
plt.axis('off')  # Eksenleri gizliyoruz
plt.show()

# Siyah-beyaz görüntü matrisini yazdırmak isterseniz
print("Siyah-Beyaz Görüntü Matris Boyutları: ", gray_image.shape)

gray_image_indir = Image.fromarray(np.uint8(gray_image))
gray_image_indir.save('C:/Users/Dell/Downloads/Asistanlık/Dersler/Görüntü İşleme/Uygulamalar-Yeni/kelebek_siyahbeyaz.jpeg')


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Görüntülerin dosya yollarını belirtme
circle_path = r'C:\Users\Dell\Downloads\Asistanlık\Dersler\Görüntü İşleme\Uygulamalar-Yeni\Hafta 2\daire.png'
triangle_path = r'C:\Users\Dell\Downloads\Asistanlık\Dersler\Görüntü İşleme\Uygulamalar-Yeni\Hafta 2\ucgen.png'

# Görüntüleri açma ve tek kanala çevirme
circle_image = Image.open(circle_path).convert('L') 
triangle_image = Image.open(triangle_path).convert('L') 

# Görüntüleri ikili (binary) hale getirme
threshold = 128  # Piksel eşiği
circle_binary = np.array(circle_image) > threshold  # Piksel değeri 128'den büyükse True, değilse False
triangle_binary = np.array(triangle_image) > threshold  # Piksel değeri 128'den büyükse True, değilse False

# Küme işlemleri yapma
# 1. Birleşim (Union) -> A ∪ B
union = np.logical_or(circle_binary, triangle_binary)

# 2. Kesişim (Intersection) -> A ∩ B
intersection = np.logical_and(circle_binary, triangle_binary)

# 3. Fark (Difference) -> A - B
difference = np.logical_and(circle_binary, np.logical_not(triangle_binary))

# 4. Tamamlayıcı (Complement) -> A^c
complement_circle = np.logical_not(circle_binary)

# Sonuçları görselleştirme
plt.figure(figsize=(10, 8))

# Orijinal daire ve üçgen görüntüleri
plt.subplot(2, 3, 1)
plt.imshow(circle_binary, cmap='gray')
plt.title('Daire (A)')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(triangle_binary, cmap='gray')
plt.title('Üçgen (B)')
plt.axis('off')

# Birleşim -> A ∪ B
plt.subplot(2, 3, 3)
plt.imshow(union, cmap='gray')
plt.title('Birleşim (A ∪ B)')
plt.axis('off')

# Kesişim -> A ∩ B
plt.subplot(2, 3, 4)
plt.imshow(intersection, cmap='gray')
plt.title('Kesişim (A ∩ B)')
plt.axis('off')

# Fark -> A - B
plt.subplot(2, 3, 5)
plt.imshow(difference, cmap='gray')
plt.title('Fark (A - B)')
plt.axis('off')

# Tamamlayıcı -> A^c
plt.subplot(2, 3, 6)
plt.imshow(complement_circle, cmap='gray')
plt.title('Daire Tamamlayıcı (A^c)')
plt.axis('off')

plt.tight_layout()
plt.show()

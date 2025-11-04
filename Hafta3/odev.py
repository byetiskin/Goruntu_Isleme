import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Görüntüleri yükle
a = cv2.imread('gunes.jpg', cv2.IMREAD_GRAYSCALE)
b = cv2.imread('cicek.jpg', cv2.IMREAD_GRAYSCALE)

if a is None or b is None:
    raise FileNotFoundError("Lütfen 'gunes.jpg' ve 'cicek.jpg' aynı klasöre ekleyin.")

# Aynı boyutta değilse boyutlarını eşitle
a = cv2.resize(a, (256, 256))
b = cv2.resize(b, (256, 256))

# 2. Görüntüleri topla
ab_sum = cv2.addWeighted(a, 0.8, b, 0.2, 0)  # normalize edilmiş toplama

# 3. Doğrusal filtre (Gaussian) uygula
gauss_ab = cv2.GaussianBlur(ab_sum, (5,5), 1)   # (a+b)'ye filtre

gauss_a = cv2.GaussianBlur(a, (5,5), 1)         # a'ya filtre
gauss_b = cv2.GaussianBlur(b, (5,5), 1)         # b'ye filtre
gauss_sum = cv2.addWeighted(gauss_a, 0.5, gauss_b, 0.5, 0)  # filtreli görüntülerin toplamı

# 4. Görselleri 3x3 olarak göster
plt.figure(figsize=(14,10))

# Satır 1: a görüntüsü b görüntüsü a+b görüntüsü
plt.subplot(3,3,1)
plt.title("A Görüntüsü")
plt.imshow(a, cmap='gray')
plt.axis('off')

plt.subplot(3,3,2)
plt.title("B Görüntüsü")
plt.imshow(b, cmap='gray')
plt.axis('off')

plt.subplot(3,3,3)
plt.title("A + B (Toplam)")
plt.imshow(ab_sum, cmap='gray')
plt.axis('off')

# Satır 2: a filtreli b filtreli
plt.subplot(3,3,4)
plt.title("A Filtreli")
plt.imshow(gauss_a, cmap='gray')
plt.axis('off')

plt.subplot(3,3,5)
plt.title("B Filtreli")
plt.imshow(gauss_b, cmap='gray')
plt.axis('off')

# Satır 3: a filtreli+b filtreli toplamı ile (a+b) toplamına filtre
plt.subplot(3,3,7)
plt.title("A Filtreli + B Filtreli Toplamı")
plt.imshow(gauss_sum, cmap='gray')
plt.axis('off')

plt.subplot(3,3,8)
plt.title("(A + B)'ye Filtre")
plt.imshow(gauss_ab, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

# 5. Açıklama
# Bu deneyde Gaussian (doğrusal) filtre kullanıldığı için
# (A + B)'ye uygulanan filtre ≈ A'ya filtre + B'ye filtre sonucu verir.
# Bu özellik doğrusal filtrelerin "toplanabilirlik" (additivity) özelliğini gösterir.

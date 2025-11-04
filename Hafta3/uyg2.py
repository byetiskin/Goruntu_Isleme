import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lenna.jpeg', cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("Lütfen 'example.jpg' adlı bir görüntü dosyası aynı klasöre ekleyin.")

plt.figure(figsize=(10,4))
plt.subplot(1,3,1)
plt.title("Orijinal Görüntü")
plt.imshow(img, cmap='gray')
plt.axis('off')

# Sobel fonksiyonu: kenar tespiti için gradyan hesaplar.
# (1,0) → x yönü, (0,1) → y yönü
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)

plt.subplot(1,3,2)
plt.title("Sobel Filtresi")
plt.imshow(sobel, cmap='gray')
plt.axis('off')


# OpenCV'de hazır Prewitt yok, biz çekirdekleri kendimiz tanımlıyoruz.
kernelx = np.array([[-1, 0, 1],
                    [-1, 0, 1],
                    [-1, 0, 1]])

kernely = np.array([[ 1,  1,  1],
                    [ 0,  0,  0],
                    [-1, -1, -1]])

# Her iki yönde konvolüsyon uygula
prewittx = cv2.filter2D(img, -1, kernelx)
prewitty = cv2.filter2D(img, -1, kernely)

# Gradyan büyüklüğünü hesapla
prewitt = cv2.magnitude(prewittx.astype(float), prewitty.astype(float))

plt.subplot(1,3,3)
plt.title("Prewitt Filtresi")
plt.imshow(prewitt, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

# Sobel, Prewitt'e göre merkez piksele daha fazla ağırlık verir.
# Bu yüzden kenarlar Sobel filtresinde biraz daha belirgin çıkar.
# Her iki filtre de doğrusal (linear) filtrelerdir.

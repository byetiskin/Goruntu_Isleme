import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Görüntüyü açma
image_path = 'C:/Users/Dell/Downloads/Asistanlık/Dersler/Görüntü İşleme/Uygulamalar-Yeni/Hafta 2/galaksi.jpg'
image = Image.open(image_path)
image = np.array(image)

# Gaussian gürültüsü parametreleri
mean = 0
sigma = 50
gaussian_noise = np.random.normal(mean, sigma, image.shape)

# Gürültüyü görüntüye ekleme
noisy_image = image + gaussian_noise

# Piksel değerlerinin 0-255 aralığında kalması için limitleme
noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

# Görüntüleri gösterme
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(noisy_image, cmap='gray')
plt.title('Gaussian Gürültülü Görüntü')
plt.axis('off')

plt.show()

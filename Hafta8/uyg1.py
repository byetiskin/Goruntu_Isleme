import cv2
import numpy as np
import matplotlib.pyplot as plt

# Gürültü eklemek için fonksiyon
def add_noise(image, sigma):
    """
    Görüntüye Gauss gürültüsü ekler.
    :param image: Giriş görüntüsü (gri tonlamalı)
    :param sigma: Gürültünün standart sapması
    :return: Gürültülü görüntü
    """
    noise = np.random.normal(0, sigma, image.shape)  # Gauss gürültüsü oluştur
    noisy_image = image + noise  # Gürültüyü görüntüye ekle
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)  # Piksel değerlerini sınırla
    return noisy_image

# Orijinal görüntüyü yükle
image_path = "resim.jpg"  # Kendi görüntü dosyanızın yolunu yazın
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Görüntü yüklenemedi! Lütfen dosya yolunu kontrol edin.")
else:
    # Farklı sigma değerleriyle gürültülü görüntüler üret
    sigmas = [10, 30, 50]
    noisy_images = [add_noise(image, sigma) for sigma in sigmas]

    # Gürültülü görüntüleri plot et
    plt.figure(figsize=(12, 4))
    for i, sigma in enumerate(sigmas):
        plt.subplot(1, len(sigmas), i + 1)
        plt.imshow(noisy_images[i], cmap='gray')
        plt.title(f"Sigma: {sigma}")
        plt.axis('off')
    plt.suptitle("Farklı Sigma Değerleri ile Gürültü")
    plt.show()

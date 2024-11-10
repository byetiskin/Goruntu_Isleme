import cv2
import numpy as np
import matplotlib.pyplot as plt

# Ortalama filtre fonksiyonu
def mean_filter(image, kernel_size=3):
    """
    Ortalama filtre uygular.
    :param image: Gri tonlamalı görüntü
    :param kernel_size: Filtre boyutu (örnek: 3x3)
    :return: Filtrelenmiş görüntü
    """
    pad_size = kernel_size // 2
    padded_image = np.pad(image, pad_size, mode='constant', constant_values=0)
    filtered_image = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            kernel_region = padded_image[i:i + kernel_size, j:j + kernel_size]
            filtered_image[i, j] = np.mean(kernel_region)
    return filtered_image

# Gauss filtre fonksiyonu
def gaussian_filter(image, kernel_size=3):
    """
    Gauss filtresi uygular.
    :param image: Gri tonlamalı görüntü
    :param kernel_size: Filtre boyutu
    :return: Filtrelenmiş görüntü
    """
    pad_size = kernel_size // 2
    padded_image = np.pad(image, pad_size, mode='constant', constant_values=0)
    filtered_image = np.zeros_like(image)

    # Gauss kernel oluştur
    ax = np.arange(-pad_size, pad_size + 1)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2) / (2 * (pad_size**2)))
    kernel /= np.sum(kernel)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            kernel_region = padded_image[i:i + kernel_size, j:j + kernel_size]
            filtered_image[i, j] = np.sum(kernel_region * kernel)
    return filtered_image

# Medyan filtre fonksiyonu
def median_filter(image, kernel_size=3):
    """
    Medyan filtre uygular.
    :param image: Gri tonlamalı görüntü
    :param kernel_size: Filtre boyutu
    :return: Filtrelenmiş görüntü
    """
    pad_size = kernel_size // 2
    padded_image = np.pad(image, pad_size, mode='constant', constant_values=0)
    filtered_image = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            kernel_region = padded_image[i:i + kernel_size, j:j + kernel_size]
            filtered_image[i, j] = np.median(kernel_region)
    return filtered_image

# Gürültülü bir görüntü oluştur
image_path = "resim.jpg"  # Kendi görüntü dosyanızın yolunu yazın
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Görüntü yüklenemedi! Lütfen dosya yolunu kontrol edin.")
else:
    # Gürültü ekle
    sigma = 30
    noisy_image = np.random.normal(0, sigma, image.shape) + image
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

    # Filtreleri uygula
    mean_filtered = mean_filter(noisy_image)
    gaussian_filtered = gaussian_filter(noisy_image)
    median_filtered = median_filter(noisy_image)

    # Orijinal ve filtrelenmiş görüntüleri plot et
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 4, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Orijinal")
    plt.axis('off')

    plt.subplot(1, 4, 2)
    plt.imshow(mean_filtered, cmap='gray')
    plt.title("Ortalama Filtre")
    plt.axis('off')

    plt.subplot(1, 4, 3)
    plt.imshow(gaussian_filtered, cmap='gray')
    plt.title("Gauss Filtre")
    plt.axis('off')

    plt.subplot(1, 4, 4)
    plt.imshow(median_filtered, cmap='gray')
    plt.title("Medyan Filtre")
    plt.axis('off')

    plt.suptitle("Filtreleme Sonuçları")
    plt.show()

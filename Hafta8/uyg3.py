import cv2
import numpy as np
import matplotlib.pyplot as plt

# Sağ fark hesaplama
def right_difference(image):
    """
    Sağ farkı hesaplar.
    :param image: Giriş görüntüsü (gri tonlamalı)
    :return: Sağ farkı içeren görüntü
    """
    kernel = np.array([[1, -1]])
    right_diff = cv2.filter2D(image, -1, kernel)
    return right_diff

# Sol fark hesaplama
def left_difference(image):
    """
    Sol farkı hesaplar.
    :param image: Giriş görüntüsü (gri tonlamalı)
    :return: Sol farkı içeren görüntü
    """
    kernel = np.array([[-1, 1]])
    left_diff = cv2.filter2D(image, -1, kernel)
    return left_diff

# Dikey kenar hesaplama
def vertical_edges(image):
    """
    Dikey kenarları hesaplar.
    :param image: Giriş görüntüsü (gri tonlamalı)
    :return: Dikey kenarları içeren görüntü
    """
    kernel = np.array([[-1], [2], [-1]])
    vertical_diff = cv2.filter2D(image, -1, kernel)
    return vertical_diff

# Yatay kenar hesaplama
def horizontal_edges(image):
    """
    Yatay kenarları hesaplar.
    :param image: Giriş görüntüsü (gri tonlamalı)
    :return: Yatay kenarları içeren görüntü
    """
    kernel = np.array([[-1, 2, -1]])
    horizontal_diff = cv2.filter2D(image, -1, kernel)
    return horizontal_diff

# Keskinleştirme fonksiyonu
def sharpen_image(image):
    """
    Görüntüyü keskinleştirir.
    :param image: Giriş görüntüsü (gri tonlamalı)
    :return: Keskinleştirilmiş görüntü
    """
    blurred_image = cv2.GaussianBlur(image, (3, 3), 0)  # Yumuşatma
    edges = image - blurred_image  # Kenarları hesapla
    sharpened_image = image + edges  # Keskinleştirilmiş görüntü
    return sharpened_image

# Görüntüyü yükle
image_path = "resim.jpg"  # Kendi görüntü dosyanızın yolunu yazın
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Görüntü yüklenemedi! Lütfen dosya yolunu kontrol edin.")
else:
    # Farkları ve kenarları hesapla
    right_diff = right_difference(image)
    left_diff = left_difference(image)
    vertical_diff = vertical_edges(image)
    horizontal_diff = horizontal_edges(image)
    sharpened_image = sharpen_image(image)

    # Sonuçları görselleştir
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Orijinal Görüntü")
    plt.axis('off')

    plt.subplot(2, 3, 2)
    plt.imshow(right_diff, cmap='gray')
    plt.title("Sağ Fark")
    plt.axis('off')

    plt.subplot(2, 3, 3)
    plt.imshow(left_diff, cmap='gray')
    plt.title("Sol Fark")
    plt.axis('off')

    plt.subplot(2, 3, 4)
    plt.imshow(vertical_diff, cmap='gray')
    plt.title("Dikey Kenarlar")
    plt.axis('off')

    plt.subplot(2, 3, 5)
    plt.imshow(horizontal_diff, cmap='gray')
    plt.title("Yatay Kenarlar")
    plt.axis('off')

    plt.subplot(2, 3, 6)
    plt.imshow(sharpened_image, cmap='gray')
    plt.title("Keskinleştirilmiş Görüntü")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

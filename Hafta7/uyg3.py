import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_histogram(image):
    """
    1. Histogramı hesapla
    """
    histogram = [0] * 256
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel_value = image[i, j]
            histogram[pixel_value] += 1
    return histogram

def calculate_pdf(histogram, total_pixels):
    """
    2. Olasılık Yoğunluk Fonksiyonu (PDF) hesapla
    """
    pdf = [h / total_pixels for h in histogram]
    return pdf

def calculate_cdf(pdf):
    """
    3. Kümülatif Yoğunluk Fonksiyonu (CDF) hesapla
    """
    cdf = [0] * 256
    cdf[0] = pdf[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + pdf[i]
    return cdf

def histogram_equalization(image):
    """
    Histogram eşitleme işlemini uygular.
    """
    # Adım 1: Histogramı hesapla
    histogram = calculate_histogram(image)
    
    # Adım 2: PDF hesapla
    total_pixels = image.size
    pdf = calculate_pdf(histogram, total_pixels)
    
    # Adım 3: CDF hesapla
    cdf = calculate_cdf(pdf)
    
    # Adım 4: T(r) = CDF olacak şekilde dönüşüm uygula
    new_pixel_values = [int(cdf[i] * 255) for i in range(256)]
    
    # Yeni piksel değerleri ile görüntüyü güncelle
    equalized_image = np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            equalized_image[i, j] = new_pixel_values[image[i, j]]
    
    return equalized_image

# Gri tonlamalı örnek görüntüyü yükleyin
image = cv2.imread('bulut.png', cv2.IMREAD_GRAYSCALE)
histogram = calculate_histogram(image)

# Orijinal histogramı çizin
plt.figure()
plt.plot(histogram)
plt.title('Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.xlim([0, 255])

# Histogram eşitleme işlemini gerçekleştirin
equalized_image = histogram_equalization(image)

# Eşitlenmiş histogramı hesaplayın ve çiz
equalized_histogram = calculate_histogram(equalized_image)
plt.figure()
plt.plot(equalized_histogram)
plt.title('İyileştirilmiş Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.xlim([0, 255])

# Sonuçları görselleştirin
plt.figure(figsize=(12, 6))

# Orijinal görüntü
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Orijinal Görüntü')
plt.axis('off')

# Histogram Eşitleme Sonucu
plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Histogram Eşitleme Sonucu')
plt.axis('off')

plt.show()

import cv2
import matplotlib.pyplot as plt

# Gri görüntü histogramı
def calculate_histogram_grayscale(image):
    # Histogram dizisini elle başlatma (256 sıfırdan oluşan dizi)
    histogram = [0] * 256
    
    # Görüntüyü 2D dizi olarak gezinerek her pikselin yoğunluk değerini hesapla
    for i in range(len(image)):
        for j in range(len(image[i])):
            pixel_value = image[i][j]
            histogram[pixel_value] += 1  # Her piksel değeri için sayıyı artır
    return histogram


# Renkli görüntü histogramı
def calculate_histogram_color(image):
    # B, G, R kanalları için histogram dizilerini elle başlat
    histogram_b = [0] * 256
    histogram_g = [0] * 256
    histogram_r = [0] * 256
    
    # B, G, R kanallarını ayrı ayrı hesapla
    for i in range(len(image)):
        for j in range(len(image[i])):
            b_value, g_value, r_value = image[i][j]
            histogram_b[b_value] += 1  # Mavi kanal
            histogram_g[g_value] += 1  # Yeşil kanal
            histogram_r[r_value] += 1  # Kırmızı kanal
    
    return histogram_b, histogram_g, histogram_r

# Örnek görüntü yükleme
image_gray = cv2.imread('kus.jpg', cv2.IMREAD_GRAYSCALE)
image_color = cv2.imread('kus.jpg', cv2.IMREAD_COLOR)

# Gri görüntü için histogram hesapla
histogram_gray = calculate_histogram_grayscale(image_gray)

# Renkli görüntü için histogram hesapla
histogram_b, histogram_g, histogram_r = calculate_histogram_color(image_color)

# Gri tonlama histogramını ayrı bir grafikte çizme
plt.figure()
plt.plot(histogram_gray, color='black')
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.xlim([0, 255])

# Renkli görüntü histogramlarını aynı grafikte çizme
plt.figure()
plt.plot(histogram_b, color='blue', label='Blue Channel')
plt.plot(histogram_g, color='green', label='Green Channel')
plt.plot(histogram_r, color='red', label='Red Channel')
plt.title('Color Channels Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.xlim([0, 255])
plt.legend()

plt.show()


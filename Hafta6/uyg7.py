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

# Histogramı çizme
def plot_histogram(histogram, title, color='k'):
    plt.figure()
    plt.plot(histogram, color=color)
    plt.title(title)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 255])

# Örnek görüntü yükleme
image_gray = cv2.imread('kus_kucuk.jpg', cv2.IMREAD_GRAYSCALE)
image_color = cv2.imread('kus_kucuk.jpg', cv2.IMREAD_COLOR)

# Gri görüntü için histogram hesapla ve çiz
histogram_gray = calculate_histogram_grayscale(image_gray)
plot_histogram(histogram_gray, 'Grayscale Histogram', color='black')

# Renkli görüntü için histogram hesapla ve çiz
histogram_b, histogram_g, histogram_r = calculate_histogram_color(image_color)
plot_histogram(histogram_b, 'Blue Channel Histogram', color='blue')
plot_histogram(histogram_g, 'Green Channel Histogram', color='green')
plot_histogram(histogram_r, 'Red Channel Histogram', color='red')

plt.show()

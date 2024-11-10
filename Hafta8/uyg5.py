import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü yükle
image_path = "resim2.jpg"  # Kendi görüntü dosyanızın yolunu yazın
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Görüntü yüklenemedi! Lütfen dosya yolunu kontrol edin.")
else:
    # Kenar tespiti için Canny uygulanıyor
    edges = cv2.Canny(image, 50, 150)

    # Hough Çizgi Dönüşümü
    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=200)
    image_with_lines = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    if lines is not None:
        for rho_theta in lines:
            rho, theta = rho_theta[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(image_with_lines, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Yeşil çizgi

    # Hough Daire Dönüşümü
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                                param1=100, param2=40, minRadius=30, maxRadius=100)
    image_with_circles = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]
            cv2.circle(image_with_circles, center, radius, (255, 0, 0), 2)  # Mavi daire
            cv2.circle(image_with_circles, center, 2, (0, 0, 255), 3)  # Merkez noktası kırmızı

    # Görselleştirme
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Orijinal Görüntü")
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title("Kenarlar (Canny)")
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(image_with_lines, cv2.COLOR_BGR2RGB))
    plt.title("Hough Çizgi Tespiti")
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(cv2.cvtColor(image_with_circles, cv2.COLOR_BGR2RGB))
    plt.title("Hough Daire Tespiti")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

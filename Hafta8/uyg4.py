import cv2
import numpy as np
import matplotlib.pyplot as plt

# Robert Kenar Tespiti
def roberts_edge_detection(image):
    kernel_x = np.array([[1, 0], [0, -1]])
    kernel_y = np.array([[0, 1], [-1, 0]])
    grad_x = cv2.filter2D(image, -1, kernel_x)
    grad_y = cv2.filter2D(image, -1, kernel_y)
    roberts = np.sqrt(grad_x**2 + grad_y**2).astype(np.uint8)
    return roberts

# Prewitt Kenar Tespiti
def prewitt_edge_detection(image):
    kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    grad_x = cv2.filter2D(image, -1, kernel_x)
    grad_y = cv2.filter2D(image, -1, kernel_y)
    prewitt = np.sqrt(grad_x**2 + grad_y**2).astype(np.uint8)
    return prewitt

# Sobel Kenar Tespiti
def sobel_edge_detection(image):
    grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobel = np.sqrt(grad_x**2 + grad_y**2).astype(np.uint8)
    return sobel

# Laplacian of Gaussian (LoG)
def log_edge_detection(image):
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    log = cv2.Laplacian(blurred, cv2.CV_64F)
    log = np.uint8(np.absolute(log))
    return log

# Difference of Gaussians (DoG)
def dog_edge_detection(image):
    blurred1 = cv2.GaussianBlur(image, (3, 3), 1)
    blurred2 = cv2.GaussianBlur(image, (3, 3), 2)
    dog = cv2.absdiff(blurred1, blurred2)
    return dog

# Canny Kenar Tespiti
def canny_edge_detection(image):
    canny = cv2.Canny(image, 100, 200)
    return canny

# Görüntüyü Yükleme
image_path = "resim.jpg"  # Görüntü yolunu güncelleyin
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Görüntü yüklenemedi! Lütfen dosya yolunu kontrol edin.")
else:
    # Kenar Tespit Yöntemlerini Uygula
    roberts = roberts_edge_detection(image)
    prewitt = prewitt_edge_detection(image)
    sobel = sobel_edge_detection(image)
    log = log_edge_detection(image)
    dog = dog_edge_detection(image)
    canny = canny_edge_detection(image)

    # Görselleştirme
    plt.figure(figsize=(18, 10))
    
        
    plt.subplot(2, 3, 1)
    plt.imshow(roberts, cmap='gray')
    plt.title("Robert Kenar Tespiti")
    plt.axis('off')
    
    plt.subplot(2, 3, 2)
    plt.imshow(prewitt, cmap='gray')
    plt.title("Prewitt Kenar Tespiti")
    plt.axis('off')
    
    plt.subplot(2, 3, 3)
    plt.imshow(sobel, cmap='gray')
    plt.title("Sobel Kenar Tespiti")
    plt.axis('off')
    
    plt.subplot(2, 3, 4)
    plt.imshow(log, cmap='gray')
    plt.title("LoG Kenar Tespiti")
    plt.axis('off')
    
    plt.subplot(2, 3, 5)
    plt.imshow(dog, cmap='gray')
    plt.title("DoG Kenar Tespiti")
    plt.axis('off')
    
    plt.subplot(2, 3, 6)
    plt.imshow(canny, cmap='gray')
    plt.title("Canny Kenar Tespiti")
    plt.axis('off')
    
    plt.show()

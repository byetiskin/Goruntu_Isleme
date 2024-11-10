import cv2
import numpy as np

# Sınır Çıkarımı
def boundary_extraction(image, kernel_size=3):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    erosion = cv2.erode(image, kernel, iterations=1)
    boundary = image - erosion
    return boundary

# Delik Doldurma
def hole_filling(image):
    inverted = cv2.bitwise_not(image)
    flood_filled = inverted.copy()
    h, w = image.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    cv2.floodFill(flood_filled, mask, (0, 0), 255)
    hole_filled = cv2.bitwise_not(flood_filled)
    return image | hole_filled

# Bağlı Bileşenlerin Çıkarımı
def connected_components(image):
    num_labels, labels = cv2.connectedComponents(image)
    return labels, num_labels

# Dış Bükey Gövde
def convex_hull(image):
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    hull_image = np.zeros_like(image)
    for contour in contours:
        hull = cv2.convexHull(contour)
        cv2.drawContours(hull_image, [hull], -1, 255, -1)
    return hull_image

# İnceleme
def thinning(image):
    return cv2.ximgproc.thinning(image)

# Kalınlaştırma
def thickening(image, kernel_size=3):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    dilation = cv2.dilate(image, kernel, iterations=1)
    return dilation

# İskeletler
def skeletonization(image):
    skeleton = np.zeros_like(image)
    temp = image.copy()
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    while True:
        eroded = cv2.erode(temp, kernel)
        temp_open = cv2.morphologyEx(eroded, cv2.MORPH_OPEN, kernel)
        subset = eroded - temp_open
        skeleton = cv2.bitwise_or(skeleton, subset)
        temp = eroded.copy()
        if cv2.countNonZero(temp) == 0:
            break
    return skeleton

# Budama
def pruning(image, iterations=1):
    pruned = image.copy()
    for _ in range(iterations):
        pruned = cv2.erode(pruned, None)
    return pruned

# Geodezik İnşa
def geodesic_reconstruction(marker, mask):
    while True:
        dilated = cv2.dilate(marker, None, iterations=1)
        intersection = cv2.bitwise_and(dilated, mask)
        if np.array_equal(marker, intersection):
            break
        marker = intersection
    return marker

# Gri Seviyede Morfolojik İşlemler
def gray_morphology(image, operation="erosion", kernel_size=3):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    if operation == "erosion":
        return cv2.erode(image, kernel, iterations=1)
    elif operation == "dilation":
        return cv2.dilate(image, kernel, iterations=1)

# Test Görüntüsü Yükleme
image_path = "biber.jpg"  # Test görüntünüzün yolunu yazın
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# İşlemleri Uygulama
boundary = boundary_extraction(binary_image)
filled = hole_filling(binary_image)
labels, num_labels = connected_components(binary_image)
convex = convex_hull(binary_image)
thick = thickening(binary_image)
skeleton = skeletonization(binary_image)
pruned = pruning(binary_image)

# Görselleştirme 
cv2.imshow("Orijinal", binary_image)
cv2.imshow("Sinir Cikarimi", boundary)  # Sınır Çıkarımı
cv2.imshow("Delik Doldurma", filled)
cv2.imshow("Dis Bukey Govde", convex)  # Dış Bükey Gövde
cv2.imshow("Kalinlastirma", thick)  # Kalınlaştırma
cv2.imshow("Iskeletler", skeleton)  # İskeletler
cv2.imshow("Budama", pruned)

cv2.waitKey(0)
cv2.destroyAllWindows()


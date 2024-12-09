import cv2
import matplotlib.pyplot as plt

# Görüntü ve maskeyi yükleme
image_path = "cxrimage_0.png"  # Orijinal akciğer görüntüsü yolu
mask_path = "cxrmask_0.jpeg"  # Akciğer maskesi görüntüsü yolu

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Gri tonlamalı yükleme
mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)   # Maskeyi gri tonlamalı yükle

# Maskeyi binary (ikili) hale getirme
_, binary_mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

# Maskeyi görüntüye uygulama
masked_image = cv2.bitwise_and(image, image, mask=binary_mask)

# SIFT dedektörünü başlatma
sift = cv2.SIFT_create()

# Maskelenmiş görüntüde anahtar noktaları tespit etme ve deskriptörleri çıkarma
keypoints, descriptors = sift.detectAndCompute(masked_image, None)

# Anahtar noktaları orijinal görüntü üzerine çizme
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Sonuçları görselleştirme
plt.figure(figsize=(15, 5))

# Orijinal görüntü
plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(image, cmap="gray")
plt.axis("off")

# Maskelenmiş görüntü
plt.subplot(1, 3, 2)
plt.title("Masked Image")
plt.imshow(masked_image, cmap="gray")
plt.axis("off")

# Anahtar noktalar çizilmiş görüntü
plt.subplot(1, 3, 3)
plt.title("Keypoints on Original Image")
plt.imshow(image_with_keypoints, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.show()

# Anahtar nokta koordinatlarını yazdırma
print("Number of Keypoints Detected:", len(keypoints))
for i, kp in enumerate(keypoints[:5]):  # Sadece ilk 5 anahtar nokta
    print(f"Keypoint {i + 1}: X={kp.pt[0]:.2f}, Y={kp.pt[1]:.2f}, Size={kp.size:.2f}")

"""
import cv2
import matplotlib.pyplot as plt

# Görüntü ve maskeyi yükleme
image_path = "cxrimage_0.png"  # Orijinal akciğer görüntüsü yolu
mask_path = "cxrmask_0.jpeg"  # Akciğer maskesi görüntüsü yolu

# Görüntüleri gri tonlamalı olarak yükle
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

# Görüntülerin doğru yüklendiğini kontrol et
if image is None:
    raise FileNotFoundError(f"Görüntü bulunamadı: {image_path}")
if mask is None:
    raise FileNotFoundError(f"Maske bulunamadı: {mask_path}")

# Maskeyi binary (ikili) hale getirme
_, binary_mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

# Maskeyi görüntüye uygulama
masked_image = cv2.bitwise_and(image, image, mask=binary_mask)

# Maskelenmiş görüntünün boş olmadığını kontrol et
if masked_image is None or masked_image.size == 0:
    raise ValueError("Maskelenmiş görüntü boş. Lütfen maskeyi kontrol edin.")

# SIFT dedektörünü başlatma
sift = cv2.SIFT_create()

# Maskelenmiş görüntüde anahtar noktaları tespit etme ve deskriptörleri çıkarma
keypoints, descriptors = sift.detectAndCompute(masked_image, None)

if keypoints is None or len(keypoints) == 0:
    print("Hiç anahtar nokta tespit edilemedi.")
else:
    # Anahtar noktaları orijinal görüntü üzerine çizme
    image_with_keypoints = cv2.drawKeypoints(
        image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    )

    # Sonuçları görselleştirme
    plt.figure(figsize=(15, 5))

    # Orijinal görüntü
    plt.subplot(1, 3, 1)
    plt.title("Original Image")
    plt.imshow(image, cmap="gray")
    plt.axis("off")

    # Maskelenmiş görüntü
    plt.subplot(1, 3, 2)
    plt.title("Masked Image")
    plt.imshow(masked_image, cmap="gray")
    plt.axis("off")

    # Anahtar noktalar çizilmiş görüntü
    plt.subplot(1, 3, 3)
    plt.title("Keypoints on Original Image")
    plt.imshow(image_with_keypoints, cmap="gray")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    # Anahtar nokta koordinatlarını yazdırma
    print("Number of Keypoints Detected:", len(keypoints))
    for i, kp in enumerate(keypoints[:5]):  # Sadece ilk 5 anahtar nokta
        print(f"Keypoint {i + 1}: X={kp.pt[0]:.2f}, Y={kp.pt[1]:.2f}, Size={kp.size:.2f}")
"""



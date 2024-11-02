# pip install SimpleITK matplotlib

import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

# Tüm MHA dosyalarının bulunduğu ana klasör
base_folder = "C:/Users/Dell/Downloads/10927452/PENGWIN_CT_train_images_part1"  # Kendi klasörünüzle değiştirin

# İşlenecek olan MHA dosyalarının olduğu klasördeki tüm dosyaları listele
def get_mha_files(folder_path):
    mha_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.mha'):
                mha_files.append(os.path.join(root, file))
    return mha_files

# Basit görüntü işleme fonksiyonları
def process_image(image_array):
    # 1. Histogram Eşitleme
    equalized_image = cv2.equalizeHist(image_array.astype(np.uint8))
    
    # 2. Gauss Bulanıklığı
    blurred_image = cv2.GaussianBlur(equalized_image, (5, 5), 1.0)
    
    # 3. Kenar Tespiti (Canny Edge Detection)
    edges = cv2.Canny(blurred_image, 50, 150)
    
    return equalized_image, blurred_image, edges

# Klasördeki tüm MHA dosyalarını işleyin
mha_files = get_mha_files(base_folder)
print(f"Toplam {len(mha_files)} adet MHA dosyası bulundu.")

for file_path in mha_files:
    # MHA dosyasını aç
    image = sitk.ReadImage(file_path)
    image_array = sitk.GetArrayFromImage(image)
    
    # Orta dilimi seç (örneğin, görüntünün Z ekseninin ortasındaki dilim)
    middle_slice = image_array[image_array.shape[0] // 2]
    
    # Görüntü işleme adımlarını uygula
    equalized_image, blurred_image, edges = process_image(middle_slice)
    
    # Sonuçları görselleştir
    plt.figure(figsize=(12, 8))
    
    plt.subplot(1, 4, 1)
    plt.imshow(middle_slice, cmap='gray')
    plt.title('Orijinal Orta Dilim')
    plt.axis('off')

    plt.subplot(1, 4, 2)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Histogram Eşitleme')
    plt.axis('off')

    plt.subplot(1, 4, 3)
    plt.imshow(blurred_image, cmap='gray')
    plt.title('Gauss Bulanıklığı')
    plt.axis('off')

    plt.subplot(1, 4, 4)
    plt.imshow(edges, cmap='gray')
    plt.title('Kenar Tespiti')
    plt.axis('off')
    
    plt.suptitle(f"İşlenen Görüntü: {os.path.basename(file_path)}")
    plt.show()

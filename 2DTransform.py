import os
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize
from skimage import io, img_as_ubyte

# Dosya yolları
img_path = "amos_img_0001.nii.gz"
label_path = "amos_label_0001.nii.gz"

# Veri yükleme
img = nib.load(img_path).get_fdata()  # Orijinal görüntü
label = nib.load(label_path).get_fdata()  # Etiket görüntüsü

# Coronal görünüm için transpoz işlemi
coronal_img = np.transpose(img, (2, 0, 1))  # x-y-z eksen sırası
coronal_label = np.transpose(label, (2, 0, 1))  # Aynı işlem etiket için

# Orta coronal slice seçimi
mid_slice = coronal_img.shape[2] // 2  # Orta dilimi seç
img_coronal_mid = coronal_img[:, :, mid_slice]  # Orta slice (orijinal görüntü)
label_coronal_mid = coronal_label[:, :, mid_slice]  # Orta slice (etiket)

# Sadece label 6'yı gösterecek şekilde maskeleme
label_coronal_mid_masked = (label_coronal_mid == 6).astype(np.uint8) * 255  # Sadece 6'yı tut

# Görselleri 768x768 boyutuna yeniden boyutlandırma
img_coronal_resized = resize(img_coronal_mid, (768, 768), anti_aliasing=True)
label_coronal_resized = resize(label_coronal_mid_masked, (768, 768), anti_aliasing=False, order=0)

# Görüntüleri normalize ederek uint8 formatına dönüştürmek için uygun hale getirme
img_coronal_normalized = (img_coronal_resized - img_coronal_resized.min()) / (img_coronal_resized.max() - img_coronal_resized.min())
img_uint8 = img_as_ubyte(img_coronal_normalized)  # Orijinal görüntü için dönüşüm
label_uint8 = label_coronal_resized.astype(np.uint8)  # Label zaten uint8 formatında
img_uint8_flipped = np.flipud(img_uint8)
label_uint8_flipped = np.flipud(label_uint8)

# Kayıt İşlevi
def save_slices(img, label, img_path, label_path):
    """
    Kaydedilen dosyaları orijinal isimlerini koruyarak PNG olarak kaydeder.
    """
    # Çıktı dizinlerini ayarla
    image_dir = "dataset/image"
    label_dir = "dataset/label"
    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(label_dir, exist_ok=True)

    # Dosya adlarını belirle
    img_name = os.path.splitext(os.path.basename(img_path))[0] + ".png"
    label_name = os.path.splitext(os.path.basename(label_path))[0] + ".png"

    # Dosyaları kaydet
    io.imsave(os.path.join(image_dir, img_name), img)
    io.imsave(os.path.join(label_dir, label_name), label)

# Kayıt işlemini çağır
save_slices(img_uint8_flipped, label_uint8_flipped, img_path, label_path)

# Görselleştirme
plt.figure(figsize=(12, 6))

# Orijinal Görüntü
plt.subplot(1, 2, 1)
plt.title("Image")
plt.imshow(img_uint8_flipped, cmap="gray", origin="upper")

# Etiket (Label) Görüntüsü
plt.subplot(1, 2, 2)
plt.title("Label 6")
plt.imshow(label_uint8_flipped, cmap="gray", origin="upper")

plt.show()

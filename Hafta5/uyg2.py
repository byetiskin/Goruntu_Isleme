import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

# Ana pencereyi oluştur
form = tk.Tk()
form.title("İki Resim İşlemleri")
form.geometry("1200x300")

# Global resim değişkenleri
img1_cv = None
img2_cv = None

def resim_sec(label_image, image_num):
    global img1_cv, img2_cv
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")])
    
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((150, 150))
        img_tk = ImageTk.PhotoImage(img)
        label_image.config(image=img_tk)
        label_image.image = img_tk
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        if image_num == 1:
            img1_cv = img_cv
        else:
            img2_cv = img_cv

def boyut_esitle(img1, img2):
    h2, w2 = img2.shape[:2]
    h1, w1 = img1.shape[:2]

    # Yatay ve dikey oranları hesapla
    height_ratio = h2 / h1
    width_ratio = w2 / w1

    # Her iki oranı kullanarak yeniden boyutlandırma
    resized_img = np.zeros((h2, w2, 3), dtype=np.uint8)

    for i in range(h2):
        for j in range(w2):
            # Orantılı olarak kaynak görüntüden piksel al
            orig_i = int(i / height_ratio)
            orig_j = int(j / width_ratio)

            # Sınır kontrolü yaparak piksel atamasını gerçekleştir
            if orig_i < h1 and orig_j < w1:
                resized_img[i, j] = img1[orig_i, orig_j]

    return resized_img, img2

def resimleri_topla():
    if img1_cv is not None and img2_cv is not None:
        img1_resized, img2_resized = boyut_esitle(img1_cv, img2_cv)
        result = cv2.add(img1_resized, img2_resized)
        show_result(result, label_result_sum)

def resimleri_cikar():
    if img1_cv is not None and img2_cv is not None:
        img1_resized, img2_resized = boyut_esitle(img1_cv, img2_cv)
        result = cv2.subtract(img1_resized, img2_resized)
        show_result(result, label_result_diff)

def show_result(result_img, label_result):
    result_img_pil = Image.fromarray(cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB))
    result_img_pil.thumbnail((150, 150))
    result_img_tk = ImageTk.PhotoImage(result_img_pil)
    label_result.config(image=result_img_tk)
    label_result.image = result_img_tk

# Tüm elemanları yan yana diziyoruz
buton1 = tk.Button(form, text="Resim 1 Seç", command=lambda: resim_sec(label_image1, 1))
buton1.grid(row=0, column=0, padx=10, pady=10)

buton2 = tk.Button(form, text="Resim 2 Seç", command=lambda: resim_sec(label_image2, 2))
buton2.grid(row=0, column=1, padx=10, pady=10)

buton_topla = tk.Button(form, text="Topla", command=resimleri_topla)
buton_topla.grid(row=0, column=2, padx=10, pady=10)

buton_cikar = tk.Button(form, text="Çıkar", command=resimleri_cikar)
buton_cikar.grid(row=0, column=3, padx=10, pady=10)

label_image1 = tk.Label(form)
label_image1.grid(row=0, column=4, padx=10, pady=10)

label_image2 = tk.Label(form)
label_image2.grid(row=0, column=5, padx=10, pady=10)

label_result_sum = tk.Label(form, text="Toplama Sonucu")
label_result_sum.grid(row=0, column=6, padx=10, pady=10)

label_result_diff = tk.Label(form, text="Çıkarma Sonucu")
label_result_diff.grid(row=0, column=7, padx=10, pady=10)

# Programın ekrana gelmesi için mainloop() fonksiyonu
form.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import threading

class GammaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gamma Ayarı Uygulaması")
        self.root.geometry("800x600")
        self.root.configure(bg="#2C2C2C")
        self.root.resizable(False, False)  # Pencere boyutunu sabitle

        # Başlık Etiketi
        title = tk.Label(root, text="Gamma Ayarı Uygulaması", font=("Arial", 20, "bold"), bg="#2C2C2C", fg="#FFFFFF")
        title.pack(pady=10)
        
        # Buton Çerçevesi
        button_frame = tk.Frame(root, bg="#2C2C2C")
        button_frame.pack(pady=10)
        
        # Resim Yükleme Butonu
        load_button = tk.Button(button_frame, text="Resim Yükle", font=("Arial", 12), command=self.load_image, bg="#5A5A5A", fg="white", padx=10, pady=5)
        load_button.grid(row=0, column=0, padx=10)
        
        # Gamma Artırma Butonu
        increase_button = tk.Button(button_frame, text="Gamma Artır", font=("Arial", 12), command=lambda: self.run_in_thread(self.adjust_gamma, 1.5), bg="#5A5A5A", fg="white", padx=10, pady=5)
        increase_button.grid(row=0, column=1, padx=10)
        
        # Gamma Azaltma Butonu
        decrease_button = tk.Button(button_frame, text="Gamma Azalt", font=("Arial", 12), command=lambda: self.run_in_thread(self.adjust_gamma, 0.5), bg="#5A5A5A", fg="white", padx=10, pady=5)
        decrease_button.grid(row=0, column=2, padx=10)

        # Yükleniyor etiketi
        self.loading_label = tk.Label(root, text="", font=("Arial", 12), bg="#2C2C2C", fg="white")
        self.loading_label.pack(pady=10)

        # Görüntü alanı
        self.image_label = tk.Label(root, bg="#2C2C2C")
        self.image_label.pack(pady=20)

        # OpenCV görüntüsü için değişken
        self.cv_image = None

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if file_path:
            try:
                # Dosyayı binary modunda aç ve OpenCV formatına dönüştür
                with open(file_path, 'rb') as file:
                    file_bytes = bytearray(file.read())
                    np_arr = np.asarray(file_bytes, dtype=np.uint8)
                    self.cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

                if self.cv_image is not None:
                    self.display_image(self.cv_image)
                else:
                    messagebox.showerror("Hata", "Görüntü dosyası açılamadı.")
            except Exception as e:
                messagebox.showerror("Hata", f"Görüntü dosyası yüklenemedi: {e}")
        else:
            messagebox.showwarning("Uyarı", "Resim yüklenemedi.")

    def display_image(self, cv_img):
        # Görüntüyü oranını koruyarak yeniden boyutlandır
        max_width, max_height = 600, 400
        height, width = cv_img.shape[:2]
        scale = min(max_width / width, max_height / height)
        new_size = (int(width * scale), int(height * scale))
        resized_img = cv2.resize(cv_img, new_size)

        # BGR'den RGB'ye dönüştür
        rgb_image = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
        
        # OpenCV görüntüsünü PIL görüntüsüne dönüştür ve Tkinter'de göster
        pil_image = Image.fromarray(rgb_image)
        tk_image = ImageTk.PhotoImage(pil_image)
        
        self.image_label.configure(image=tk_image)
        self.image_label.image = tk_image
        self.loading_label.config(text="")  # İşlem tamamlanınca "Yükleniyor..." yazısını temizle

    def run_in_thread(self, func, gamma):
        # "Yükleniyor..." mesajını göster
        self.loading_label.config(text="Yükleniyor...")
        
        # İş parçacığını başlat
        thread = threading.Thread(target=func, args=(gamma,))
        thread.start()

    def adjust_gamma(self, gamma):
        if self.cv_image is not None:
            # Yeni bir görüntü oluştur (aynı boyutlarda ve aynı veri türünde)
            height, width, channels = self.cv_image.shape
            adjusted_gamma = np.zeros((height, width, channels), dtype=np.uint8)

            # Her piksel üzerinde gamma işlemini uygula
            for r in range(height):
                for c in range(width):
                    for k in range(channels):
                        # Gamma ayarını uygula: J(r, c) = 255 * [(I(r, c) / 255)^(1/gamma)]
                        normalized_pixel = self.cv_image[r, c, k] / 255.0
                        adjusted_pixel = 255 * (normalized_pixel ** (1 / gamma))
                        adjusted_gamma[r, c, k] = int(adjusted_pixel)

            self.display_image(adjusted_gamma)
        else:
            messagebox.showwarning("Uyarı", "Önce bir resim yükleyin.")

# Tkinter Uygulaması Başlat
root = tk.Tk()
app = GammaApp(root)
root.mainloop()

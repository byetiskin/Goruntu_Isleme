import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading

class HistogramApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Histogram Görüntüleme Uygulaması")
        self.root.geometry("800x600")
        self.root.configure(bg="#2C2C2C")
        self.root.resizable(False, False)
        
        # Başlık Etiketi
        title = tk.Label(root, text="Histogram Görüntüleme Uygulaması", font=("Arial", 20, "bold"), bg="#2C2C2C", fg="#FFFFFF")
        title.pack(pady=10)
        
        # Buton Çerçevesi
        button_frame = tk.Frame(root, bg="#2C2C2C")
        button_frame.pack(pady=10)
        
        # Resim Yükleme Butonu
        load_button = tk.Button(button_frame, text="Resim Yükle", font=("Arial", 12), command=self.load_image, bg="#5A5A5A", fg="white", padx=10, pady=5)
        load_button.grid(row=0, column=0, padx=10)
        
        # Gri Histogram Butonu
        gray_button = tk.Button(button_frame, text="Gri Histogram", font=("Arial", 12), command=lambda: self.run_in_thread(self.show_histogram, "gray"), bg="#5A5A5A", fg="white", padx=10, pady=5)
        gray_button.grid(row=0, column=1, padx=10)
        
        # Kırmızı Histogram Butonu
        red_button = tk.Button(button_frame, text="Kırmızı Histogram", font=("Arial", 12), command=lambda: self.run_in_thread(self.show_histogram, "red"), bg="#5A5A5A", fg="white", padx=10, pady=5)
        red_button.grid(row=0, column=2, padx=10)
        
        # Yeşil Histogram Butonu
        green_button = tk.Button(button_frame, text="Yeşil Histogram", font=("Arial", 12), command=lambda: self.run_in_thread(self.show_histogram, "green"), bg="#5A5A5A", fg="white", padx=10, pady=5)
        green_button.grid(row=0, column=3, padx=10)
        
        # Mavi Histogram Butonu
        blue_button = tk.Button(button_frame, text="Mavi Histogram", font=("Arial", 12), command=lambda: self.run_in_thread(self.show_histogram, "blue"), bg="#5A5A5A", fg="white", padx=10, pady=5)
        blue_button.grid(row=0, column=4, padx=10)

        # Görüntü veya histogram alanı
        self.display_frame = tk.Frame(root, bg="#2C2C2C")
        self.display_frame.pack(pady=20)

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
        # Önceki histogram veya görüntüyü temizle
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        # Görüntüyü oranını koruyarak yeniden boyutlandır
        max_width, max_height = 600, 450
        height, width = cv_img.shape[:2]
        scale = min(max_width / width, max_height / height)
        new_size = (int(width * scale), int(height * scale))
        resized_img = cv2.resize(cv_img, new_size)

        # BGR'den RGB'ye dönüştür
        rgb_image = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
        
        # OpenCV görüntüsünü PIL görüntüsüne dönüştür ve Tkinter'de göster
        pil_image = Image.fromarray(rgb_image)
        tk_image = ImageTk.PhotoImage(pil_image)
        
        image_label = tk.Label(self.display_frame, image=tk_image, bg="#2C2C2C")
        image_label.image = tk_image
        image_label.pack()

    def run_in_thread(self, func, *args):
        # İş parçacığını başlat
        thread = threading.Thread(target=func, args=args)
        thread.start()

    def show_histogram(self, channel):
        if self.cv_image is not None:
            if channel == "gray":
                gray_image = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2GRAY)
                histogram = self.calculate_histogram(gray_image)
                self.plot_histogram(histogram, "Grayscale Histogram", "black")
            elif channel == "red":
                histogram = self.calculate_histogram(self.cv_image[:, :, 2])  # Kırmızı kanal
                self.plot_histogram(histogram, "Red Channel Histogram", "red")
            elif channel == "green":
                histogram = self.calculate_histogram(self.cv_image[:, :, 1])  # Yeşil kanal
                self.plot_histogram(histogram, "Green Channel Histogram", "green")
            elif channel == "blue":
                histogram = self.calculate_histogram(self.cv_image[:, :, 0])  # Mavi kanal
                self.plot_histogram(histogram, "Blue Channel Histogram", "blue")
        else:
            messagebox.showwarning("Uyarı", "Önce bir resim yükleyin.")

    def calculate_histogram(self, image_channel):
        histogram = [0] * 256
        for value in image_channel.ravel():
            histogram[value] += 1
        return histogram

    def plot_histogram(self, histogram, title, color):
        # Önceki içerikleri temizle
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        # Yeni bir Figure ve Canvas oluştur
        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(histogram, color=color)
        ax.set_title(title)
        ax.set_xlabel('Pixel Value')
        ax.set_ylabel('Frequency')
        ax.set_xlim([0, 255])

        canvas = FigureCanvasTkAgg(fig, master=self.display_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

# Tkinter Uygulaması Başlat
root = tk.Tk()
app = HistogramApp(root)
root.mainloop()

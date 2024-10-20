import tkinter as tk

# Modüldeki fonksiyonları kullanabilmek için Tk() sınıfından bir nesne oluşturuyoruz
form = tk.Tk()

# Pencere ismi
form.title("Görüntü İşleme Dersi")

# Pencere boyutu
form.geometry("500x500")

# Pencerenin ekrandaki konumunu ayarlamak istersek
#form.geometry("500x500+800+200")

# Pencere üzerinde yazı yazdıralım
# .pack() metodu, etiketi pencere içinde görüntüler
label1 = tk.Label(form, text = "Masaüstü Uygulaması Yapalım.").pack()
label2 = tk.Label(form, text = "İlk Uygulama", fg = "blue").pack() # fg = foreground (yazı rengi)
label3 = tk.Label(form, text = "Begüm YETİŞKİN", fg = "white", bg = "red").pack() # bg = background (arka plan rengi)
label4 = tk.Label(form, text = "İtalik Yazı", font = ("Arial", 20, "italic")).pack() # font = yazı tipi

def yazdir():
    print("çalıştı")

# Pencere üzerinde buton
buton1 = tk.Button(form, text = "Tıkla", bg = "yellow", command = yazdir).pack(side=tk.RIGHT)   # command = butona tıklanınca metot çağırıyor
buton2 = tk.Button(form, text = "Tıkla", bg = "purple", command = yazdir).pack(side=tk.RIGHT)   # command = butona tıklanınca metot çağırıyor

giris = tk.Entry(bg = "#995567")
giris.pack()

def veriAl():
    label5["text"] = giris.get()
    
# Klavyeden veri almak için
buton3 = tk.Button(form, text = "Gönder", command = veriAl).pack() 
label5 = tk.Label(text = "Verinin buraya gelmesi lazım")
label5.pack() # font = yazı tipi


# Programın ekrana gelmesi için kodun sonunda mutlaka mainloop() yazılmalı
form.mainloop()
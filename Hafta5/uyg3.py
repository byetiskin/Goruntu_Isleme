import tkinter as tk

form = tk.Tk()

form.title("Görüntü İşleme Dersi")
form.geometry("400x400+500+200")


sayi1 = tk.Label(
    form,
    text="5", 
    font=("Arial", 40),
    bg="#995734",
    fg="white"
)
sayi1.grid(row=0, column=1, padx=10, pady=10)


sayi2 = tk.Label(
    form,
    text="7", 
    font=("Arial", 40),
    bg="#995734",
    fg="white"
)
sayi2.grid(row=0, column=2, padx=10, pady=10)

sonuc = tk.Label(
    form,
    text="Sonuç: ", 
    font=("Arial", 40),
    bg="#995734",
    fg="white"
)
sonuc.grid(row=1, column=1, columnspan=2, pady=20)

def topla():
    num1 = int(sayi1.cget("text"))
    num2 = int(sayi2.cget("text"))
    toplam = num1 + num2
   # sonuc["text"] = f"Sonuç: {toplam}"
    sonuc.config(text = f"Sonuç: {toplam}")

buton = tk.Button(
    form,
    text="Tıkla",
    font=("Arial", 30),
    bg="#995734",
    fg="white",
    command=topla  
)
buton.grid(row=2, column=1, columnspan=2, pady=20)

form.mainloop()

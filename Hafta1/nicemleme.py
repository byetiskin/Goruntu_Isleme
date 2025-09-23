import numpy as np

# Orijinal 3x3 matris
I = np.array([[12, 10,  9],
              [11,200,201],
              [12,205,198]])

# 3 bit nicemleme
levels = 8   # 2^3
delta = 255 / (levels - 1)
I_q = (np.round(I / delta) * delta).astype(int)

# Hata matrisi
H = I - I_q

# En büyük fark (l∞ normu)
max_error = np.max(np.abs(H))

# Ortalama kare hata (MSE)
MSE = np.mean(H**2)

print("Orijinal:\n", I)
print("3-bit Nicemlenmiş:\n", I_q)
print("Hata Matrisi (I - I_q):\n", H)
print("Delta:", delta)
print("En büyük fark (l∞):", max_error)
print("MSE:", MSE)

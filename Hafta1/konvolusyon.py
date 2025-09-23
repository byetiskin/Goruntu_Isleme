import numpy as np
from scipy.signal import convolve2d

# Görüntü matrisi
I = np.array([
    [10, 10, 10, 10],
    [10, 50, 50, 10],
    [10, 50, 50, 10],
    [10, 10, 10, 10]
])

# 2D filtre
K = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

# ---- Yöntem 1: Normal 2D konvolüsyon ----
out_2d = convolve2d(I, K, mode='same', boundary='fill', fillvalue=0)

# ---- Yöntem 2: Ayrıştırılmış 1D + 1D ----
h = np.array([[-1, 0, 1]])   # yatay filtre
v = np.array([[1], [1], [1]])  # dikey filtre

# önce yatay
out_h = convolve2d(I, h, mode='same', boundary='fill', fillvalue=0)
# sonra dikey
out_sep = convolve2d(out_h, v, mode='same', boundary='fill', fillvalue=0)

print("Orijinal Görüntü:\n", I)
print("\n2D Konvolüsyon Sonucu:\n", out_2d)
print("\nAyrıştırılmış (1D + 1D) Sonucu:\n", out_sep)
print("\nFark:\n", out_2d - out_sep)

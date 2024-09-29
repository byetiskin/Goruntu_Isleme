# Temel Matris İşlemleri

import numpy as np

# A ve B matrislerini tanımlıyoruz
A = np.array([[1, -2], [3, 2]])
B = np.array([[1, 2, 4], [1, 3, 1]])

# Matrisleri yazdırıyoruz
print("A matrisi:\n", A)
print("B matrisi:\n", B)

# Matris çarpımını gerçekleştiriyoruz
C = np.dot(A, B)

# Sonucu ekrana yazdırıyoruz
print("A ve B matrislerinin çarpımı:\n", C)

# -------------------------------------------------
# D matrisini tanımlıyoruz
D = np.array([[1], [2], [3], [4]])

# D matrisini yazdırıyoruz
print("D matrisi:\n", D)

# D matrisinin transpozunu alıyoruz
D_transpose = D.T

# Sonucu ekrana yazdırıyoruz
print("D matrisinin transpozu:\n", D_transpose)

# E matrisi tanımlıyoruz
E = np.array([[10], [20], [30], [40]])

# E matrisini yazdırıyoruz
print("E matrisi:\n", E)

#D matrisinin transpozu ile E matrisini çarpıyoruz
F = np.dot(D_transpose, E)

# Sonucu ekrana yazdırıyoruz
print("F matrisi:\n", F)

# -------------------------------------------------

# İki vektör oluşturuyoruz
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Vektörleri yazdırıyoruz
print("v1 vektörü:\n", v1)
print("v2 vektörü:\n", v2)

# Vektörlerin toplama işlemi
toplam = v1 + v2

# Vektörlerin çıkarma işlemi
cikarma = v1 - v2

# Vektörlerin çarpma işlemi (eleman bazlı çarpma)
carpma = v1 * v2

# Vektörlerin bölme işlemi (eleman bazlı bölme)
bolme = v1 / v2

# Sonuçları ekrana yazdırıyoruz
print("Toplama:\n", toplam)
print("Çıkarma:\n", cikarma)
print("Çarpma:\n", carpma)
print("Bölme:\n", bolme)
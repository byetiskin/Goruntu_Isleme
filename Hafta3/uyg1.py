import numpy as np

# -----------------------------
# 1. PARAMETRELER
# -----------------------------
size = 3       # Filtre boyutu (örneğin 3x3). 3 elemanlı bir Gauss çekirdeği oluşturacağız.
sigma = 1.0    # Standart sapma (σ): Dağılımın genişliğini belirler.
               # Sigma küçük olursa dağılım dar olur (keskin), büyük olursa yayılır (daha yumuşak blur etkisi).

# -----------------------------
# 2. 1 BOYUTLU GAUSS FİLTRESİ (FORMÜLDEN HESAPLAMA)
# -----------------------------
# x değerleri, maskenin merkezine göre konumları gösterir.
# Örneğin 3x3 filtrede merkez piksel 0’dır, bir solundaki -1, bir sağındaki +1’dir.
# 5x5 filtre olsaydı x = [-2, -1, 0, 1, 2] olurdu.
half = size // 2
x = np.arange(-half, half + 1)  # [-1, 0, 1]
print("x değerleri:", x)

# 1B Gauss fonksiyonu:
# G(x) = e^{-(x^2) / (2σ^2)}
# Bu denklem, merkeze yakın piksellere yüksek ağırlık, uzaklara düşük ağırlık verir.
g1d = np.exp(-(x**2) / (2 * sigma**2))

# Toplam 1 olmalı ki görüntünün genel parlaklığı değişmesin.
# Bu yüzden tüm değerleri toplamına bölerek normalize ederiz.
g1d = g1d / np.sum(g1d)
print("\n1B Gauss filtresi:\n", g1d)

# -----------------------------
# 3. 2 BOYUTLU GAUSS FİLTRESİ OLUŞTURMA
# -----------------------------
# 2B Gauss filtresi, 1B Gauss’un hem x hem y yönünde çarpımıyla elde edilir.
# Yani G(x, y) = Gx(x) * Gy(y)
# Bu işlemi np.outer() fonksiyonu (dış çarpım) ile yapıyoruz.
g2d = np.outer(g1d, g1d)

# Tekrar normalize ediyoruz (küçük yuvarlama farkları için güvenli olur)
g2d = g2d / np.sum(g2d)
print("\n2B Gauss filtresi:\n", g2d)

# -----------------------------
# 4. AÇIKLAMA ÖZETİ
# -----------------------------
# σ (sigma): Filtrenin yayılma miktarını belirler.
# x: Filtredeki konum değerleridir. Merkez 0, kenarlar negatif/pozitif olur.
# normalize: Filtrenin toplamını 1 yapar, böylece parlaklık korunur.

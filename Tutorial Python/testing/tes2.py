def luas_trapesium(x1, y1, x2, y2):
    """
    Menghitung luas trapesium.

    Parameters:
    - x1 (float): Koordinat x titik pertama.
    - y1 (float): Koordinat y titik pertama.
    - x2 (float): Koordinat x titik kedua.
    - y2 (float): Koordinat y titik kedua.

    Returns:
    - float: Luas trapesium.
    """
    luas = 0.5 * (y1 + y2) * (x2 - x1)
    return luas

# Data dari tabel kedua
data_tanah = [(0, 125), (100, 125), (200, 120), (300, 112), (400, 90), (500, 90), (600, 95), (700, 88), (800, 75), (900, 35), (1000, 0)]

# Inisialisasi luas total
luas_total = 0

# Menghitung luas setiap trapesium
for i in range(len(data_tanah) - 1):
    x1, y1 = data_tanah[i]
    x2, y2 = data_tanah[i + 1]
    luas_total += luas_trapesium(x1, y1, x2, y2)

# Menampilkan hasil perhitungan luas tanah
print(f'Luas total tanah adalah {luas_total} meter persegi.')

def interpolasi_linear(x, x1, y1, x2, y2):
    """
    Menghitung nilai interpolasi linear.

    Parameters:
    - x (float): Nilai x yang ingin diinterpolasi.
    - x1 (float): Titik x pertama.
    - y1 (float): Titik y pertama.
    - x2 (float): Titik x kedua.
    - y2 (float): Titik y kedua.

    Returns:
    - float: Nilai interpolasi linear pada x.
    """
    y = y1 + (x - x1) * ((y2 - y1) / (x2 - x1))
    return y

# Data dari tabel pertama
data = [(10, 0), (30, 40), (50, 80), (70, 120), (90, 160)]

# Nilai X yang ingin diinterpolasi
x_interpolasi = 60

# Mencari interval yang sesuai
for i in range(len(data) - 1):
    if data[i][0] <= x_interpolasi <= data[i + 1][0]:
        x1, y1 = data[i]
        x2, y2 = data[i + 1]
        break

# Menghitung nilai Y dengan interpolasi linear
y_interpolasi = interpolasi_linear(x_interpolasi, x1, y1, x2, y2)

# Menampilkan hasil interpolasi
print(f'Interpolasi linear pada X = {x_interpolasi} adalah Y = {y_interpolasi}')


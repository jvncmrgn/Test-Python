# Data
x1, y1 = 9.0, 2.1972
x2, y2 = 9.5, 2.2513
x_interpolate = 9.2

# Interpolasi linier
y_interpolate = y1 + (x_interpolate - x1) * (y2 - y1) / (x2 - x1)

# Menampilkan hasil interpolasi
print(f'Interpolasi ln(9.2): {y_interpolate:.4f}')

# Nilai sejati ln(9.2)
true_value = 2.2192

# Menghitung kesalahan interpolasi
error = abs(true_value - y_interpolate)

# Menampilkan hasil perbandingan dengan nilai sejati
print(f'Nilai sejati ln(9.2): {true_value}')
print(f'Perbandingan Nilai Intepolasi Linier(9.2) dan Nilai Sejati ln(9.2) = {y_interpolate:.4f} & {true_value}')

print(f'Kesalahan interpolasi: {error:.4f}')

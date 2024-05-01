def f(x):
    return 4 * x - x**2

def simpsons_rule(a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    integral_approximation = h / 3 * (y[0] + 4 * sum(y[i] for i in range(1, n, 2)) + 2 * sum(y[i] for i in range(2, n - 1, 2)) + y[n])
    return integral_approximation

# Batas integrasi
a = 0
b = 1

# Jumlah segmen (2 segmen)
n = 2

# Menghitung integral menggunakan aturan Simpson
approximation = simpsons_rule(a, b, n)

# Menghitung fungsi asli (integral sebenarnya)
def true_integral(x):
    return 2 * x**2 - (x**3) / 3

true_value = true_integral(b) - true_integral(a)

# Menghitung kesalahan perhitungan
error = abs(true_value - approximation)

# Menampilkan hasil
print(f'Pendekatan integral dengan aturan Simpson (2 segmen): {approximation}')
print(f'Nilai sebenarnya integral: {true_value}')
print(f'Kesalahan perhitungan: {error}')

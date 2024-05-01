import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Data pengukuran
strain = np.array([0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50])
stress = np.array([0.000, 0.252, 0.531, 0.840, 1.184, 1.558, 1.975, 2.444, 2.943, 3.500, 4.115])

# Regresi linear
slope, intercept, r_value, p_value, std_err = linregress(strain, stress)

# Persamaan regresi linear: σ = a + bε
a = intercept
b = slope

# Koefisien korelasi (ρ)
rho = r_value

# Membuat gambar dan subplot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# Plotting data pengukuran dan regresi linear di subplot pertama
ax1.scatter(strain, stress, label='Pengukuran')
regression_line = a + b * strain
ax1.plot(strain, regression_line, label=f'Regresi Linear\nσ = {a:.3f} + {b:.3f}ε\nρ = {rho:.3f}', color='red')
ax1.set_xlabel('Strain')
ax1.set_ylabel('Stress')
ax1.set_title('Stress vs Strain with Linear Regression')
ax1.legend()

# Plotting hanya data pengukuran di subplot kedua
ax2.scatter(strain, stress, label='Pengukuran')
ax2.set_xlabel('Strain')
ax2.set_ylabel('Stress')
ax2.set_title('Stress vs Strain - Pengukuran')
ax2.legend()

# Menampilkan plot
plt.tight_layout()
plt.show()

# Menampilkan nilai a, b, dan ρ
print(f'Nilai a: {a:.3f}')
print(f'Nilai b: {b:.3f}')
print(f'Koefisien Korelasi (ρ): {rho:.3f}')

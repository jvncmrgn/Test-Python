import numpy as np
import matplotlib.pyplot as plt

# Persamaan
def omega(v, psi, k):
    return v * psi * k

# Membuat array v, psi, dan k
v = np.linspace(0, 10, 100)  # Ganti dengan rentang yang sesuai
psi = np.linspace(0, 10, 100)  # Ganti dengan rentang yang sesuai
k = np.linspace(0, 10, 100)  # Ganti dengan rentang yang sesuai

# Menghasilkan grid v, psi, dan k
v, psi, k = np.meshgrid(v, psi, k)

# Menghitung omega
w = omega(v, psi, k)

# Membuat plot 3D
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(v, psi, w, cmap='viridis')

# Menambahkan label sumbu
ax.set_xlabel('v')
ax.set_ylabel('psi')
ax.set_zlabel('omega')

# Menampilkan plot
plt.show()
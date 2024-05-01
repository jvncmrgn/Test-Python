import pandas as pd

# Membaca file CSV
df = pd.read_csv(r'C:\Users\jovan\OneDrive\Documents\Vs Code\Python VSCODE\Bangkit\Capstone\Data\nutrition.csv')

# Menangani nilai-nilai yang hilang (NaN)
df = df.dropna()

# Menghapus duplikat baris
df = df.drop_duplicates()

# Menyimpan hasil kembali ke file CSV
df.to_csv('file_benar.csv', index=False)

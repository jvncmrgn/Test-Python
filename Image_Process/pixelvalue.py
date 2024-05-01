# from PIL import Image

# # Buka gambar
# img = Image.open("gambar1.jpg")

# # Ambil nilai pixel di koordinat (x,y)
# pixel_value = img.getpixel((20,30))

# # Cetak nilai pixel
# print(pixel_value)

import cv2

# Load citra grayscale
img = cv2.imread('harimau-malaya.png', cv2.IMREAD_GRAYSCALE)

# Batas jumlah pixel yang dicari nilainya
limit = 100

# Variabel counter untuk menghitung jumlah pixel yang sudah dicari nilainya
counter = 0

# Menampilkan nilai piksel dari setiap baris dan kolom pada citra
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        print("Nilai piksel pada baris ", i, " kolom ", j, ": ", img[i, j])

 # Menambah counter
        counter += 1

        # Kondisi untuk berhenti saat jumlah pixel sudah mencapai limit
        if counter >= limit:
            break
    if counter >= limit:
        break
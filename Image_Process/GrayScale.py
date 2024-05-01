import cv2
import numpy as np
import os

# Mendefinisikan direktori gambar
dir_path = 'Image/gambar/'

# Mengambil semua nama file gambar dalam direktori
img_files = [f for f in os.listdir(dir_path) if f.endswith('.jpg')]

# Looping untuk membaca semua gambar dan menampilkannya
for f in img_files:
    # Membaca gambar
    img = cv2.imread(os.path.join(dir_path, f), 0)
    # Menampilkan gambar
    cv2.imshow('Citra ' + f, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# # Tunggu input dari keyboard
# # Tutup semua jendela
# cv2.destroyAllWindows()


# image = cv2.imread('Image/gambar/PCT1.jpg')
# # bisa juga langsung imread('Image/gambar/PCT1.jpg', 0)

# #Konversi ke grayscale
# img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Gambar Asli', image)
# cv2.imshow('GrayScale', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
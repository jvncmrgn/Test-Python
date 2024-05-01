import cv2
import numpy as np

# Load citra
img = cv2.imread('Image/gambar/PCT7.jpg', cv2.IMREAD_GRAYSCALE)

# Deteksi tepi menggunakan operator Canny
canny = cv2.Canny(img, 100, 200)

# # Tampilkan citra
cv2.imshow('Gambar Asli', img)
cv2.imshow('Deteksi Tepi Canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

# Load citra
img = cv2.imread('Image/gambar/PCT8.jpg', cv2.IMREAD_GRAYSCALE)

# Blurring menggunakan filter Gaussian
blur = cv2.GaussianBlur(img, (5, 5), 0)

# Deteksi tepi menggunakan operator Laplacian
laplacian = cv2.Laplacian(blur, cv2.CV_64F)

# Konversi hasil deteksi ke citra uint8
laplacian = np.uint8(np.absolute(laplacian))

# Tampilkan citra
cv2.imshow('Citra Asli', img)
cv2.imshow('Deteksi Tepi Gaussian', laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()

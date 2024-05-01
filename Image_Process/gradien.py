import cv2
import numpy as np

# Load gambar
img = cv2.imread('Image/gambar/PCT2.jpg', cv2.IMREAD_GRAYSCALE)

# Hitung gradien menggunakan filter Sobel
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Gabungkan hasil gradien
grad = np.sqrt(sobelx*2 + sobely*2)

# Tampilkan gambar dan hasil gradien
cv2.imshow('Gambar Asli', img)
cv2.imshow('Gradien', grad)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# Konversi Gambar langsung ke Grayscale
img = cv2.imread('Image/PCT6.jpg', cv2.IMREAD_GRAYSCALE)

# Deteksi tepi menggunakan operator Sobel
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
# Gabungkan hasil Sobel x dan y
sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# Deteksi tepi menggunakan operator Canny
canny = cv2.Canny(img, 100, 200)

# Deteksi tepi menggunakan operator Gaussian
gaussian = cv2.GaussianBlur(img, (5,5), 0)

# Hasil
cv2.imshow('Gambar Asli', img)
cv2.imshow('Deteksi Tepi Sobel', sobel)
cv2.imshow('Deteksi Tepi Canny', canny)
cv2.imshow('Deteksi Tepi Gaussian', gaussian)

cv2.waitKey()
cv2.destroyAllWindows()
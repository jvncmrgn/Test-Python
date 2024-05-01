import cv2

img1 = cv2.imread('Image/PCT1.jpg')
img2 = cv2.imread('Image/PCT2.jpg')

# Operasi Pertambahan
add = cv2.add(img1, img2)

# Operasi Pengurangan
sub = cv2.subtract(img1, img2)

# Operasi Perkalian
multi = cv2.multiply(img1, img2)

# Operasi Pembagian
div = cv2.divide(img1, img2)

# Hasil
cv2.imshow('Gambar 1', img1)
cv2.imshow('Gambar 2', img2)
cv2.imshow('Add', add)
cv2.imshow('Subtract', sub)
cv2.imshow('Multiply', multi)
cv2.imshow('Divide', div)

cv2.waitKey(0)
cv2.destroyAllWindows()
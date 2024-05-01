import cv2
import numpy as np

img = cv2.imread('Image/PCT5.jpg')

# Ambil nilai tinggi dan lebar
height, width = img.shape[:2]

# Tranlasi citra
x = np.float32([[1,0,100],[0,1,50]])
translasi = cv2.warpAffine(img, x, (height,width))

# Rotasi Gambar
x = cv2.getRotationMatrix2D((height/2,width/2), 45, 1)
rotasi = cv2.warpAffine(img, x, (height, width))

# Flip Horizontal
flip_hrz = cv2.flip(img, 1)

# Flip Vertikal
flip_vrt = cv2.flip(img, 0)

# Mengecil
down_width = 300
down_height = 200
down_points = (down_width, down_height)
mengecil = cv2.resize(img, down_points, interpolation= cv2.INTER_LINEAR)

# Membesar
up_width = 600
up_height = 400
up_points = (up_width, up_height)
membesar = cv2.resize(img, up_points, interpolation= cv2.INTER_LINEAR)

# Hasil
cv2.imshow('Gambar Asli', img)
cv2.imshow('Translasi', translasi)
cv2.imshow('Rotasi', rotasi)
cv2.imshow('Flip', flip_hrz)
cv2.imshow('Flip', flip_vrt)
cv2.imshow('Mengecil', mengecil)
cv2.imshow('Membesar', membesar)

cv2.waitKey()
cv2.destroyAllWindows()
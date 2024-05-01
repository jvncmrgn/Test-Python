import cv2
import numpy as np

img1 = cv2.imread('Image/PCT3.jpg')
img2 = cv2.imread('Image/PCT4.jpg')

# Operasi boolean AND
result_and = cv2.bitwise_and(img1, img2)

# Operasi boolean OR
result_or = cv2.bitwise_or(img1, img2)

# Operasi boolean NOT
result_not = cv2.bitwise_not(img1, img2)

# Operasi boolean XOR
result_xor = cv2.bitwise_xor(img1, img2)

# Hasil
cv2.imshow('Gambar 1', img1)
cv2.imshow('Gambar 2', img2)
cv2.imshow('AND', result_and)
cv2.imshow('OR', result_or)
cv2.imshow('NOT', result_not)
cv2.imshow('XOR', result_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()
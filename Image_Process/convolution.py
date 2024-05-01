import cv2
import numpy as np

# membaca citra grayscale
img = cv2.imread('Image/PCT8.jpg', 0)

# membuat filter
filter = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
])

# melakukan konvolusi
result = cv2.filter2D(img, -1, filter)

# menampilkan hasil
cv2.imshow('Original Image', img)
cv2.imshow('Result Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
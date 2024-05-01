import cv2

image = cv2.imread('Image/PCT1.jpg')

# Konversi ke grayscale
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# bisa juga langsung imread('Image/gambar/PCT1.jpg', 0)

# Threshold Binary
pxl, threshBi = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
# Threshold Truncate
pxl, threshTr = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
# Threshold to Zero
pxl, thresh0 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)

# Image Brightening
bright_img = cv2.add(img, 100)

# Hasil
cv2.imshow('Gambar Asli', image)
cv2.imshow('Threshold Binary', threshBi)
cv2.imshow('Threshold Truncated', threshTr)
cv2.imshow('Threshold to Zero', thresh0)
cv2.imshow('Grayscale', img)
cv2.imshow('Image Brightening', bright_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
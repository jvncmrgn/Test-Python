import cv2

img = cv2.imread("Image/Gambar/PCT1.jpg")

image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Mencerahkan
bright_img = cv2.add(image, 100)

# Menggelapkan
dark_img = cv2.subtract(image, 50)

# Display the results
cv2.imshow('Input image', img)
cv2.imshow('Brightened image', bright_img)
cv2.imshow('Darkened image', dark_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
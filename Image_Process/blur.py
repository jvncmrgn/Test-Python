from PIL import Image, ImageFilter, ImageOps

# Load the image
img = Image.open("Image/gambar/PCT1.jpg")
iclmg = ImageOps.exif_transpose(img)

# Apply Gaussian blur with radius 2
blur = iclmg.filter(ImageFilter.GaussianBlur(radius=10))

# Save the blurred image
blur.save("BlurredImage.jpg")

# Show the original and blurred images
img.show()
blur.show()

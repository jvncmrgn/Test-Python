from PIL import Image, ImageOps
img  = Image.open("harimau-malaya.png")
# iclmg = ImageOps.exif_transpose(img)
img.show()
print(img.histogram())

# img2 = Image.open("harimau-malaya.png") 
# img.paste(img2, (100, 100))

# filename = "gambar1.jpg"
# with Image.open(filename) as image:
#     width, height = image.size

# Save changes in image
# img.save("gambartempel.jpg")

# format is optional, if no format is specified, 
#it is determined from the filename extension
# On successful execution of this statement,
# an object of Image type is returned and stored in img variable)
   
# try: 
#     img  = Image.open("gambar1.jpg")1
#     img.show() 
# except IOError:
#     pass
# Use the above statement within try block, as it can 
# raise an IOError if fiadaadale cannot be found, 
# or image cannot be opened.

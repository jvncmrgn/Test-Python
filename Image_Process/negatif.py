from PIL import Image, ImageOps

# Buka gambar
img = Image.open("gambar1.jpg")
iclmg = ImageOps.exif_transpose(img)

# Buat gambar negatif
img_negatif = ImageOps.invert(iclmg)

# Simpan gambar
img_negatif.save('negatif.jpg')

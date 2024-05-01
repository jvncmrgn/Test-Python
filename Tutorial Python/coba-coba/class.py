class Hewan:
 def __init__(self, inputNama, inputWarna, inputKaki):
     self.nama = inputNama
     self.warna = inputWarna
     self.kaki = inputKaki

kucing1 = Hewan("catty", "putih", 4)

print(kucing1.nama)
print(kucing1.warna)
print(kucing1.kaki)

print(kucing1.__dict__)
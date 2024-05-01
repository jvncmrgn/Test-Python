#Dari Tabel,
#Buatlah sebuah dictionary/object yang terdiri atas Nama sebagai key dan Aset sebagai value. Aset harus dalam bentuk array/list.
print("\nBagian A")
Aset = ['Rumah', 'Motor', 'Mobil']
Nama = ["Salman", "Iyan", "Karim", "Bowlang", "Adit", "Soqi", "Gatot", "Firly", "Okta", "Nandi"]
dict = {
    'Key' : Nama,
    'Value' : Aset, 
}
print(dict)

#Pecah dictionary sebelumnya menjadi dua buah variabel yaitu Nama dan Aset
print("\nBagian B")
# keys_for_slicing = ["Key", "Value"]
# sliced_dict = {key: dict[key] for key in keys_for_slicing }
# print(sliced_dict)
for i, j in dict.items():
    print(i, j)

#Lakukan Slicing untuk mendapatkan nilai dari index ke 3 – 10 pada variabel Nama
print("\nBagian C")
print(Nama[2:])


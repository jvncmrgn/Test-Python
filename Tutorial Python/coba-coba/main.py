# print("Halo Jovanic!")
# print("saya kuliah di unsri")
# print("Pakailah aku jalan berkat-Mu, Memancarkan cahaya-Mu")
# print("Buatlah aku, saluran berkat, bagi siapa yang risau penat")
# print("Tunjukkan aku jalannya Tuhan")
# variabel1 = 75
# variabel2 = variabel1 * 2
# print(variabel2)
# namaDepan = "Budi"
# namaBelakang = "Susanto"
# nama = namaDepan + " " + namaBelakang
# umur = 22
# hobi = "Berenang"
# print("Biodata\n", nama, "\n", umur, "\n", hobi)

# count = 0
# while (count < 1):
#     print ("The count is: ", count)
#     count = count + 1

# print ("Good bye!")

# angka = [1,2,3,4,5]
# for x in angka:
#     print(x)

# #Contoh pengulangan for
# buah = ["nanas", "apel", "jeruk"]
# for makanan in buah:
#     print ("Saya suka makan", makanan)


# i = 2
# while(i < 100):
#     j = 2
#     while(j <= (i/j)):
#         if not(i%j): break
#         j = j + 1
#     if (j > i/j) : print(i, " is prime")
#     i = i + 1

print("Good bye!")

#Tipe Data List
foo = ["satu","dua","tiga","satu"]
print(foo)
 
#Tipe Data Tuple
foo = ("satu","dua","tiga","satu")
print(foo)
 
#Tipe Data Set
foo = {"satu","dua","tiga","empat"}
print(foo)
 
#Tipe Data Dictionary
foo = {"satu":1, "dua":2.13, "tiga":"a", "empat": True}
print(foo)

foo = "Duniailkom"
print(foo)
bar = 'Duniailkom\nitu\nsunggguh menyenangkan'
print(bar)

foo = 'Belajar '
bar = "Bahasa Pemrograman Python "
baz = "di Dunia\nilkom"
hasil = foo + bar + baz
print(hasil)

foo = 'Duniailkom'
print(foo[0])
print(foo[4])
print(foo[5:10])

foo = 3e2
bar = 3e-2
baz = 1.34E5
  
print(foo)
print(bar)
print(baz)

print(type(foo))
print(type(bar))
print(type(baz))

foo = 12 < 10
print(foo)
foo = 12 > 10
print(foo)
foo = "A" == "a"
print(foo)

a = 12
b = 10
if (a < b):
  print("Isi variabel a lebih kecil daripada variabel b")
elif (a > b):
  print("Isi variabel a lebih besar daripada variabel b")
else:
  print("Isi variabel a sama dengan variabel b")

foo = ["Belajar", "Python", "di", "Duniailkom"]
bar = [100, 200, 300, 400]
baz = ["Python", 200, 6.99, True]
  
print(foo)
print(bar)
print(baz)

foo = ["Python", 200, 6.99, True, 'Duniailkom', 99j]
print(foo[2:5])
print(foo[:3])
print(foo[3:])
print(foo[:])

foo = ("Python", 200, 6.99, True, 'Duniailkom', 99j)
  
print(foo[0])
print(foo[1])
print(foo[2])
print(foo[2:5])
print(foo[:3])
print(foo[3:])
print(foo[:])
# foo[0] = "Belajar"
# print(foo)

foo = {"Belajar", "Python", "di", "Duniailkom", "di"}
bar = {100, 200, 300, 400, 200, 300}
 
print(foo)
print(bar)

foo = {1, 2, 3, 4, 5}
bar = {3, 4, 5, 6, 7}
 
print (foo | bar) # union
print (foo & bar) # intersection

foo = { 1: "Belajar", 
        2: ["Pascal", "C", "Python"],
        "website": "Duniailkom",
        "menyerah" : False,
        "target": 2020,
        "riwayat_sekolah": {
          "SD": "SDN 3 Hijau Daun",
          "SMP": "SMP 7 Hijau Lumut",
          "SMA": "SMA 8 Hijau Rumput"}
      }
       
print(foo)

foo = { "kegiatan": "Belajar Python",
        "website": "Duniailkom",
        "hasil": "Yakin bisa!" }
 
del foo["kegiatan"]
print(foo)

foo = dict ( kegiatan = "Belajar Python",
             website = "Duniailkom",
             hasil = "Yakin bisa!" )
              
print(foo)

x = 10
x += 5
print('x += 5  :',x)
  
x = 10
x /= 5
print('x /= 5  :',x)
  
x = 10
x **= 5
print('x **= 5 :',x)
  
x = 10
x <<= 2
print('x <<= 2 :',x)

foo = 'Duniailkom'
print('foo :',foo)
print('\'i\' in foo     :', 'i' in foo)
print('\'k\' not in foo :', 'k' not in foo)
print('\'d\' not in foo :', 'd' not in foo)
print('\n')
 
 
bar = ['a','b','c']
print('bar :',bar)
print('\'a\' in bar     :', 'a' in bar)
print('\'a\' not in bar :', 'a' not in bar)
print('\'d\' not in bar :', 'd' not in bar)
print('\n')
 
baz = (12,43,102,55)
print('baz :',baz)
print('102 in baz     :', 102 in baz)
print('102 not in baz :', 102 not in baz)
print('35 not in baz  :', 35 in baz)

i = 1
while i <= 5:
  print('Duniailkom', i)
  i += 1

i = 10
while i > 5:
  print('Duniailkom', i)
  i -= 1

for i in range(5):
  print(i)

for i in range(5,10):
  print(i)

i = 1
while i <= 10:
  print(i,' x ',i ,' = ',i*i)
  if i == 5:
    break
  i += 1

i = 1
while i <= 10:
  if i == 5:
    break
  print(i,' x ',i ,' = ',i*i)
  i += 1

for i in range(1,11):
  print(i,' x ',i ,' = ',i*i)
  if i == 5:
    break

for i in range(1,11):
  if i == 5:
    continue
  print(i,' x ',i ,' = ',i*i)

for i in range(1,11):
  print(i,' x ',i ,' = ',i*i)
  if i == 5:
    continue

i = 0
while i < 10:
  i += 1
  if i == 5:
    continue
  print(i,' x ',i ,' = ',i*i)

def hitung_luas_segitiga():
  alas = 5
  tinggi = 7
  luas = (alas * tinggi) / 2
  print("Luas segitiga adalah: ",luas)
   
hitung_luas_segitiga()

def hitung_luas_segitiga(alas, tinggi):
  luas = (alas * tinggi) / 2
  print("Luas segitiga adalah: ",luas)
    
hitung_luas_segitiga(5, 7)
hitung_luas_segitiga(2, 10)
hitung_luas_segitiga(191, 357)

def hitung_luas_segitiga(alas, tinggi):
  return (alas * tinggi) / 2
    
print("Luas segitiga adalah:", hitung_luas_segitiga(5, 7))

def harga_setelah_pajak(harga_dasar):
  return harga_dasar + (harga_dasar * 10/100)
 
harga_cilok = 5000
harga_final_cilok = harga_setelah_pajak(harga_cilok)
print("Harga cilok 1 porsi Rp.", harga_final_cilok)

def pangkat(angka, pangkat = 2):
  hasil = 1
  for i in range(0,pangkat):
    hasil = hasil * angka
  return hasil;
 
print( pangkat(3) )      # 9
print( pangkat(5) )      # 25
print( pangkat(10) )     # 100
print( pangkat(3,3) )    # 27
print( pangkat(5,4) )    # 625
print( pangkat(6,6) )    # 46656

def akses_database(address,username,password):
  print("====Database Connection====");
  print("server: ",address);
  print("username: ",username);
  print("password: ",password);
  print(".....connection success!");
   
akses_database(username="admin",password="qwerty",address="192.168.0.4")

def rata2(*args):
  hasil = 0
  for i in args:
    hasil += i
  return hasil / len(args)
   
print( rata2(5,7) )
print( rata2(5,7,3,2) )
print( rata2(5,7,3,2,8,2,1,3) )
print( rata2(100,200,300,400,500) )

def sambung_kata(**kata):
  for i in kata:
     print(i)
 
sambung_kata(a="Belajar", b="Python", c="di", d="Duniailkom")

def sambung_kata(**kata):
  for i in kata.values():
     print(i)
 
sambung_kata(a="Belajar", b="Python", c="di", d="Duniailkom")

def sambung_kata(**kata):
  hasil = ""
  for i in kata.values():
     hasil += i + " "
  return hasil;
 
print( sambung_kata(a="Belajar", b="Python", c="di", d="Duniailkom") )

def test(var1, var2, *args,**kwargs):
  print(var1)
  print(var2)
  print(args)
  print(kwargs)
 
test(10, 20, 30, 40, 50, a = 60, b = 70, c = 80)


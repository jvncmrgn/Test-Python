def maks(deret):
  nilai_terbesar = deret[0]

  for nilai in deret:
    if nilai > nilai_terbesar:
      nilai_terbesar = nilai

  return nilai_terbesar

def mini(deret):
  nilai_terkecil = deret[0]

  for nilai in deret:
    if nilai < nilai_terkecil:
      nilai_terkecil = nilai

  return nilai_terkecil

def modus(deret):
  peta_kemunculan = {}
  for bilangan in deret:
    if bilangan in peta_kemunculan:
      peta_kemunculan[bilangan] += 1
    else:
      peta_kemunculan[bilangan] = 1

  bilangan_terbesar = deret[0]
  for bilangan in peta_kemunculan.keys():
    jumlah = peta_kemunculan[bilangan]

    if jumlah > peta_kemunculan[bilangan_terbesar]:
      bilangan_terbesar = bilangan

  return bilangan_terbesar

def rata_rata(deret):
  rata = sum(deret) / len(deret)
  return rata

def StDev(deret):
  for i in range(len(deret)):
    deret[i] = int(deret[i])
  jumlah=0
  for i in range(len(deret)):
    jumlah += deret[i]
  
  rata=jumlah/len(deret)
  sigma = 0
  for i in range(len(deret)):
    hitung = (deret[i]-rata)**2
    sigma += hitung

  pembagianN=sigma/len(deret)
  standarDeviasi = pembagianN ** 0.5
  return standarDeviasi

def Var(deret):
  for i in range(len(deret)):
    deret[i] = int(deret[i])
  jumlah=0
  for i in range(len(deret)):
    jumlah += deret[i]
  
  rata=jumlah/len(deret)
  sigma = 0
  for i in range(len(deret)):
    hitung = (deret[i]-rata)**2
    sigma += hitung

  pembagianN=sigma/len(deret)
  Varians = pembagianN ** 0.5 ** 2
  return Varians

print("Bagian A")
print("Max, Min, Mode, Mean, Variance, Standard deviation from Tabungan")
Tabungan = [100000000, 50000000, 2000000000, 10000000, 150000000, 20000000, 75000000, 30000000, 5000000]
print("Minimum = ", maks(Tabungan))
print("Maximum = ", mini(Tabungan))
print("Mode = ", modus(Tabungan))
print("Mean = ", rata_rata(Tabungan))
print("Variance = ", Var(Tabungan))
print("Standard deviation = ", StDev(Tabungan))
print()

print("Max, Min, Mode, Mean, Variance, Standard deviation from Total_kekayaan")
Total_kekayaan = [50000000000, 1000000000, 50000000000, 300000000, 45000000000, 900000000, 2000000000, 3000000000, 500000000, 600000000]
print("Minimum = ", maks(Total_kekayaan))
print("Maximum = ", mini(Total_kekayaan))
print("Mode = ", modus(Total_kekayaan))
print("Mean = ", rata_rata(Total_kekayaan))
print("Variance = ", Var(Total_kekayaan))
print("Standard deviation = ", StDev(Total_kekayaan))

print("\n=======================================")
print("\nBagian B")
Tabungan.append(120000000)
Total_kekayaan.append(3400000000)

Tabungan_Furqon = 120000000
Kekayaan_Furqon = 3400000000


if Tabungan_Furqon > 50000000 and Kekayaan_Furqon > 1000000000:
    print("Tn. Furqon termasuk Kelas Atas")
else:
    print("Tn. Furqon termasuk Kelas Bawah")
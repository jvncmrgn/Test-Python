import csv

# Definisi state dan goal
class InstansiEdukasi:
    def __init__(self, nama: str, tipe: str, prasyarat: str, kualitas: int):
        self.nama = nama
        self.tipe = tipe
        self.prasyarat = prasyarat
        self.kualitas = kualitas

# Fungsi teknis membaca file csv
def readCsv() -> list:
    instansi = []
    with open('instansi.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            instansi.append(InstansiEdukasi(row[0].strip(), row[1].strip(), row[2].strip(), int(row[3])))
    return instansi

# Fungsi untuk mencari jalur terbaik / pilihan terbaik
def pilihInstansi(instansi: list, goal: str):
    pilihan = []

    currentInstansi = instansi.copy()
    for i in currentInstansi:
        # jika memiliki tipe sama dengan yang dicari, maka masukkan ke pilihan
        if i.tipe == goal:
            pilihan.append(i)
            instansi.remove(i)

    if len(pilihan) == 0:
        return False
    else:
        # pilih pilihan dengan kualitas terbaik
        pilihanTerbaik = max(pilihan, key=lambda x: x.kualitas)
        return pilihanTerbaik

# Fungsi teknis untuk menampilkan jalur terbaik / pilihan karir
def tampilkanPilihan(tahap):
    translate = {"s1-komputer": "Software Engineer", "s1-sipil": "Insinyur Sipil", "s1-mesin": "Insinyur Mesin", "s1-sosial": "HR", "s1-sejarah": "Guru Sejarah"}

    tahap.reverse()

    print("Jalur terbaik untuk mencapai karir tersebut adalah:")
    print("1. Bersekolah di Sekolah Dasar (SD)")
    for i in range(len(tahap)):
        print(f"{i+2}. Meneruskan studi di {tahap[i].nama} ({tahap[i].tipe})")
    print(f"{len(tahap)+2}. Bekerja sebagai {translate[tahap[-1].tipe]}")

# Fungsi untuk user memilih karir melalui command line
def pilihKarir() -> str:
    translate = {1: "s1-komputer", 2: "s1-sipil", 3: "s1-mesin", 4: "s1-sosial", 5: "s1-sejarah"}

    print("Pilih karir yang ingin dicapai:")
    print("1. Software Engineer")
    print("2. Insinyur Sipil")
    print("3. Insinyur Mesin")
    print("4. HR")
    print("5. Guru Sejarah")

    return translate[int(input("(1-5): ").strip())]

#Algoritma planning untuk mencari jalur terbaik / pilihan terbaik
def plan(instansi, goal):
    #instansiasi variabel menampung tahap tahap
    tahap = []
    #mengambil instansi yang memiliki tipe yang sama dengan goal
    objective = pilihInstansi(instansi, goal)

    while objective:
        #jika ditemukan instansi yang sesuai dengan action schema
        if objective:
            tahap.append(objective)

            #lanjutkan mencari instansi tahap selanjutnya
            objective = pilihInstansi(instansi, objective.prasyarat)
        else:
            break

    #jika jalur tidak ditemukan
    if len(tahap) != 3:
        return False
    else:
        return tahap

# Program utama
instansi = readCsv()
goal = pilihKarir()

tahap = plan(instansi, goal)

if not tahap:
    print("Tidak ada jalur untuk mencapai karir tersebut sesuai dataset yang ada")
else:
    tampilkanPilihan(tahap)

# panggil fungsi plan_career untuk merencanakan urutan tindakan yang optimal
plan = plan_career(programming_goal)

# tampilkan rencana karir
print("Career Plan:")
for i, action in enumerate(plan):
    print(f"{i+1}. {action}")
print("End of Career Plan")
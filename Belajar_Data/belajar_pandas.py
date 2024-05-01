import pandas as pd
import matplotlib.pyplot as plt    

order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
print(order_df.shape) #informasi mengenai berapa size dari dataframe yang akan digunakan termasuk berapa jumlah kolom dan jumlah baris data frame tersebut.
print(order_df.columns)
print(order_df.head())#gambaran dari konten dataframe tersebut
print(order_df.tail())# Konten Terbawah
print(order_df.describe())#print(order_df.describe(include="all")) Statistik deskriptif atau summary dalam Python - Pandas
# Function describe dapat memberikan informasi mengenai nilai rataan, standar deviasi dan IQR (interquartile range).
# Ketentuan umum:
# Secara umum function describe() akan secara otomatis mengabaikan kolom category dan hanya memberikan summary statistik untuk kolom berjenis numerik.
# Kita perlu menambahkan argument bernama include = "all" untuk mendapatkan summary statistik atau statistik deskriptif dari kolom numerik dan karakter.
#Jika ingin mendapatkan summary statistik dari kolom yang tidak bernilai angka, maka aku dapat menambahkan command include=["object"] pada syntax describe().
#Selanjutnya, untuk mencari rataan dari suatu data dari dataframe. Aku dapat menggunakan syntax mean, median, dan mode dari Pandas
print(order_df.loc[:, "price"].mean())
print("Hello Dunia")

# # Distribusi Data
# bins = jumlah_bins dalam histogram yang akan digunakan. Jika tidak didefinisikan jumlah_bins, maka function akan secara default menentukan jumlah_bins sebanyak 10.
# by = nama kolom di DataFrame untuk di group by. (valuenya berupa nama column di dataframe tersebut).
# alpha = nilai_alpha untuk menentukan opacity dari plot di histogram. (value berupa range 0.0 - 1.0, dimana semakin kecil akan semakin kecil opacity nya)
# figsize = tuple_ukuran_gambar yang digunakan untuk menentukan ukuran dari plot histogram. Contoh: figsize=(10,12)
# nama_dataframe[["nama_kolom"]].hist(bins=jumlah_bin,
#                                     by=nama_kolom,
#                                     alpha=nilai_alpha,
#                                     figsize=tuple_ukuran_gambar)
order_df[["price"]].hist(figsize=(4, 5), bins=10, xlabelsize=8, ylabelsize=8)
plt.show()

#Outliers merupakan data observasi yang muncul dengan nilai-nilai ekstrim. Yang dimaksud dengan nilai-nilai ekstrim dalam observasi adalah nilai yang jauh atau beda sama sekali dengan sebagian besar nilai lain dalam kelompoknya.
# Hitung quartile 1
Q1 = order_df[["product_weight_gram"]].quantile(0.25)
# Hitung quartile 3
Q3 = order_df[["product_weight_gram"]].quantile(0.75)
# Hitung inter quartile range dan cetak ke console
IQR = Q3-Q1
print(IQR)

#Mengganti Nama Kolom
order_df.rename(columns={"price": "harga"}, inplace=True)
order_df.columns.values[0] = "harga"

#Kegunaan .groupby adalah mencari summary dari data frame dengan menggunakan aggregate dari kolom tertentu.
rata_rata = order_df["price"].groupby(order_df["payment_type"]).mean()

#Sorting adalah sebuah metode mengurutkan data berdasarkan syarat kolom tertentu dan biasanya digunakan untuk melihat nilai maksimum dan minimum dari dataset. Library Pandas sendiri menyediakan fungsi sorting sebagai fundamental dari exploratory data analysis.
sort_harga = order_df.sort_values(by="price", ascending=False)
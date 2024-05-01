import numpy as np
print("Bagian A")
matriksA = [
    ["Salman", 100000000, "Rumah, Mobil, Motor", 50000000000, "Atas"], 
    ["Iyan", 50000000, "Rumah, Mobil, Motor", 1000000000, "Atas"],
    ["Karim", 2000000000, "Rumah, Motor", 50000000000, "Atas"],
    ["Bowlang", 10000000, "Rumah, Motor", 300000000, "Bawah"],
    ["Adit", 150000000, "Rumah, Mobil, Motor", 45000000000, "Atas"],
]
print("\n", matriksA)

print("\nBagian B")
matriksB = [
    ["Soqi", 20000000, "Rumah, Motor", 900000000, "Bawah"],
    ["Gatot", 50000000, "Rumah, Mobil, Motor", 2000000000, "Atas"],
    ["Firly", 75000000, "Rumah, Mobil, Motor", 3000000000, "Atas"],
    ["Okta", 30000000, "Rumah, Mobil, Motor", 500000000, "Bawah"],
    ["Nandi", 5000000, "Rumah, Motor", 600000000, "Bawah"]
]
print(matriksB)

print("\nSoal 5")
x = matriksA + matriksB
print(x)
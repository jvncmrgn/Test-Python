# # Tentukan output yaitu “Teknik Geologi masuk ke dalam fakultas Teknik”, 
# fakultas=[("Teknik Geologi ","Teknik"),("Manajemen","FEB")] 
# (name, fakultas) = (fakultas[0][0], fakultas[0][1]) 
# print(name, " masuk ke dalam fakultas ",fakultas,'.',sep= "" )

# # nama-nama lima puluh negara di dunia
# countries = [ "Japan", "India", "Algeria", "Brazil", "Angola", "England", "Argentina", "Portugal",
# "China", "Australia", "Austria", "Ghana", "Bahamas", "Bangladesh", "Belgium", "Bhutan", "Bosnia",
# "Cameroon", "Canada", "Denmark"]
# # bagian a
# print(countries[2], ", ", countries[-1])
# # bagian b
# countries.insert(5, "Germany")
# print(countries[5])
# # bagian c
# del countries[4]
# print(countries[4])
# # bagian d
# countries[1] = "Poland"
# print(countries[:3])
# # bagian e
# print(countries[2:len(countries)])


tuple1 = ("universitas", "sriwijaya", "fakultas", "teknik", "prodi", "teknik geologi")
tuple2 = tuple1[4:]
tuple3 = tuple1[2:4]
tuple4 = tuple1[:2]
# Tentukan tuple2 menjadi :
# ('prodi', 'teknik geologi', 'fakultas', 'teknik', 'universitas', 'sriwijaya')
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
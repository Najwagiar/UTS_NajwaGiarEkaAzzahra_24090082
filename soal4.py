 #Meminta input berat badan (dalam kilogram) dan tinggi badan (dalam meter)
berat_badan = float(input("Masukan Berat Badan Anda (kg):"))
tinggi_badan = float(input("Masukan Tinggi Badan Anda (m):"))

#Menghitung BMI
bmi = berat_badan / (tinggi_badan ** 2)

#Menentukan kategori BMI
if bmi < 18.5:
    ketegori = "berat badan kurang"
elif 18.5 <= bmi < 24.9:
    kategori = "berat badan normal"
elif 25 <= bmi < 29.9:
    kategori = "kelebihan berat badan"
else:
    kattegori = "obesitas"

#Menampilkan hasil BMI dan reekomendasi
print(f"Indeks Masa Tubuh (BMI) Anda: {bmi:.2f}")
print(f"kategori: {kategori}")
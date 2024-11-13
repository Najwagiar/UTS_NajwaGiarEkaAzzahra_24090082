# Program menentukan apakah suatu tahun adalah kabisat

# Masukan tahun
year = int(input("Masukan Tahun:"))

# Menentukan apakah tahun tersebut kabisat atau bukan

if (year % 400 == 0):...
elif (year % 4 == 0 and year % 100 != 0):
    print(f"{year} adalah tahun kabisat.")
else :
    print(f"{year} bukan tahun kabisat.")
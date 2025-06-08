def deret_ganjil_tak_beraturan(jumlahsuku, sukusekarang=1, selisih=2):
    if jumlahsuku == 1:
        return sukusekarang
    return sukusekarang + deret_ganjil_tak_beraturan(jumlahsuku - 1, sukusekarang + selisih, selisih + 2)

print(deret_ganjil_tak_beraturan(5))  


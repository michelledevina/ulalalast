def is_palindrom(kalimat):
    kalimat = kalimat.replace(" ", "").lower()
    
    def cek_rekursif(teks):
        if len(teks) <= 1:
            return True
        if teks[0] != teks[-1]:
            return False
        return cek_rekursif(teks[1:-1])

    return cek_rekursif(kalimat)

kalimat = "Kasur ini rusak"
if is_palindrom(kalimat):
    print(f'"{kalimat}" adalah palindrom')
else:
    print(f'"{kalimat}" bukan palindrom')


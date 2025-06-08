def jumlah_digit(n):
    if n < 10:
        return n
    return n % 10 + jumlah_digit(n // 10)

angka = 234
print(f"Jumlah digit dari {angka} adalah {jumlah_digit(angka)}")

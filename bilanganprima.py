def cek_prima(n, pembagi=2):
    if n <= 1:
        return False
    if pembagi * pembagi > n:
        return True
    if n % pembagi == 0:
        return False
    return cek_prima(n, pembagi + 1)

angka = 17
if cek_prima(angka):
    print(f"{angka} adalah bilangan prima")
else:
    print(f"{angka} bukan bilangan prima")

    

def kombinasi(n, r):
    def faktorial(k):
        if k == 0 or k == 1:
            return 1
        return k * faktorial(k - 1)
    
    if n < r:
        return 0  
    return faktorial(n) // (faktorial(r) * faktorial(n - r))

print(kombinasi(5, 2))  

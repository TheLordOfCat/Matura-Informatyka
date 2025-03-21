def Rek(n):
    if n > 0:
        Rek(n-1)
        print(n)

Rek(5)
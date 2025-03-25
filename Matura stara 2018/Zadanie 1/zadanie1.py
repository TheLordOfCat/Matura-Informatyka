n = 94000
T = [n]
i = 0

while True:
    ok = True
    k = T[i]
    suma = 0

    while k > 0:
        suma = suma + (k%10)*(k%10)
        k = k//10

    if suma == 1:
        print("liczba wesoła")
        ok = False
        break

    if not ok:
        break

    for j in range(0, i+1):
        if T[j] == suma:
            print("Liczba smutna")
            ok = False
            break

    if not ok:
        break

    i = i + 1
    T.append(0)
    T[i] = suma

print(T)
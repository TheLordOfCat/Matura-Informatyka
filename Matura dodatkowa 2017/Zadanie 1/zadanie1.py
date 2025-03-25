n = 100
Czyjest = [False]
for i in range(1, n+1):
    Czyjest.append(False)
j = 1
c = 0
while j*j < n:
    j += 1
for i in range(2, j+1):
    kw = i*i
    poz = kw
    while poz <= n:
        c += 1
        Czyjest[poz] = True
        poz = poz + kw

found = False
k = 12
for i in range(0, k+1):
    if Czyjest[i] == True and Czyjest[k-i] == True:
        found = True
        break

print(found)


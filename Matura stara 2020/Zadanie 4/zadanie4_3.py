f = open("dane.txt" , "r")
data = f.read().split()

ans = 0

sp = []
for i in range(0, len(data)):
    cD1 = [False] * 10
    d1 = int(data[i])
    while d1 > 0:
        cD1[d1 % 10] = True
        d1 //= 10

    sp.append(cD1)

for i in range(0, len(data)):
    for j in range(i+1, len(data)):
        ok = True
        for o in range(0, 10):
            if sp[i][o] != sp[j][o]:
                ok = False

        if ok:
            ans += 1

print(ans)
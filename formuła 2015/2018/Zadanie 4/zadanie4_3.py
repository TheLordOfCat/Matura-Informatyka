f = open("sygnaly.txt", "r")
data = f.read().split()

ans = []

for d in data:
    ok = True
    for i in range(0, len(d)):
        for j in range(0, len(d)):
            dif = ord(d[j]) - ord(d[i])
            if dif < 0:
                dif *= -1
            if dif > 10:
                ok = False
    if ok:
        ans.append(d)

for a in ans:
    print(a)

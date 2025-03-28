f = open("gra.txt", "r")
data = f.read().split()

base = []
for i in range(0, len(data)):
    temp = []
    for j in range(0, len(data[i])):
        temp.append(data[i][j])
    base.append(temp)

for z in range(0,100):
    pro = [row[:] for row in base]
    for i in range(0, len(base)):
        for j in range(0, len(base[i])):
            countLive = 0

            for o in range(-1, 2):
                for k in range(-1, 2):

                    if o == 0 and k == 0:
                        continue

                    if base[(i+o)%len(base)][(j+k)%len(base[i])] == "X":
                        countLive += 1

            if base[i][j] == "X" and (countLive == 2 or countLive == 3):
                pro[i][j] = "X"
            elif base[i][j] == "." and countLive == 3:
                pro[i][j] = "X"
            else:
                pro[i][j] = "."

    ok = True
    for s in range(0, len(base)):
        for t in range(0, len(base[s])):
            if base[s][t] != pro[s][t]:
                ok = False
                break
        if not ok:
            break

    if ok:
        print(z+2)
        break

    base = [row[:] for row in pro]

ans = 0
for l in base:
    for n in l:
        if n == "X":
            ans += 1

print(ans)
f = open("plansza.txt", "r")
data = f.read().split()

l = 100
plane = []
ind = 0
for i in range(0, l):
    temp = []
    for j in range(0, l):
        temp.append(data[ind])
        ind +=1
    plane.append(temp)


ans = 0
for i in range(0,l):
    for j in range(0,l):
        ok = True

        for o in range(-1, 2):
            for k in range(-1, 2):
                if 0 <= i + o < l and 0 <= j + k <l:
                    if plane[i+o][j+k] != "0":
                        ok = False
                        break

        if ok:
            ans += 1

print(ans)




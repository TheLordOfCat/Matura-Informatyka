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
    for j in range(i+1,l):

        ok = True

        for o in range(-1, 2):
            for k in range(-1, 2):
                if 0 <= i + o < l and 0 <= j + k <l and (o != 0 or k != 0):
                    if plane[i+o][j+k] != "0":
                        ok = False
                        break

        for o in range(-1, 2):
            for k in range(-1, 2):
                if 0 <= j + o < l and 0 <= i + k <l and (o != 0 or k != 0):
                    if plane[j+o][i+k] != "0":
                        ok = False
                        break

        if plane[i][j] == "1" and plane[j][i] == "1" and ok:
            ans += 1

print(ans)





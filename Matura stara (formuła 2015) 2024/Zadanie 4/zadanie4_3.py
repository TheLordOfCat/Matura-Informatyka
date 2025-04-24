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


ans1 = 0
ans2 = 0

for i in range(0,l):
    j = i
    if plane[i][j] == "1":
        ok = True

        for o in range(-1, 2):
            for k in range(-1, 2):
                if 0 <= i + o < l and 0 <= j + k <l and (o != 0 or k != 0):
                    if plane[i+o][j+k] != "0":
                        ok = False
                        break

        if ok == True:
            ans1 += 1
        else:
            ans2 += 1

for i in range(0,l):
    j = l-i-1
    if plane[i][j] == "1":
        ok = True

        for o in range(-1, 2):
            for k in range(-1, 2):
                if 0 <= i + o < l and 0 <= j + k <l and (o != 0 or k != 0):
                    if plane[i+o][j+k] != "0":
                        ok = False
                        break

        if ok == True:
            ans1 += 1
        else:
            ans2 += 1

l-=1
if (plane[int(l/2)][int(l/2)] == "1" and plane[int(l/2)+1][int(l/2)] == "1") or (plane[int(l/2)][int(l/2)] == "1" and plane[int(l/2)][int(l/2)+1] == "1"):
    ans2 -= 1
if (plane[int(l/2)+1][int(l/2)+1] == "1" and plane[int(l/2)+1][int(l/2)] == "1") or (plane[int(l/2)+1][int(l/2)+1] == "1" and plane[int(l/2)][int(l/2)+1] == "1"):
    ans2 -= 1

print(ans1)
print(ans2)





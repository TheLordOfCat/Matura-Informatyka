f1 = open("dane1.txt" , "r")
data1 = f1.read().split("\n")

f2 = open("dane2.txt", "r")
data2 = f2.read().split("\n")

ans = []
for o in range(0, len(data1)):
    d1 = data1[o].split(" ")
    d2 = data2[o].split(" ")

    ind1 = 0
    ind2 = 0

    temp = []
    for i in range(0, len(d1)+len(d2)):
        if ind1 == len(d1):
            temp.append(int(d2[ind2]))
            ind2 += 1
        elif ind2 == len(d2):
            temp.append(int(d1[ind1]))
            ind1 += 1
        else:
            if int(d1[ind1]) < int(d2[ind2]):
                temp.append(int(d1[ind1]))
                ind1 += 1
            else:
                temp.append(int(d2[ind2]))
                ind2 += 1
    ans.append(temp)

for l in ans:
    print(l)

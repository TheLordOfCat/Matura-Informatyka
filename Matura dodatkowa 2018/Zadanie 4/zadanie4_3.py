f1 = open("dane1.txt" , "r")
data1 = f1.read().split("\n")

f2 = open("dane2.txt", "r")
data2 = f2.read().split("\n")

ans = 0
ansLines = []
for o in range(0, len(data1)):
    d1 = data1[o].split(" ")
    d2 = data2[o].split(" ")

    ok1 = True
    for i in range(0, len(d1)):
        found = False
        for j in range(0, len(d2)):
            if d1[i] == d2[j]:
                found = True
                break
        if found == False:
            ok1 = False
            break

    ok2 = True
    for i in range(0, len(d2)):
        found = False
        for j in range(0, len(d1)):
            if d2[i] == d1[j]:
                found = True
                break
        if found == False:
            ok2 = False
            break

    if ok1 and ok2:
        ans+= 1
        ansLines.append(o+1)




print(ans)
print(ansLines)
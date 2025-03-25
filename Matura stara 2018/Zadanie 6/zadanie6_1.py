f = open("slowa.txt", "r")
data = f.read().split("\n")

c = 0
for d in data:
    sList = d.split(" ")
    s1 = sList[0]
    s2 = sList[1]

    if len(s1) > len(s2):
        continue

    for i in range(0, len(s2)-len(s1)+1):
        ok = True
        for j in range(0, len(s1)):
            if s2[i+j] != s1[j]:
                ok = False
                break
        if ok:
            c += 1
            break

print(c)
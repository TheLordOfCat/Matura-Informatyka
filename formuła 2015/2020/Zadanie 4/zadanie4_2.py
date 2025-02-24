f = open("pary.txt", "r")
data = f.read().split()

ans = []

for i in range(0, len(data), 2):
    num = data[i]
    s = data[i+1]

    ansC = ""
    ansVal = 0

    curC = ""
    valC = 0

    for l in s:
        if curC == l:
            valC += 1
        else:
            if valC > ansVal:
                ansC = curC
                ansVal = valC
            curC = l
            valC = 1
    ans.append([ansC, ansVal])

print(ans)


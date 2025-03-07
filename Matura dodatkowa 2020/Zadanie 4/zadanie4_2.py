f = open("identyfikator.txt" , "r")
data = f.read().split()

ans = []
bestVal = 0

for d in data:
    #get base
    serial = ""
    for i in range(0,3):
        serial += d[i]
    numStr = ""
    for i in range(3, len(d)):
        numStr += d[i]
    num = int(numStr)

    #get Inv
    serialInv = ""
    for i in range(2,-1, -1):
        serialInv += serial[i]

    numStrInv = ""
    for i in range(len(numStr)-1, -1, -1):
        numStrInv += numStr[i]

    ok1 = True
    for i in range(0, len(serial)):
        if serial[i] != serialInv[i]:
            ok1 = False
            break

    ok2 = True
    for i in range(0, len(numStr)):
        if numStr[i] != numStrInv[i]:
            ok2 = False
            break

    if ok1 or ok2:
        ans.append(d)

print(ans)


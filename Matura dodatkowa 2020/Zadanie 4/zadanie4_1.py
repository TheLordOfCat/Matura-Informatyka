f = open("identyfikator.txt" , "r")
data = f.read().split()

ans = []
bestVal = 0

for d in data:
    serial = ""
    for i in range(0,3):
        serial += d[i]
    numStr = ""
    for i in range(3, len(d)):
        numStr += d[i]
    num = int(numStr)

    sumDigits = 0
    for i in numStr:
        sumDigits += int(i)

    if sumDigits == bestVal:
        ans.append(d)
    elif sumDigits > bestVal:
        ans.clear()
        ans.append(d)
        bestVal = sumDigits

print(ans)


f = open("identyfikator.txt" , "r")
data = f.read().split()

ans = []

for d in data:
    #get base
    serial = ""
    for i in range(0,3):
        serial += d[i]
    numStr = ""
    for i in range(3, len(d)):
        numStr += d[i]

    num = 0
    serialCoe = "731"
    for i in range(0, len(serial)):
        num += int(serialCoe[i])*(ord(serial[i])-ord("A") + 10)

    numCoe = "73173"
    for i in range(1, len(numStr)):
        num += int(numCoe[i-1])*int(numStr[i])

    if num%10 != int(numStr[0]):
        ans.append(d)

print(ans)




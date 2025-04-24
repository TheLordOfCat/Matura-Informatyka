f = open("przyklad.txt", "r")
data = f.read().split()

ansType = ""
ansCount = 0

curType = data[0]
curCount = 1

for i in range(2, len(data), 2):
    if data[i] == curType:
        curCount += 1
    else:
        if curCount > ansCount:
            ansCount = curCount
            ansType = curType
        curType = data[i]
        curCount = 1

if curCount > ansCount:
    ansCount = curCount
    ansType = curType

print(ansType)
print(ansCount)
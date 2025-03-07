f = open("dane4.txt" , "r")
data = f.read().split()

holes = []

for i in range(1, len(data)-1):
    dif = int(data[i+1]) - int(data[i])
    if dif < 0:
        dif *= (-1)
    holes.append(dif)

ansLen = 0
ansCount = []

for i in range(0, len(holes)):
    curLen = 0
    for j in range(i, len(holes)):
        if holes[j] == holes[i]:
            curLen += 1
    if curLen == ansLen:
        ansCount.append(holes[i])
    elif curLen > ansLen:
        ansCount = [holes[i]]
        ansLen = curLen

print(ansLen)
print(ansCount)
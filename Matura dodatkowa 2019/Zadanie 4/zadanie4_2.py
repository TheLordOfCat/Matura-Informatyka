f = open("dane4.txt" , "r")
data = f.read().split()

ansLen = 0
ansFirstSeq = 0
ansLastSeq = 0

curLong = int(data[0]) - int(data[1])
if curLong < 0:
    curLong *= -1
curLen = 2
firstSeq = data[0]
lastSeq = data[1]

for i in range(1, len(data)-1):
    dif = int(data[i+1]) - int(data[i])
    if dif < 0:
        dif *= (-1)
    if dif == curLong:
        curLen += 1
        lastSeq = data[i+1]
    else:
        if curLen > ansLen:
            ansLen = curLen
            ansFirstSeq = firstSeq
            ansLastSeq = lastSeq
        curLong = dif
        curLen = 2
        firstSeq = data[i]
        lastSeq = data[i+1]

if curLen > ansLen:
    ansLen = curLen
    ansFirstSeq = firstSeq
    ansLastSeq = lastSeq

print(ansLen)
print(ansFirstSeq)
print(ansLastSeq)


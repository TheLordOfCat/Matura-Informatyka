f = open("dane.txt", "r")
data = f.read().split()

#generate lucky number up to 10000
totalLen = 10000
isLucky = [True]*(totalLen+1)

for i in range(0,totalLen+1, 2):
    isLucky[i] = False

for i in range(3, totalLen+1):
    if isLucky[i] == True:
        c = 0
        for j in range(1, totalLen+1):
            if isLucky[j] == True:
                c += 1
                if c == i:
                    isLucky[j] = False
                    c = 0

ans = 0
ansF = 0

cur = 0
curF = -1
for i in range(0, len(data)):
    if isLucky[int(data[i])] == True:
        cur += 1
        if curF == -1:
            curF = int(data[i])
    else:
        if cur > ans:
            ans = cur
            ansF = curF
        cur = 0
        curF = -1

if cur > ans:
    ans = cur
    ansF = curF

print(ans)
print(ansF)
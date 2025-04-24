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
for i in range(0, len(data)):
    if isLucky[int(data[i])] == True:
        ans += 1

print(ans)
T = [0,1,2,3,5,5]
n = 5

m = 0
for i in range(1, len(T)):
    countNum = 0
    num = T[i]
    for j in range(1, len(T)):
        if T[j] == num:
            countNum += 1
    if countNum > m:
        m = countNum

print(m)


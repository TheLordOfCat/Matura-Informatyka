f = open("pi_przyklad.txt", "r")
data = f.read().split()

ansF = 0
ansS = 0
ansLen = 0

for i in range(0, len(data)):
    count = 1
    l = 1
    ind = 0

    for j in range(i+1, len(data)):
        if count == 1:
            if data[j] > data[j-1]:
                l += 1
            else:
                count += 1
                l += 1
            ind = j
        elif count == 2:
            if data[j] < data[j-1]:
                l += 1
            else:
                count += 1
            ind = j
        else:
            break

    if ansLen < l:
        ansF = i
        ansS = ind
        ansLen = l

print(ansF)
for i in range(ansF, ansF+ansLen):
    print(data[i], end= "")


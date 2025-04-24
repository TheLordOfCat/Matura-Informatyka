f = open("anagram.txt", "r")
data = f.read().split()

ansZ = 0
ansP = 0

for d in data:
    countOne = 0
    countZero = 0
    for l in d:
        if l == "0":
            countZero += 1
        if l == "1":
            countOne += 1
    if countZero == countOne:
        ansZ += 1
    if countZero == countOne + 1 or countZero+1 == countOne:
        ansP +=1

print(ansZ)
print(ansP)
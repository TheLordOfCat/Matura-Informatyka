f = open("anagram.txt", "r")
data = f.read().split()

ansCount = 0
ansList = []

for d in data:
    if len(d) != 8:
        continue

    curCount = 1

    countOne = 0
    for l in d:
        if l == "1":
            countOne += 1

    for i in range(1, 8):
        curCount *= i

    for i in range(1, countOne):
        curCount /= i

    for i in range(1, 7-(countOne-1)+1):
        curCount /= i

    if curCount > ansCount:
        ansList.clear()
        ansList.append(d)
        ansCount = curCount
    elif curCount == ansCount:
        ansList.append(d)

print(ansCount)
print(ansList)
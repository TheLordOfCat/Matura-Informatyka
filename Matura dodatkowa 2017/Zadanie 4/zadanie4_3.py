f = open("punkty.txt", "r")
data = f.read().split("\n")

ans = 0
ansA = []
ansB = []
for i in range(0, len(data)):
    numA = data[i].split(" ")

    for j in range(i, len(data)):
        numB = data[j].split(" ")

        ab = (int(numB[0]) - int(numA[0]))*(int(numB[0]) - int(numA[0])) + (int(numB[1]) - int(numA[1]))*(int(numB[1]) - int(numA[1]))
        if ab > ans:
            ans = ab
            ansA.clear()
            ansB.clear()
            ansA = [numA[0], numA[1]]
            ansB = [numB[0], numB[1]]

print(ans)
print(ansA)
print(ansB)

f = open("slowa.txt", "r")
data = f.read().split()

for d in data:
    countW = 0
    countK = 0
    countA = 0
    countC = 0
    countJ = 0
    countE = 0

    words = 0

    for l in d:
        if l == "w":
            countW += 1
        if l == "k":
            countK += 1
        if l == "a":
            countA += 1
        if l == "c":
            countC += 1
        if l == "j":
            countJ += 1
        if l == "e":
            countE += 1

    while countW >= 1 and countA >= 2 and countK >= 1 and countC >= 1 and countJ >= 1 and countE >= 1:
        words += 1

        countW -= 1
        countA -= 2
        countK -= 1
        countC -= 1
        countJ -= 1
        countE -= 1

    print(words, end=" ")

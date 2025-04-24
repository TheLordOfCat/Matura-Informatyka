f = open("slowa.txt", "r")
data = f.read().split()

for d in data:
    countW = 0
    countK = 0
    for l in d:
        if l == "w":
            countW += 1
        if l == "k":
            countK += 1
    if countW == countK:
        print(d)

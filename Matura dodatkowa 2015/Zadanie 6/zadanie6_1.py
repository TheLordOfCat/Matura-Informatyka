f = open("kody.txt" , "r")
data = f.read().split("\n")

for d in data:
    num = d

    parz = 0
    for i in range(0, len(d), 2):
        parz += int(d[i])

    niep = 0
    for i in range(1, len(d), 2):
        niep += int(d[i])

    print(str(parz) + " " + str(niep))

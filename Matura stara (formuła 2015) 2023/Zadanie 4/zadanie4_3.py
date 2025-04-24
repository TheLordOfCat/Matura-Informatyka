f = open("slowa.txt", "r")
data = f.read().split()

for d in data:
    base = "wakacje"
    ind = 0

    rem = 0

    for i in range(0, len(d)):
        if d[i] == base[ind]:
            ind += 1
            ind %= len(base)
        else:
            rem += 1

    if ind != 0:
        rem += ind

    print(rem)

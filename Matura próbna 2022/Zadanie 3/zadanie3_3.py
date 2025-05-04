f = open("liczby.txt", "r")
data = f.read().split()

countHex = [0]*16

for d in data:
    num = int(d)
    resPrimes = []

    s = hex(num)
    for i in range(2, len(s)):
        c = str(s[i])
        if c == "a":
            countHex[10] += 1
        elif c == "b":
            countHex[11] += 1
        elif c == "c":
            countHex[12] += 1
        elif c == "d":
            countHex[13] += 1
        elif c == "e":
            countHex[14] += 1
        elif c == "f":
            countHex[15] += 1
        else:
            countHex[int(c)] += 1

print(countHex)
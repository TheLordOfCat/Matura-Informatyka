f = open("liczby.txt", "r")
data = f.read().split()

for d in data:
    dRev = ""
    for i in range(len(d)-1, -1, -1):
        dRev += d[i]
    if int(dRev)%17 == 0:
        print(dRev)
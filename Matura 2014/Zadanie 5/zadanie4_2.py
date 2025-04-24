f = open("NAPIS.TXT", "r")
data = f.read().split()

for d in data:
    ok = True
    for i in range(1, len(d)):
        if ord(d[i]) <= ord(d[i-1]):
            ok = False
            break
    if ok:
        print(d)


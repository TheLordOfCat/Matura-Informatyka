f = open("dane.txt", "r")
data = f.read().split()

ansSmall = "1000000000000000"
ansBig = "0"
for d in data:
    ok = True
    for i in range(0, len(d)-1):
        if not d[i] <= d[i+1]:
            ok = False
            break

    if ok:
        if int(ansSmall,8) > int(d,8):
            ansSmall = d
        if int(ansBig, 8) < int(d, 8):
            ansBig = d

print(ansSmall)
print(ansBig)
f = open("slowa.txt" , "r")
data = f.read().split()

ans = 0
ansLon = ""
for d in data:
    shift = ""

    for l in d:
        shift += chr(ord("a") + (ord(l)-ord("a") + 13)%26)

    shiftRev = ""
    for i in range(len(d)-1, -1, -1):
        shiftRev += shift[i]

    if d == shiftRev:
        ans += 1
        if len(ansLon) <= len(shift):
            ansLon = d

print(ans)
print(ansLon)

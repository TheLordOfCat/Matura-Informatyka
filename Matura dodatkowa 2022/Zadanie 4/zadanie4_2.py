f = open("liczby.txt", "r")
data = f.read().split()

ans = 0
ansDist = 0

for d in data:
    dRev = ""
    for i in range(len(d)-1, -1, -1):
        dRev += d[i]

    dist = int(d)-int(dRev)

    if dist < 0:
        dist *= -1

    if dist > ansDist:
        ans = d
        ansDist = dist

print(ans)
print(ansDist)
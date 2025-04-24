f = open("NAPIS.TXT", "r")
data = f.read().split()

ans = 0
for d in data:
    sum = 0
    for l in d:
        sum += ord(l)

    ok = True
    for i in range(2, sum):
        if sum %i == 0:
            ok = False
            break

    if ok:
        ans += 1

print(ans)
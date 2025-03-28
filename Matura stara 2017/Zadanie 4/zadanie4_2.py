f = open("binarne.txt", "r")
data = f.read().split()

smallest = "100000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
ans = 0
for d in data:
    ok = True
    for i in range(0, len(d), 4):
        num = ""
        for j in range(0, 4):
            num = num + d[i+j]
        n = int(num, 2)
        if n > 9:
            ok = False
            break

    if not ok:
        ans += 1
        if len(smallest) > len(d):
            smallest = d
print(ans)
print(len(smallest))

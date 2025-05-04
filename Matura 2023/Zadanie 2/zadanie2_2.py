f = open("bin.txt", "r")
data = f.read().split()

ans = 0

for d in data:
    countBlocks = 1

    for i in range(1, len(d)):
        if d[i] != d[i-1]:
            countBlocks += 1

    if countBlocks <= 2:
        ans += 1

print(ans)
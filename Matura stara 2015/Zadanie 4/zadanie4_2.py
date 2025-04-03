f = open("slowa.txt" , "r")
data = f.read().split()

ans = 0
for d in data:

    countBlocks = 1
    last = d[0]
    if last != "0":
        continue
    for l in d:
        if l != last:
            countBlocks += 1
            last = l

    if countBlocks == 2:
        # print(d)
        ans += 1

print(ans)



f = open("liczby.txt", "r")
data = f.read().split()

ans = 0
for d in data:
    countOne = 0
    countZero = 0
    for l in d:
        if l == "0":
            countZero += 1
        elif l == "1":
            countOne += 1

    if countZero > countOne:
        ans += 1

print(ans)
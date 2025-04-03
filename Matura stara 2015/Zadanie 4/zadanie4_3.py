f = open("slowa.txt" , "r")
data = f.read().split()

ansLen = 0
ans = []
for d in data:

    longestZero = 0
    cur = 0

    for l in d:
        if l == "0":
           cur += 1
        else:
            longestZero = max(longestZero, cur)
            cur = 0

    longestZero = max(longestZero, cur)

    if longestZero > ansLen:
        ansLen = longestZero
        ans = [d]
    elif longestZero == ansLen:
        ans.append(d)

print(ansLen)
print(ans)



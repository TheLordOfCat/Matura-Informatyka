f = open("bin.txt", "r")
data = f.read().split()

for d in data:
    num = int(d, 2)
    ops = num^(num//2)
    s = bin(ops)
    ans = ""
    for i in range(2, len(s)):
        ans += s[i]
    print(ans)
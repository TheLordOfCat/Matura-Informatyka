f = open("dane.txt", "r")
data = f.read().split()

ans = 0
for d in data:
    num = int(d,8)
    s = str(num)
    if s[0] == s[len(s)-1]:
        ans += 1

print(ans)
f = open("dane.txt", "r")
data = f.read().split()

ans = 0
for d in data:
    if d[0] == d[len(d)-1]:
        ans += 1

print(ans)
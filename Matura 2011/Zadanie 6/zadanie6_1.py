f = open("liczby.txt", "r")
data = f.read().split()

ans = 0
for d in data:
    if int(int(d,2))%2 == 0:
        ans += 1

print(ans)
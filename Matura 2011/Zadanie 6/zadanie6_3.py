f = open("liczby.txt", "r")
data = f.read().split()

ans = 0
sum = 0
for d in data:
    if len(d) == 9:
        ans += 1
        sum += int(int(d, 2))

print(ans)
print(bin(sum))
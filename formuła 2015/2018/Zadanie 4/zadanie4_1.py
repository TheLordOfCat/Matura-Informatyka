f = open("sygnaly.txt", "r")
data = f.read().split()

ans = ""
for i in range(39, len(data), 40):
    ans += data[i][9]

print(ans)

f = open("mecz.txt", "r")
data = f.read().split()

ans = 0
for i in range(1, len(data[0])):
    if data[0][i] != data[0][i-1]:
       ans += 1

print(ans)
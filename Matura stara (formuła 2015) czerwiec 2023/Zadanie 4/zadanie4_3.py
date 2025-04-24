f = open("anagram.txt", "r")
data = f.read().split()

ans = 0
for i in range(0, len(data)-1):
    dif = int(data[i], 2) - int(data[i+1], 2)
    if dif < 0:
        dif *= -1

    ans = max(ans, dif)

print(bin(ans))
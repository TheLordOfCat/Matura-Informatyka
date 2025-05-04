f = open("pi.txt", "r")
data = f.read().split()

ans = 0
for i in range(0, len(data)-1):
    num1 = data[i]
    num2 = data[i+1]

    numS = num1 + num2
    num = int(numS)

    if num > 90:
        ans += 1

print(ans)

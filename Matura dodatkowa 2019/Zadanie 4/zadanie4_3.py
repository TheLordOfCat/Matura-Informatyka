f = open("pierwsze.txt" , "r")
data = f.read().split()

ans = []

for d in data:
    num = int(d)

    while num >= 10:
        s = str(num)
        sum = 0
        for l in s:
            sum += int(l)
        num = sum

    if num == 1:
        ans.append(d)

print(len(ans))



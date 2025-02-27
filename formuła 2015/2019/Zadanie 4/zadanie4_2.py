f = open("liczby.txt", "r")
data = f.read().split()

ans = []

for d in data:
    digits = []
    dCopy = int(d)

    while dCopy > 0:
        c = dCopy - (dCopy//10)*10
        digits.append(c)
        dCopy//=10

    sumDigits = 0
    for i in range(0, len(digits)):
        p = 1
        for j in range(1, digits[i]+1):
            p *= j
        sumDigits += p

    if sumDigits == int(d):
        ans.append(d)

print(ans)


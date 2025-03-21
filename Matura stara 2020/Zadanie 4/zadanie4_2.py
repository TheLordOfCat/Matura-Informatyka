f = open("dane.txt" , "r")
data = f.read().split()

def convert(num, base):
    if num == 0:
        return 0

    b = ""
    while num > 0:
        b = str(num%base) + b
        num //= base

    return b

ans = 0

for d in data:
    n = convert(int(d), 2)

    isPal = True
    for i in range(0, int(len(n)/2)):
        if n[i] != n[len(n)-1-i]:
            isPal = False
            break

    indL = len(n)-1
    indR = 0
    for i in range(0, len(n)):
        if n[i] == "1":
            indR = i
            break
    for i in range(len(n)-1, -1, -1):
        if n[i] == "1":
            indL = i
            break

    isNearPal = True
    while indL > indR:
        if n[indR] != n[indL]:
            isNearPal = False
        indL -= 1
        indR += 1

    if isNearPal or isPal:
        ans += 1

print(ans)

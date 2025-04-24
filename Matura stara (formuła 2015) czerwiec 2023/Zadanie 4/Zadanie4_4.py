f = open("przyklad.txt", "r")
data = f.read().split()

ansNonZero = 0
ansSum = 0
ansNum = 0

for d in data:
    n = int(d,2)
    s = str(n)

    ok = True
    countDigits = [0]*10

    for l in s:
        if l == "0":
            ok = False
        countDigits[ord(l)-ord('0')] += 1

    if ok:
        ansNonZero += 1

    cur = 0
    for i in range(0, len(countDigits)):
        if countDigits[i] > 0:
            cur += i

    if cur > ansSum:
        ansSum = cur
        ansNum = n

print(ansNonZero)
print(ansNum)
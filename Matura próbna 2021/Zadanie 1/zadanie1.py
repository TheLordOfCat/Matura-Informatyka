def getBin(x):
    ans = ""
    while x > 0:
        ans = str(x%2) + ans
        x //= 2
    return ans

x = 16
y = 30
k = 5

X = getBin(x)
Y = getBin(y)

while len(X) < k:
    X = "0" + X

while len(Y) < k:
    Y = "0" + Y

for i in range(0, k):
    if X[i] == Y[i]:
        k -= 1
    else:
        break

print(k)
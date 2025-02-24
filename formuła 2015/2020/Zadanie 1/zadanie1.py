ok = True

A = [0, 4, 2, 4, 4, 2, 6]
B = [0, 4, 4, 2, 6, 4, 2]
k = 1
n = 6

for i in range(1, k+1):
    if not A[i] == B[n-k+i]:
        ok = False

for i in range(1, n-k+1):
    if not A[k+i] == B[i]:
        ok = False

print(ok)
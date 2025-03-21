A = [0, 4, 2, 4, 4, 2, 6]
B = [0, 4, 4, 2, 6, 4, 2]
n = 6
k = 1

ok = True
for i in range(1,k+1):
    if A[i] != B[n-k+i]:
        ok = False
        break

for i in range(k+1,n+1):
    if A[i] != B[i-k]:
        ok = False
        break

if ok:
    print("PRAWDA")
else:
    print("FALSZ")


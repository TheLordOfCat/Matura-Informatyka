A = [0,1,2,3,4,5,6,1,1]
C = [0,0,0,0,0,0,0,0, 0]
n = 8

for i in range(1, n+1):
    C[i] = 1
    for j in range(1, i):
        if A[j] < A[i] and C[j] + 1 > C[i]:
            C[i] = C[j] + 1

print(C)
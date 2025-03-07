n = 10

P = [None]*(n+1)
S = [None]*(n+1)

for i in range(1,n+1):
    P[i] = 1
    S[i] = 0

for j in range(2, n+1):
    if P[j] == 1:
        i = j*j
        while i <= n:
            P[i] = 0
            i = i+j
    S[j] = S[j-1] + P[j]

print(P)
print(S)

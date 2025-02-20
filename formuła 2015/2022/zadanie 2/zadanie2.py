# s = input()
s = 'a'*300+'b'*550 + 'a'*300 + 'b'*7 + 'a'*280 + 'b'*110

n = len(s)

A = [0]*(n+1)
for i in range(1, n+1):
    if s[i-1] == 'a':
        A[i] = A[i-1]+1
    else:
        A[i] = A[i-1]

B = [0]*(n+2)
for i in range(n, 0, -1):
    if s[i-1] == 'b':
        B[i] = B[i+1]+1
    else:
        B[i] = B[i+1]

k  = 1
for i in range(0, n+1):
    if A[i]+ B[i+1] > k:
        k = A[i] + B[i+1]

print(k)
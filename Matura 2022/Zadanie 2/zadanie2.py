s = "0"

for i in range(0, 300):
    s += "a"
for i in range(0, 550):
    s += "b"
for i in range(0, 300):
    s += "a"
for i in range(0, 7):
    s += "b"
for i in range(0, 280):
    s += "a"
for i in range(0, 110):
    s += "b"

n = len(s)-1

A = [0]*(n+2)

for i in range(1, n+1):
    if s[i] == "a":
        A[i] = A[i-1]+1
    else:
        A[i] = A[i-1]

B = [0]*(n+2)
B[n+1] = 0

for j in range(n, 0, -1):
    if s[j] == "b":
        B[j] = B[j+1]+1
    else:
        B[j] = B[j+1]

k = 1
for i in range(0, n+1):
    if A[i] + B[i+1] > k:
        k = A[i] + B[i+1]

print(k)

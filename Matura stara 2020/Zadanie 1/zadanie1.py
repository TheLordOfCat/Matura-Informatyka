A = [5, 8, 10, 14, 20, 12, 19, 23, 38, 30]
n = 10

i = 0
while i < n-1:
    if A[i] > A[i+1]:
        pom = A[i]
        A[i] = A[i+1]
        A[i+1] = pom
    i = i+2

i = 0
x = A[i]
y = A[i+1]
while i < n-3:
    if A[i+2] < x:
        x = A[i+2]
    if A[i+3] > y:
        y = A[i+3]
    i = i+2

print(x)
print(y)

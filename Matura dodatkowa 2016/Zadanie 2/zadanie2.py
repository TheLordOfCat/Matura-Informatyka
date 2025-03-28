A = [0, 27, 16, 7, 32, 10, 12]

for i in range(1, len(A)):
    for j in range(1, len(A)-1):
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp

ans = []
for i in range(0, len(A)):
    if A[i]%2 == 0:
        ans.append(A[i])

for i in range(len(A)-1, -1, -1):
    if A[i]%2 == 1:
        ans.append(A[i])

print(ans)
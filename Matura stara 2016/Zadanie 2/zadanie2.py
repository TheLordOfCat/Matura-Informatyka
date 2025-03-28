A = [0]
for i in range(0, 7):
    A.append(1)

# c = 0
six = 0
eight = 0

maX = 1
nr = 1
for i in range(1, len(A)):
    k = 0
    for j in range(i, len(A)):
        # c += 1
        if A[i] == A[j]:
            k += 1
            six += 1
    if k > maX:
        maX = k
        nr = i
        eight += 1

# print(A[nr])
# print(c)
print(six)
print(eight)
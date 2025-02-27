n = 10
A = [5, 99, 3, 7, 111, 13, 4, 24, 4, 8]

l = 1
r = n
w = -1

while l <= r:
    mid = int((l+r)/2)
    if A[mid]%2 == 0:
        w = A[mid]
        r = mid-1
    else:
        l = mid+1

print(w)



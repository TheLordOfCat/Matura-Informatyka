A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def f(p,q):
    if p != q:
        k = (q-p+1)//2
        for i in range(1, k+1):
            temp = A[p+i-1]
            A[p+i-1] = A[q-k+i]
            A[q-k+i] = temp
        print(A)
        f(p, p+k-1)
        f(q-k+1, q)

f(1, 10)
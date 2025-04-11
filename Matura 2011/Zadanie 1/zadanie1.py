def sklej(n):
    if n == 1:
        return 0
    if n%2 == 0:
        return n-1+2*sklej(n/2)
    else:
        return n-1+sklej((n-1)/2) + sklej((n+1)/2)

print(sklej(6))
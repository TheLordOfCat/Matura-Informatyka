n = 9999

for i in range(n-37, n):
    sum = i
    dig = 0
    c = i
    while c>0:
        dig += c%10
        c //= 10

    if sum + dig == n:
        print(i)
        break
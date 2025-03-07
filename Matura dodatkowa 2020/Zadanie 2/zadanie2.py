a = 5
b = 6

n = []

while a > 0:
    low = b/a
    num = 0
    while num < low:
        num += 1
    n.append(num)
    if b%num == 0:
        a = a - b/num
    else:
        a *= num
        a -= b
        b *= num

print(n)
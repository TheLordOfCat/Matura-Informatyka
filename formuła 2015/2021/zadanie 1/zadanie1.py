n = 2021
a = 0
m = 1
d = 0

while m < n:
    l = n % (m * 10) - a
    l = l / m
    d += m * (9 - l)
    a += m * l
    m = m * 10

print(d)
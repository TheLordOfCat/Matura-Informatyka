a = 0
b = 2
d = 0.5

def f(x):
    return x*x*x-x-2

while b-a > d and f((b-a)/2) != 0:
    if (b-a)/2 * a > 0:
        b = (b+a)/2
    else:
        a = (b+a)/2

print((b-a)/2)
print(a)
print(b)
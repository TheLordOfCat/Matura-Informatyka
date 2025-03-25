n = 76
s = str(n)
temp = (n*n)%(10**(len(s)))

if n == temp:
    print("Tak")
else:
    print("NIE")
n = int("132",4) + int("3111",4)

base = 16
digits = []

ans = ''

while n:
    rem = n%base
    if rem < 10:
        digits.append(str(rem))
    else:
        digits.append(chr(ord('A') + rem - 10))
    n //= base

ans = ''.join(digits[::-1])

print(ans)

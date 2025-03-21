def convert(num, base):
    if num == 0:
        return 0
    ans = 0
    while num > 0:
        ans = num%base + ans*10
        num //= base
    return ans

L = 0
n = 259
while n > 0:
    dig = n%10
    n //= 10

    binVer = convert(dig, 2)
    while binVer > 0:
        if binVer % 10 == 1:
            L += 1
        binVer //= 10

print(L)
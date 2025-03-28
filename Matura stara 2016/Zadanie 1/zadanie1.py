def convert(num, base):
    if num == 1:
        return 1

    digits = "0123456789ABCDEF"

    ans = ""
    while num > 0:
        ans = digits[num%base] + ans
        num //= base

    return ans

n = int("10000000000000000000", 2)
print(len("10000000000000000000"))
print(len(convert(n, 4)))
print(len(convert(n, 8)))
print(len(convert(n, 16)))
print(len(convert(n, 10)))
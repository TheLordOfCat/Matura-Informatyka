# n = 6
# suma = 0
#
# if n == 1:
#     suma = 1
# else:
#     suma = 1 + n
#     i = n-1
#     while i > 1:
#         suma = 1 + i*suma
#         i = i-1
#
# print(suma)

def convert(n, base):
    ans = ""
    if n == 1:
        return "1"

    digits = "0123456789ABCDEF"

    while n >= 1:
        ans = digits[n%base] + ans
        n //= base

    return ans

print(convert(int("101011111100", 2), 16))
# print(int("11001001",2) - int("1111110",2))
#
# print(int("4C", 16))
# print(int("113", 8))
# print(int("1023", 4))
# print(int("1001010",2))

def convert(n, base):
    if n == 0:
        return "0"

    numbers = "0123456789ABCDEF"
    ans = ""
    while n > 0:
        ans = numbers[n%base] + ans
        n //= base
    return ans

# print(int("1000000000000000",2))
print(len(convert(32768, 4)))
print(len(convert(32768, 8)))
print(len(convert(32768, 16)))
print(len(convert(32768, 10)))
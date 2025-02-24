#A
print(int("10",2), end = "")
print(int("10",2), end = ":")
print(int("11",2), end = "")
print(int("100",2), end = ":")
print(int("100",2), end = "")
print(int("1001",2))

#B
print(int("00",2), end = "")
print(int("111",2), end = ":")
print(int("101",2), end = "")
print(int("1000",2), end = ":")
print(int("11",2), end = "")
print(int("101",2))

#C
print(int("1",2), end = "")
print(int("0",2), end = ":")
print(int("100",2), end = "")
print(int("100",2), end = ":")
print(int("10",2), end = "")
print(int("100",2))

#D
print(int("1",2), end = "")
print(int("111",2), end = ":")
print(int("100",2), end = "")
print(int("1001",2), end = ":")
print(int("101",2), end = "")
print(int("10",2))


n = 11111
w = 0

while n != 0:
    # print(w)
    w = w+(n%10)
    n = n//10

print(w)
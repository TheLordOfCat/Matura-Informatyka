def fibonacci(k):
    if k < 3:
        return 1
    else:
        return (fibonacci(k-1) + fibonacci(k-2))%26

s = "NIEPRZYJACIELNADCHODZI"
d = len(s)
szyfr = ""
for i in range(0, d):
    if s[i] >= "A" and s[i] <= "Z":
        szyfr += chr(65+(ord(s[i]) -65 + fibonacci(i+1))%26)

print(szyfr)
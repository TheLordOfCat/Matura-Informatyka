# l = ["100001", "110011", "111111", "101101"]
#
# for n in l:
#     print(n + " | " + str(int(n, 2)))

n = 1000000
ans = 0
for num in range(1, n):
    okDecimal = True
    s = str(num)
    sRev = ""
    for j in range(0, len(s)):
        sRev += s[len(s)-j-1]

    if sRev != s:
        okDecimal = False

    okBinary = True
    sB = str(bin(num))
    s = ""
    for j in range(2, len(sB)):
        s += sB[j]
    sRev = ""
    for j in range(0, len(s)):
        sRev += s[len(s)-j-1]

    if sRev != s:
        okBinary = False

    if okBinary and okDecimal:
        ans += num

print(ans)
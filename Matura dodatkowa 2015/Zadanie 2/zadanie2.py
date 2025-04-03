# cPos = [2, 3, 5, 6, 9, 10, 11, 13, 14, 15, 17, 19, 20, 23, 24]
#
# a = 5
# b = 15
#
# ans = 0
# for i in range(0, len(cPos)):
#     c = cPos[i]
#     if b-a < c and b+a>c:
#         ans += 1
# print(ans)

c = [5, 15, 2, 3, 6, 9, 10, 11, 13, 14, 17, 19, 20, 23, 24]

ans = 0
for i in range(0, len(c)):
    a = 5
    b = 15
    if b-a < c[i] and b+a>c[i]:
        ans += 1
print(ans)

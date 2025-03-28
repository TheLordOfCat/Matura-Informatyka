f = open("liczby.txt", "r")
data = f.read().split()
#
# ans = 0
# for d in data:
#     if d[-1] == "8":
#         ans += 1
#
# print(ans)

# ans = 0
# for d in data:
#     if d[-1] == "4":
#         ok = True
#         for i in range(0, len(d)-1):
#             if d[i] == "0":
#                 ok = False
#                 break
#         if ok:
#             ans += 1
#
# print(ans)

# ans = 0
# for d in data:
#     if d[-1] == "2":
#         dS = ""
#         for i in range(0, len(d)-1):
#             dS = dS + d[i]
#         num = int(dS, 2)
#         if num%2 == 0:
#             ans += 1
#
# print(ans)

# ans = 0
# for d in data:
#     if d[-1] == "8":
#         dS = ""
#         for i in range(0, len(d)-1):
#             dS = dS + d[i]
#         num = int(dS, 8)
#         ans += num
# print(ans)

ansMax = 0
orgMax = ""
ansMin = 1000000000000000000000000000
orgMin = ""

for d in data:
    dS = ""
    for i in range(0, len(d)-1):
        dS = dS + d[i]
    num = int(dS, int(d[-1]))
    if ansMax < num:
        ansMax = num
        orgMax = d
    if ansMin > num:
        ansMin = num
        orgMin = d

print(ansMax)
print(orgMax)
print(ansMin)
print(orgMin)

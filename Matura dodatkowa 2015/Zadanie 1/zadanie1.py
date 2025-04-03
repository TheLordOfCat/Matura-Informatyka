allOps = []

def getOps(s):
    if len(s) == 8:
        allOps.append(s)
    else:
        getOps(s+"0")
        getOps(s+"1")

getOps("")

for i in range(0, len(allOps)):
    n = 7
    s = allOps[i]
    val = 0
    if s[0] == "1":
        val = (-1)*(2**n)
    n -= 1
    for j in range(1, len(s)):
        if s[j] == "1":
            val += 2**n
        n -= 1
    if val == 93:
        print(allOps[i])
    elif val == -42:
        print(allOps[i])


# n = 16
# aRev = [1,1,1,1,0,0,1,0,0,1,1,1,0,0,0,0]
# a = []
# for i in range(len(aRev)-1, -1, -1):
#     a.append(aRev[i])
#
# b = [0]*len(aRev)
#
# i = 0
# while a[i] == 0:
#         b[i] = 0
#         i = i+1
# b[i] = a[i]
# i = i+1
# while i < n:
#     if a[i] == 1:
#         b[i] = 0
#     else:
#         b[i] = 1
#     i = i+1
#
# print(b)
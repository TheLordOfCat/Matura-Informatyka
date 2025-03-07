n = 17
T = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

ops = 0
def Rek(x, p, k):
    global ops
    ops += 1
    if p<k:
        s = (p+k)//2
        if T[s] >= x:
            return Rek(x,p,s)
        else:
            return Rek(x, s+1, k)
    else:
        if T[p] == x:
            return p
        else:
            return -1

print(Rek(2020,5,14))
print(ops)

# n = 11
# T = [0,1,5,8,10,12,14,19,20,23,30,38]
#
# def Rek(x, p, k):
#     print(str(x) + " " + str(p) + " " + str(k))
#     if p<k:
#         s = (p+k)//2
#         if T[s] >= x:
#             return Rek(x,p,s)
#         else:
#             return Rek(x, s+1, k)
#     else:
#         if T[p] == x:
#             return p
#         else:
#             return -1
#
# print(Rek(7,1,11))
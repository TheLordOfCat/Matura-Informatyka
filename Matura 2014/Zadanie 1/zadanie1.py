# ans = []
# def Korale(n):
#     global ans
#     if n == 1:
#         ans.append('c')
#     elif n%2 == 0:
#         Korale(n/2)
#         ans.append('b')
#     else:
#         Korale((n-1)/2)
#         ans.append('c')
#
# Korale(16)

def KoraleBis(n):
    ans = []
    cur = n
    while cur > 1:
        if n%2 == 0:
            ans.append('b')
            cur = cur/2
        else:
            ans.append('c')
            cur = (cur-1)/2
    ans.append('c')

    return ans


print(KoraleBis(4))
# def F(n):
#     ans1 = 1
#     ans2 = 1
#     for i in range(3, n+1):
#         temp = ans2 + ans1
#         ans1 = ans2
#         ans2 = temp
#     return ans2

def F(n):
    if n == 1 or n== 2:
        return 1

    ans = 0
    if n%2 == 0:
        k = int(n/2)
        temp1 = F(k+1)
        temp2 = F(k-1)
        ans = temp1*temp1 - temp2*temp2
    else:
        k = int((n+1)/2)
        temp1 = F(k)
        temp2 = F(k-1)
        ans = temp1*temp1+ temp2*temp2

    return ans

print(F(5))
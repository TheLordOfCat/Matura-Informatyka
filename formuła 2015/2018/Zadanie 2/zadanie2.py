X = [1,3,2,-2]
Y = [3,4,1,2]

ans = 0
# n = 4
#
# for i in range(1, n):
#     if X[i]/Y[i]  < X[ans]/Y[ans]:
#         ans = i
#
# print(ans+1)

n = 4
ans = [1,2,3,4]

for i in range(1, n):
    for j  in range(0, n-1):
        if X[ans[j+1]-1] / Y[ans[j+1]-1] < X[ans[j]-1] / Y[ans[j]-1]:
            temp = ans[j]
            ans[j] = ans[j+1]
            ans[j+1] = temp

print(ans)
ans = 0
def sym(a,b):
    global ans
    if a != 0:
        sym(a-1, b+1)
        # print(a*b, end = " ")
        ans += 1
        sym(a-1, b+1)

sym(10,2020)
print(ans)
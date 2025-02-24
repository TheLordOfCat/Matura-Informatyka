ans = []

def sym(a, b):
    global ans
    if not a == 0:
        sym(a-1, b+1)
        # print(a*b, end = " ")
        ans.append(a*b)
        sym(a-1, b+1)

sym(10, 2020)
print(len(ans))
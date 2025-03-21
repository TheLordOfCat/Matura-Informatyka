changeP = 0
changeK = 0

def F(T,x):
    global changeP
    global changeK

    p = 1
    k = n

    while p<=k:
        s = (p+k)//2
        # changeP += 1
        # print(s)
        if T[s] == x:
            return True
        else:
            if T[s] < x:
                p = s+1
                # changeP += 1
            else:
                k = s-1
                # changeK += 1
    return False

n = 10
T = [0, 3, 5, 7, 8, 90, 13, 33, 37, 40, 43]
# for i in range(0,100):
#     T.append(1)
x = 43

print(F(T,x))
# print(changeP)

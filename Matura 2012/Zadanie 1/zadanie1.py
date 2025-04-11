a = [5,1,8,9,7, 2,3,11, 20,15]
n = len(a)

# a = [1]*2012
# n = len(a)

ans = 0

def F(i):
    global n
    global ans
    if i == n:
        return n
    else:
        j = F(i+1)
        ans += 1
        if a[i-1] < a[j-1]:
            return i
        else:
            return j

F(512)
print(ans)
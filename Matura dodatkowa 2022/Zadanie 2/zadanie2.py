ans = 0

def Koduj(n):
    global ans
    ans += 1
    if n == 1:
        return ""
    else:
        k = n//2
        if k%2 == 0:
            return Koduj(k)+"A"
        else:
            return "B" + Koduj(k)

# t = [1,2,12,33,158]
t = [1,2,12,33,1022]
for i in t:
    ans = 0
    Koduj(i)
    print(ans)

# print(Koduj(64))
# print(Koduj(65))
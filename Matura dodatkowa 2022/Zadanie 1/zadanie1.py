def SumaKwCyfr(n):
    ans = 0
    for l in str(n):
        ans += int(l)*int(l)
    return ans

t = 82
for i in range(0, 100):
    temp = SumaKwCyfr(t)
    print(temp)
    t = temp
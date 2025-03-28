f = open("binarne.txt", "r")
data = f.read().split()

ans = 0
longest = ""
for d in data:
    ok = True
    if len(d)%2 == 0:
        mid = int(len(d)/2)
        for i in range(0, mid):
            if d[i] != d[i+mid]:
                ok = False
                break
    else:
        mid = int((len(d)+1)/2)
        for i in range(0, mid):
            if d[i] != d[i+1+mid]:
                ok = False
                break
    if ok:
        ans += 1
        if len(d) > len(longest):
            longest = d

print(ans)
print(longest)
print(len(longest))


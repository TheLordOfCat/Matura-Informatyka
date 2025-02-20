seq = [1,4,2,5]

exi = [False] * (len(seq)+1)

for s in seq:
    if s <= len(seq):
        exi[s] = True

ans = 0
for i in range(1, len(seq)+1):
    if exi[i] == False:
       ans += 1

print(ans)
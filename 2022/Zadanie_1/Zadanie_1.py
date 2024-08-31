perm = [8, 4, 9, 6, 5, 7]
count = [0]*(len(perm)+1)

for i in perm:
    if not (i > len(perm)):
        count[i] = count[i] + 1

ans = 0
for i in range(1, len(count)):
    if count[i] == 0:
        ans = ans + 1

print(ans)
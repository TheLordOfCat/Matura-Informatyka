n = 50
ind = 0

ans1 = []
while (1<<ind) < n:
    if (1<<ind) & n:
        ans1.append(1<<ind)
    ind += 1

ans2 = []
val = 1
while (val*2) < n:
    val *= 2

while val > 0:
    if val <= n:
        n -= val
        ans2.append(val)
    val //= 2

print(ans1)
print(ans2)
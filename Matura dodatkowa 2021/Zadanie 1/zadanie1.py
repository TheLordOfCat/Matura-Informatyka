n = 23

ans = 0
ind = n
while n > 0:
    while n < ind*ind:
        ind -= 1
    ans += 1
    n -= ind*ind

print(ans)
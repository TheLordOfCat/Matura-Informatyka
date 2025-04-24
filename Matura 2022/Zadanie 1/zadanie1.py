c = [8, 4, 9, 6, 5, 7]
n = len(c)

nums = [0]*(n+1)

for i in range(0, len(c)):
    if c[i] < len(nums):
        nums[c[i]] += 1

ans = 0
for i in range(1, len(nums)):
    if nums[i] == 0:
        ans += 1

print(ans)
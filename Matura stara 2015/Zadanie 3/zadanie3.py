Tab = [
    [1, 1, 4, 4],
    [2,2,3,3],
    [3,3,2,2],
    [4,4,1,1]
]

k = 1
s = 0
w = 0

while w != 4:
    w = w+1
    s = s+Tab[w-1][k-1]

print(s)
print(w)
print(k)
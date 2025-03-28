p = [0, 1, 1, 2, 4]

for i in range(5,10):
    sum = 0
    for j in range(i-5, i):
        sum += p[j]
    p.append(sum)

print(p)
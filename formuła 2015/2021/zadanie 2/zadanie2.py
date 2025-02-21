T = [0]
n = 0

ans = 0

def d(x):
    global n
    global ans

    n += 1
    T.append(x)
    s = n
    ans += 1
    while s//2 >= 1 and T[s] > T[s//2]:
        ans += 1

        pom = T[s]
        T[s] = T[s//2]
        T[s//2] = pom
        s = s//2

k = 1025

for i in range(1, k):
    d(i)

ans = 0
d(k)

print(ans)


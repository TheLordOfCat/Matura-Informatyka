f = open("pary.txt", "r")
data = f.read().split()

primes = []
used = [False]*(101)
for i in range(2, 101):
    if used[i] == False:
        primes.append(i)
        for j in range(i*2, 101, i):
            used[j] = True

ans = []

for i in range(0, len(data), 2):
    num = data[i]
    s = data[i+1]

    if int(num)%2 == 1:
        continue

    temp = [0,0]
    for j in range(0, len(primes)):
        for o in range(j, len(primes)):
            if primes[j] + primes[o] == int(num):
                if o - j >= temp[1]- temp[0] :
                    temp = [primes[j], primes[o]]
    ans.append(temp)

print(ans)


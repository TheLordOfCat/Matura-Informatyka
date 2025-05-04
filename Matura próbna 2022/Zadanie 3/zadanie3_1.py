f = open("liczby.txt", "r")
data = f.read().split()

primes = [True]*1000005
for i in range(2, len(primes)):
    if primes[i] == True:
        for j in range(2*i, len(primes), i):
            primes[j] = False

ans = 0
for d in data:
    num = int(d)
    if primes[num-1] == True:
       ans += 1

print(ans)
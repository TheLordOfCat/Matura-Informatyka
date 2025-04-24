f = open("liczby.txt", "r")
data = f.read().split()


primes = [True]*10000
for i in range(2, len(primes)):
    if primes[i] == True:
        for j in range(2*i, len(primes), i):
            primes[j] = False

ans = 0
ansDist = 0

for d in data:
    dRev = ""
    for i in range(len(d)-1, -1, -1):
        dRev += d[i]

    if primes[int(dRev)] == True and primes[int(d)] == True:
        print(d)

f = open("liczby_przyklad.txt", "r")
data = f.read().split()

primes = [True]*1000005
primes[0] = False
primes[1] = False

for i in range(2, len(primes)):
    if primes[i] == True:
        for j in range(2*i, len(primes), i):
            primes[j] = False

ansMinNum = 0
ansMin = 10000000000
ansMaxNum = 0
ansMax = 0

for d in data:
    num = int(d)
    resPrimes = []

    cur = 0
    for i in range(2, num):
        if primes[i] == True and primes[num-i] == True:
            cur += 1

    if cur > ansMax:
        ansMax = cur
        ansMaxNum = num

    if cur < ansMin:
        ansMin = cur
        ansMinNum = num

print(ansMaxNum)
print(ansMax)

print(ansMinNum)
print(ansMin)

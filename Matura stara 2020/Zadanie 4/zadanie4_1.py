f = open("dane_przyklad.txt" , "r")
data = f.read().split()

ans = []
for d in data:
    num = int(d)

    prime = True

    for i in range(2, num):
        if num%i == 0:
            prime = False
            break

    if prime:
        ans.append(num)

maxPrime = 0
minPrime = 100000

for num in ans:
    maxPrime = max(maxPrime, num)
    minPrime = min(minPrime, num)


print(len(ans))
print(maxPrime)
print(minPrime)
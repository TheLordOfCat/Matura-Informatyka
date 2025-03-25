f = open("punkty.txt", "r")
data = f.read().split("\n")

def isPrime(n):
    prime = True
    for i in range(2, n):
        if n%i == 0:
            prime = False
            break
    return prime

ans = 0
for l in data:
    num = l.split(" ")
    ok1 = isPrime(int(num[0]))
    ok2 = isPrime(int(num[1]))
    if ok1 and ok2:
        ans += 1

print(ans)
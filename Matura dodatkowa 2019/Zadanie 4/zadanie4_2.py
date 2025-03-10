f = open("pierwsze.txt" , "r")
data = f.read().split()

ans = []
for d in data:
    dRev = ""
    for l in range(len(d)-1, -1, -1):
        dRev = dRev + d[l]

    num = int(dRev)
    prime = True
    for n in range(2, num):
        if num % n == 0:
            prime = False
            break

    if prime:
        ans.append(d)

print(ans)

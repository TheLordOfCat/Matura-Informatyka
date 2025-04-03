f = open("dziennik.txt", "r")
data = f.read().split()

cons = 0
last = 0
ans = 0
l = 0

f = int(data[0])
s = 0

for i in range(0, len(data)):
    if last < int(data[i]):
        cons += 1
        s = int(data[i])
    else:
        if cons > ans:
            ans = cons
            l = s-f

        f = int(data[i])
        s = int(data[i])
        cons = 1
    last = int(data[i])

print(ans)
print(l)
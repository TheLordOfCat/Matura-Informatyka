f = open("dziennik.txt", "r")
data = f.read().split()

cons = 0
last = 0
ans = 0
for i in range(0, len(data)):
    if last < int(data[i]):
        cons += 1
    else:
        if cons > 3:
            ans += 1
        cons = 1
    last = int(data[i])
        
print(ans)
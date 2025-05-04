f = open("slowa.txt" , "r")
data = f.read().split()

ans = 0

for d in data:
    for i in range(0, len(d)-2):
        if d[i] == "k" and d[i+2] == "t":
            ans += 1


print(ans)
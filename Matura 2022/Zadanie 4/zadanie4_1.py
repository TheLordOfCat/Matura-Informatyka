f = open("przyklad.txt", "r")
data = f.read().split()

ansFirst = ""
for d in data:
    if d[0] == d[len(d)-1]:
       ans = d
       break

print(ans)
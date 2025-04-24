f = open("liczby.txt", "r")
data = f.read().split()

ansFirst = ""
ansCount = 0

for d in data:
    if d[0] == d[len(d)-1] and ansFirst == "":
       ansFirst = d
    if d[0] == d[len(d)-1]:
       ansCount += 1

print(ansCount)
print(ansFirst)
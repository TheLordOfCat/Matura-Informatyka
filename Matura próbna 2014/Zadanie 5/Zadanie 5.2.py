f = open("dziennik.txt", "r")
data = f.read().split()

ansLong = int(data[0])
ansShort = int(data[0])

for i in range(0, len(data)):
    ansLong = max(ansLong, int(data[i]))
    ansShort = min(ansShort, int(data[i]))

print(ansLong)
print(ansShort)
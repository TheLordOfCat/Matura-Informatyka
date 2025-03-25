f = open("punkty.txt", "r")
data = f.read().split("\n")

ansIn = 0
ansEdge = 0
ansOut = 0

for i in range(0, len(data)):
    num = data[i].split(" ")

    x = int(num[0])
    y = int(num[1])

    if (-5000 < x < 5000) and (-5000 < y < 5000):
        ansIn += 1
    elif (x > 5000 or x < -5000) or (y > 5000 or y < -5000):
        ansOut += 1
    else:
        ansEdge += 1

print(ansIn)
print(ansEdge)
print(ansOut)

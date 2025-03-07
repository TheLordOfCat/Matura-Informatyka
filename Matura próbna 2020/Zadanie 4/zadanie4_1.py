f = open("dane4.txt" , "r")
data = f.read().split()

bigDif = int(data[0])-int(data[1])
smallDif = int(data[0]) - int(data[1])

for i in range(1, len(data)-1):
    dif = int(data[i+1]) - int(data[i])
    if dif < 0:
        dif *= (-1)
    bigDif = max(bigDif, dif)
    smallDif = min(smallDif, dif)

print(smallDif)
print(bigDif)
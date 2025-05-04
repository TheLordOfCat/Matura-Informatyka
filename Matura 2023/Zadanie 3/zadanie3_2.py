f = open("pi_przyklad.txt", "r")
data = f.read().split()

ans = 0
count = [0]*101
for i in range(0, len(data)-1):
    num1 = data[i]
    num2 = data[i+1]

    numS = num1 + num2
    num = int(numS)

    count[num] += 1

ansMin = 0
ansMinVal = 10000000
ansMax = 0
ansMaxVal = 0

for i in range(0, len(count)-1):
    if ansMaxVal < count[i]:
        ansMax = i
        ansMaxVal = count[i]

    if ansMinVal > count[i]:
        ansMin = i
        ansMinVal = count[i]

print(ansMin)
print(ansMinVal)

print(ansMax)
print(ansMaxVal)
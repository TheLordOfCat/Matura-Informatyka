f = open("mecz.txt", "r")
data = f.read().split()

countSeries = 0
curType = ""

ans = 0
ansLongest = 0
ansType = ""

for d in data[0]:
    if curType != d:
        if countSeries >= 10:
            ans += 1
            if countSeries > ansLongest:
                ansLongest = countSeries
                ansType = curType

        curType = d
        countSeries = 1
    else:
        countSeries += 1

if countSeries >= 10:
    ans += 1
    if countSeries > ansLongest:
        ansLongest = countSeries
        ansType = curType

print(ans)
print(ansType)
print(ansLongest)
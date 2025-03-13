f = open("galerie.txt" , "r")
data = f.read().split("\n")

minArea = 10000
minName = ""

maxArea = 0
maxName = ""

for d in data:
    sen = d.split(" ")

    countArea = []

    for i in range(2, len(sen), 2):
        if int(sen[i]) != 0:
            area = int(sen[i])*int(sen[i+1])
            f = False
            for j in range(0, len(countArea)):
                if countArea[j] == area:
                    f = True
                    break
            if f == False:
                countArea.append(area)

    if minArea > len(countArea):
        minArea = len(countArea)
        minName = sen[1]

    if maxArea < len(countArea):
        maxArea = len(countArea)
        maxName = sen[1]

print(maxName + " " + str(maxArea))
print(minName + " " + str(minArea))


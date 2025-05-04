f = open("mecz.txt", "r")
data = f.read().split()

pointsA = 0
pointsB = 0
for i in range(0, len(data[0])):
    if data[0][i] == "A":
        pointsA += 1
    elif data[0][i] == "B":
        pointsB += 1

    if pointsA >= 1000 or pointsB >= 1000:
        dif = pointsA - pointsB
        if dif < 0:
            dif *= -1

        if dif >= 3:
            print(pointsA)
            print(pointsB)
            break
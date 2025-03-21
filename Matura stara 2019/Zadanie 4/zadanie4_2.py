f = open("przyklad.txt" , "r")
data = f.read().split("\n")

def procesPlane(plane1, plane2):
    ok = True

    for i in range(0, len(plane1)):
        for j in range(0, len(plane1[i])):

            for o in range(0, len(plane2)):
                for k in range(len(plane2[o])-1, -1, -1):
                    if plane1[i][j] != plane[o][k]:
                        ok = False
                        break
                if not ok:
                    break

            if not ok:
                break
        if not ok:
            break
    
    return ok

plane = []
planeList = []
for i in range(0, len(data)):
    if data[i] != "":
        plane.append(data[i])
    else:
        planeList.append(plane)
        plane.clear()

for i in range(0, len(planeList)):
    for j in range(i, len(planeList)):
        if procesPlane(planeList[i], planeList[j]):
            print(str(i+1) + " " + str(j+1))


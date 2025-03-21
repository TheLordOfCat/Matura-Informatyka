f = open("dzialki.txt" , "r")
data = f.read().split("\n")

ans = 0
def procesPlane(plane):
    global ans
    totalSize = 0
    grassSize = 0
    for i in range(0, len(plane)):
        for j in range(0, len(plane[i])):
            totalSize += 1
            if plane[i][j] == "*":
                grassSize += 1

    ratio = grassSize/totalSize
    if ratio >= 0.7:
        ans += 1

plane = []
for i in range(0, len(data)):
    if data[i] != "":
        plane.append(data[i])
    else:
        procesPlane(plane)
        plane.clear()


print(ans)

f = open("liczby.txt", "r")
data = f.read().split()

ansS = 0
ansB = 0

for i in range(0, len(data)):
    if len(data[i]) > len(data[ansB]):
        ansB = i
    if len(data[i]) < len(data[ansS]):
        ansS = i

    if len(data[i]) == len(data[ansB]):
        for j in range(0, len(data[i])):
            if data[i][j] == "1" and data[ansB][j] == "0":
                ansB = i
                break
            elif data[i][j] == "0" and data[ansB][j] == "1":
                break

    if len(data[i]) == len(data[ansS]):
        for j in range(0, len(data[i])):
            if data[i][j] == "0" and data[ansS][j] == "1":
                ansS = i
                break
            elif data[i][j] == "1" and data[ansS][j] == "0":
                break

print(ansS+1)

print(ansB+1)

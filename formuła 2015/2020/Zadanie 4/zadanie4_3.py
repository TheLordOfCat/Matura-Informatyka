f = open("pary.txt", "r")
data = f.read().split()

minNum = 1000
minS = "a"*1000

for i in range(0, len(data), 2):
    num = int(data[i])
    s = data[i+1]

    if num < minNum:
        minNum = num
        minS = s
    elif num == minNum:
        equal = True
        for j in range(0, min(len(s), len(minS))):
            if ord(s[j]) < ord(minS[j]):
                equal = False
                minNum = num
                minS = s
            elif ord(s[j]) > ord(minS[j]):
                break

        if equal and len(s) < len(minS):
            minNum = num
            minS = s

print(minNum)
print(minS)

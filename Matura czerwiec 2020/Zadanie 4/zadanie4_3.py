f = open("pary.txt" , "r")
data = f.read().split()


ansNum = 10000
ansStr = ""

for i in range(0, len(data), 2):
    d = int(data[i])
    s = data[i+1]

    if len(s) != d:
        continue

    if d < ansNum:
        ansNum = d
        ansStr = s
    elif d == ansNum:
        found = False
        for j in range(0, min(len(ansStr), len(s))):
            if s[j] < ansStr[j]:
                ansNum = d
                ansStr = s
                found = True
                break

        if found == False:
            if len(ansStr) > len(s):
                ansNum = d
                ansStr = s
                found = True

print(ansNum)
print(ansStr)
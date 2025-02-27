f = open("sygnaly.txt", "r")
data = f.read().split()

ans = ""
ansVal = 0

for d in data:
    countLeters = [0]*26
    for l in d:
        countLeters[ord(l)-ord("A")]+= 1
    dif = 0
    for l in countLeters:
        if l > 0:
            dif += 1

    if dif > ansVal:
        ans = d
        ansVal = dif

print(ans)
print(ansVal)
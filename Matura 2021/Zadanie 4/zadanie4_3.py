f = open("instrukcje.txt", "r")
data = f.read().split()

letterCount = [0]*27

for i in range(0, len(data), 2):
    ops = data[i]
    l = data[i+1]

    if ops == "DOPISZ":
        letterCount[ord(l)-ord("A")] += 1

ans = ""
ansCount = 0
for i in range(0, len(letterCount)):
    if letterCount[i] > ansCount:
        ans = chr(ord("A")+i)
        ansCount = letterCount[i]

print(ans)
print(ansCount)
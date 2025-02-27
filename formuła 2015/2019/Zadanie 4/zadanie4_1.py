f = open("liczby.txt", "r")
data = f.read().split()

maxVal = 100002

powers  = []

three = 1
while three <= maxVal:
    powers.append(three)
    three *= 3

ans = []
for d in data:
    for i in range(0, len(powers)):
        if int(d) == powers[i]:
            ans.append(int(d))

print(len(ans))
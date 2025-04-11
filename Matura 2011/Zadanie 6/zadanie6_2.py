f = open("liczby.txt", "r")
data = f.read().split()

ansT = 0
ansD = ""
for d in data:
    t = int(int(d, 2))
    if t > ansT:
        ansT = t
        ansD = d

print(ansT)
print(ansD)
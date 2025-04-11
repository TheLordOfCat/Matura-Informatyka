tekst = ["$", "A","L", "G","O", "R", "Y", "T", "M", "_", "P", "R", "Z", "E", "S", "T", "A", "W", "I", "E", "N", "I", "O", "W", "Y"]
d = len(tekst)

tab = []
l = 1
while (l+1)*(l+1) <= d:
    l += 1

if l*l < d:
    l += 1

t = []
for i in range(1, len(tekst)):
    if len(t) == l:
        tab.append(t.copy())
        t.clear()
    t.append(tekst[i])

if len(t) != 0:
    while len(t) < l:
        t.append("_")
    tab.append(t)

szyfr = []
for i in range(0, l):
    for j in range(0, l):
        szyfr.append(tab[j][i])

print(szyfr)


f = open("anagram.txt", "r")
data = f.read().split()

ans = []
for i in range(0, len(data), 5):
    ok = True
    l = len(data[i])
    for j in range(1, 5):
        if l != len(data[i+j]):
            ok = False

    if ok:
        t = []
        for j in range(0, 5):
            t.append(data[i+j])
        ans.append(t)

for a in ans:
    print(a)
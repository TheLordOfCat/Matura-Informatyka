f = open("anagram.txt", "r")
data = f.read().split()

ans = []
for i in range(0, len(data), 5):
    ok = True
    base = [0]*26
    for l in data[i]:
        base[ord(l) - ord("a")] += 1

    for j in range(1, 5):
        cur = [0]*26
        for l in data[i+j]:
            cur[ord(l) - ord("a")] += 1

        for k in range(0, len(base)):
            if base[k] != cur[k]:
                ok = False

    if ok:
        t = []
        for j in range(0, 5):
            t.append(data[i+j])
        ans.append(t)

for a in ans:
    print(a)
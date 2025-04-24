f = open("liczby.txt", "r")
data = f.read().split()

vis = [0]*1001
for i in range(1, 1000):
    if vis[i] == 0:
        seq = [i]

        ok = True
        while ok:
            s = str(seq[-1])
            cur = 0
            for j in range(0, len(s)):
                cur += int(s[j])*int(s[j])

            if cur == 1:
                for j in range(0, len(seq)):
                    vis[seq[j]] = 1
                    ok = False
            else:
                for j in range(0, len(seq)):
                    if seq[j] == cur:
                        ok = False
                        break

                if ok == False:
                    for j in range(0, len(seq)):
                        vis[seq[j]] = 2

            seq.append(cur)
print(vis)
f = open("binarne.txt", "r")
data = f.read().split()

ans = 0
ansBin = ""
for d in data:
    n = int(d, 2)
    if n > 65535:
        continue
    if ans < n:
        ans = n
        ansBin = d

print(ans)
print(ansBin)

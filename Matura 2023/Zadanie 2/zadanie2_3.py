f = open("bin_przyklad.txt", "r")
data = f.read().split()

ans = "0"

for d in data:
    if int(d, 2) > int(ans, 2):
        ans = d

print(ans)
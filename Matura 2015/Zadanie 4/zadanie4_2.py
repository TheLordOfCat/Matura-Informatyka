f = open("liczby.txt", "r")
data = f.read().split()

ans2 = 0
ans8 = 0

for d in data:
    if len(d) >= 2:
        if d[len(d)-1] == "0":
            ans2 += 1

    if len(d) >= 4:
        if d[len(d)-1] == "0" and d[len(d)-2] == "0" and d[len(d)-3] == "0":
            ans8 += 1

    if d == "0":
        ans2 += 1
        ans8 += 1

print(ans2)
print(ans8)

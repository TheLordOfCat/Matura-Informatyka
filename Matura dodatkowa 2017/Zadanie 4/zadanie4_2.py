f = open("punkty.txt", "r")
data = f.read().split("\n")

ans = 0
for l in data:
    num = l.split(" ")

    dig1 = [False]*10
    dig2 = [False]*10

    for i in range(0, len(num[0])):
        dig1[int(num[0][i])] = True
    for i in range(0, len(num[1])):
        dig2[int(num[1][i])] = True

    ok = True
    for i in range(0, 10):
        if dig1[i] != dig2[i]:
            ok = False

    if ok:
        ans += 1


print(ans)
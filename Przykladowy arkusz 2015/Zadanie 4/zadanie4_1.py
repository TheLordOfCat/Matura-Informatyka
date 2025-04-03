f = open("dane_anagramy.txt", "r")
data = f.read().split()

ans = 0
for i in range(0, len(data), 2):
    digits = [0,0,0,0,0, 0,0,0,0,0]
    for d in data[i]:
        digits[int(d)] += 1
    for d in data[i+1]:
        digits[int(d)] -= 1

    ok = True
    for j in range(0, len(digits)):
        if digits[j] != 0:
            ok = False
            break

    if ok:
        ans += 1

print(ans)


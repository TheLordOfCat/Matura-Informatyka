f = open("liczby.txt", "r")
data = f.read().split()

rep = [0]*10005

for d in data:
    rep[int(d)] += 1

ans1 = 0
ans2 = 0
ans3 = 0

for i in range(0, len(rep)):
    if rep[i] > 0:
        ans1 += 1
    if rep[i] == 2:
        ans2 += 1
    if rep[i] == 3:
        ans3 += 1

print(ans1)
print(ans2)
print(ans3)
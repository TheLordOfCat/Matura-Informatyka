f = open("liczby.txt", "r")
data = f.read().split()

ans = 0
firstNum = -1
for num in data:
    s = str(num)
    if s[0] == s[-1]:
        ans += 1
        if firstNum == -1:
          firstNum = num

print(ans)
print(firstNum)
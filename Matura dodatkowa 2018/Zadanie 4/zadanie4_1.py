f1 = open("dane1.txt" , "r")
data1 = f1.read().split("\n")

f2 = open("dane2.txt", "r")
data2 = f2.read().split("\n")

ans = 0
for i in range(0, len(data1)):
    d1 = data1[i].split(" ")
    d2 = data2[i].split(" ")
    if d1[-1] == d2[-1]:
       ans += 1

print(ans)
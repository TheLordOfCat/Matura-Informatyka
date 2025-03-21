f1 = open("dane1.txt" , "r")
data1 = f1.read().split("\n")

f2 = open("dane2.txt", "r")
data2 = f2.read().split("\n")

ans = 0
for i in range(0, len(data1)):
    d1 = data1[i].split(" ")
    d2 = data2[i].split(" ")

    even1 = 0
    odd1 = 0
    for num in d1:
        if int(num)%2 == 0:
            even1 += 1
        else:
            odd1 += 1

    even2 = 0
    odd2 = 0
    for num in d2:
        if int(num) % 2 == 0:
            even2 += 1
        else:
            odd2 += 1

    if even1 == 5 and even2 == 5 and odd1 == 5 and odd2 == 5:
        ans += 1


print(ans)
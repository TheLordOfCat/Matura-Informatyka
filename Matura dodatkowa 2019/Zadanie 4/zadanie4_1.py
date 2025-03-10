f = open("liczby.txt" , "r")
data = f.read().split()

ans = []
for d in data:
    num = int(d)
    if 100 <= num and num <= 5000:
        prime = True

        for n in range(2, num):
            if num % n == 0:
                prime = False
                break

        if prime:
            ans.append(num)

print(ans)

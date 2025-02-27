f = open("liczby.txt", "r")
data = f.read().split()

def gcd(a, b):
    if a != 0:
        return gcd(b%a, a)
    return b

ans = []
gAns = 0

for i in range(0, len(data)):
    d = int(data[i])
    curSub = [d]
    g = d
    ind = i+1
    while ind < len(data):
        temp = gcd(g, int(data[ind]))
        if temp > 1:
            curSub.append(data[ind])
        else:
            break
        g = temp
        ind += 1

    if len(curSub) > len(ans):
        ans = curSub
        gAns = g

print(ans)
print(len(ans))
print(gAns)
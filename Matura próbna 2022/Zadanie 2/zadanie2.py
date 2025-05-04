# c = 0
#
# def rysuj(x):
#     global c
#     N = 20
#     if 2*x <= N:
#         # print(str(x) +", " + str(2*x))
#         rysuj(2*x)
#         c += 1
#     if 2*x+1<= N:
#         # print(str(x) + ", " + str(2 * x + 1))
#         rysuj(2*x+1)
#         c += 1
#
# rysuj(1)
# print(c)

# c = 0
# N = 2047
# while N > 1:
#     if N%2 != 0:
#         N -= 1
#         N /= 2
#     else:
#         N /= 2
#     c += 1
#
# print(c)

f = open("pary.txt", "r")
data = f.read().split()

N = 100000

def check(x, y):
    global N

    l = [x]
    ind = 0

    while ind < len(l):
        cur = l[ind]
        if cur*2 <= N:
            l.append(cur*2)
        if cur*2 + 1 <= N:
            l.append(cur*2 +1)
        ind += 1
        if cur == y:
            return True

    return False

for i in range(0, len(data), 2):
    ok = check(int(data[i]), int(data[i+1]))
    if ok:
        print(data[i] + " " + data[i+1])


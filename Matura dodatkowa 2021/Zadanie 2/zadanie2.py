T = [0, 1, 4, 2, 8, 3, 6, 2, 9, 1, 5]
n = 2021

ops = 0
def modyfikuj(s, k):
    global ops
    ops += 1
    if s + k < n:
        modyfikuj(s+k, k)
    i = s+1
    while i <= n and i <= s+k:
        # T[s] = T[s] + T[i]
        i += 1

modyfikuj(1,100)
print(ops)
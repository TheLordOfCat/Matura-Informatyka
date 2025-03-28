n = 10
k = 5
T = [0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 4]
W = [0]*(n+1)

liczba_wystapien = [0]*(k+1)

# for i in range(1, n+1):
#     liczba_wystapien[T[i]] = liczba_wystapien[T[i]] + 1
#
# p = 1
# for j in range(1, k+1):
#     for i in range(1, liczba_wystapien[j]+1):
#         W[p] = j
#         p = p + 1
#
# g = 10
# r = 0
# for j in range(1, T[g]):
#     r = r + liczba_wystapien[j]
#
# print(r)

for i in range(1, n+1):
    m = 1 + (T[i] % k)
    liczba_wystapien[m] = liczba_wystapien[m] + 1
w = liczba_wystapien[1]
print(liczba_wystapien)


def pot(a,k):
    ans = 1
    for i in range(0,k):
        ans *= a
        ans %= k

    return ans

def testF(k):
    ok = True

    for i in range(2,k):
        m = pot(i,k)
        if m != i:
            ok = False
            break

    if ok:
        return 1
    else:
        return 0


def isPrime(k):
    if k == 1 or k == 2:
        return 1
    if k %2 == 0:
        return 0

    ind = 3
    while ind*ind <= k:
        if k%ind == 0:
            return 0
        ind += 2
    return 1

def czyLC(k):
    if testF(k) == 1 and isPrime(k) != 1:
        return 1
    return 0
calls = 0

def pisz(s,n,k):
     global calls
     calls += 1
     if len(s) == n:
        print(s)
     else:
        for i in range(0,k):
            pisz(s + str(i), n, k)

pisz("",2   ,3)
print(calls)
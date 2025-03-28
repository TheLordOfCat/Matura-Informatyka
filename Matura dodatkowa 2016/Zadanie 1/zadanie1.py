def F(n):
    print("F(" + str(n) + ")")
    s = 0
    if n == 1 or n == 2:
        s = n
        print(n)
    else:
        s = n*F(n-2)
        print(n)
    s = s*(n+1)
    print(n+1)
    return s

F(11)

# for i in range(1, 7):
#     print(str(i) + " ", end = " ")
#     print(F(i))


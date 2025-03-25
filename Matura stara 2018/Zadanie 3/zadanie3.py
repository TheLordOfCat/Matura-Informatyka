def f(x):
    if x <= 1:
        return 1
    else:
        print("0")
        return x + f(x//2)

print(f(12))
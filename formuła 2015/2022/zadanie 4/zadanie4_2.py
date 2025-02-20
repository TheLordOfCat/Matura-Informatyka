f = open("liczby.txt", "r")
data = f.read().split()

def getDiv(num):
    ans = 0

    temp = num
    for i in range(2, num+1):
        while temp%i == 0:
            ans += 1
            temp /= i

    return ans


def getUnicDiv(num):
    ans = 0

    temp = num
    for i in range(2, num + 1):
        if temp%i == 0:
            ans += 1
            while temp % i == 0:
                temp /= i

    return ans

num1 = 0
val1 = 0
num2 = 0
val2 = 0

for d in data:
    num = int(d)
    temp = getDiv(num)
    if(temp > val1):
        val1 = temp
        num1 = num

    temp = getUnicDiv(num)
    if(temp > val2):
        val2 = temp
        num2 = num

print(num1)
print(val1)
print(num2)
print(val2)


a = 15
b = 24

digitsA = []
digitsB = []

indA = 0
indB = 0

while a > 0:
    indA += 1
    digitsA.append(a % 10)
    a //= 10

while b > 0:
    indB += 1
    digitsB.append(b % 10)
    b //= 10

sumA = 0
sumB = 0

for i in range(0, indA):
    sumA += digitsA[i]

for i in range(0, indB):
    sumB += digitsB[i]

if sumA == sumB:
    if digitsA[indA-1] == digitsB[0] or digitsA[0] == digitsB[indB-1]:
        print("PRAWDA")
    else:
        print("FAŁSZ")
else:
    print("FAŁSZ")
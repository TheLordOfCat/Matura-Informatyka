f = open("napisy.txt" , "r")
data = f.read().split()

countDigits = 0

for d in data:
    for l in d:
         digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
         for i in range(0, len(digits)):
             if l == digits[i]:
                 countDigits += 1
                 break

print(countDigits)
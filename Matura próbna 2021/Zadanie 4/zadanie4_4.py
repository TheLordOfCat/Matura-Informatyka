f = open("napisy.txt" , "r")
data = f.read().split()

text = ""

for d in data:
    dig = ""
    for l in d:
         digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
         for i in range(0, len(digits)):
             if l == digits[i]:
                 dig = dig + l

    for i in range(0, len(dig), 2):
        if i + 1 < len(dig):
            s = dig[i] + dig[i+1]
            num = int(s)
            if num >= 65 and num <= 90:
                text = text + chr(num)

            if len(text) >= 3:
                if text[-1] == "X" and text[-2] == "X" and text[-3] == "X":
                    print(text)
                    break


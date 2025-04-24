f = open("instrukcje.txt", "r")
data = f.read().split()

s = ""
for i in range(0, len(data), 2):
    ops = data[i]
    l = data[i+1]

    if ops == "DOPISZ":
        s += l
    elif ops == "ZMIEN":
        temp = ""
        for j in range(0, len(s)-1):
            temp += s[j]

        temp += l
        s = temp

    elif ops == "USUN":
        temp = ""
        for j in range(0, len(s) - 1):
            temp += s[j]

        s = temp

    elif ops == "PRZESUN":
        temp = ""
        found = False
        for j in range(0, len(s)):
            if s[j] == l and found == False:
                temp += chr(ord("A") + (ord(s[j])-ord("A")+1)%26)
                found = True
            else:
                temp += s[j]

        s = temp

print(s)

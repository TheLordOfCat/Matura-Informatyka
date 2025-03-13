f = open("napisy.txt" , "r")
data = f.read().split()

text = ""

for d in data:
    rev = ""
    for i in range(len(d)-1, -1, -1):
        rev = rev + d[i]

    pal1 = True
    for i in range(1, len(d)-1):
        if d[i] != rev[i-1]:
            pal1 = False

    pal2 = True
    for i in range(1, len(d)-1):
        if rev[i] != d[i-1]:
            pal2 = False

    if pal1:
        t = d[int(len(d)/2)]
        text = text + t
    elif pal2:
        t = d[int(len(d) / 2)-1]
        text = text + t

print(text)

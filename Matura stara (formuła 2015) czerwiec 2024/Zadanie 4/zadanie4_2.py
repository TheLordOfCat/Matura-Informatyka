f = open("slowa.txt" , "r")
data = f.read().split()

for d in data:
    for i in range(0, len(d)-4):
        if d[i] == "e" and d[i+4] == "e":
            s = d[i]+d[i+1]+d[i+2]+d[i+3]+d[i+4]
            print(s)
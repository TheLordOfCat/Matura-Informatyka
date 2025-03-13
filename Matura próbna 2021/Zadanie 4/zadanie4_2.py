f = open("napisy.txt" , "r")
data = f.read().split()

text = ""

for i in range(19, len(data), 20):
    text = text + data[i][int((i+1)/20)-1]

print(text)
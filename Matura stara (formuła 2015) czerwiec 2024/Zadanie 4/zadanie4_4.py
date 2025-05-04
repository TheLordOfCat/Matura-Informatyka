f = open("slowa.txt" , "r")
data = f.read().split()

for d in data:
    countLetters = [0]*26
    for l in d:
        countLetters[ord(l)-ord("a")] += 1

    for i in range(0, len(countLetters)):
        if countLetters[i] >= len(d)/2:
            print(d)
            break


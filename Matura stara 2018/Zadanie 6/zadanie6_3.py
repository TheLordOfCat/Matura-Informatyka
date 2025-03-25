f = open("slowa.txt", "r")
data = f.read().split("\n")

c = 0
for d in data:
    sList = d.split(" ")
    s1 = sList[0]
    s2 = sList[1]

    countLetters1 = [0]*27
    countLetters2 = [0] * 27

    for s in s1:
        countLetters1[ord(s) - ord("A")] += 1
    for s in s2:
        countLetters2[ord(s) - ord("A")] += 1

    ok = True
    for j in range(0, len(countLetters1)):
        if countLetters1[j] != countLetters2[j]:
            ok = False
            break
    if ok:
        c += 1


print(c)
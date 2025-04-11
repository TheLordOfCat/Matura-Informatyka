f1 = open("tj.txt", "r")
words = f1.read().split()

f2 = open("klucze1.txt", "r")
keys = f2.read().split()

ans = []
for i in range(0, len(words)):
    d = words[i]
    k = keys[i]

    w = ""
    for j in range(0, len(d)):
        a = ord(d[j]) + ord(k[j%len(k)]) - ord("A")+1
        if a > 90:
            a -= 26
        w = w + chr(a)

    ans.append(w)

print(ans)
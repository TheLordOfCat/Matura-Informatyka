f = open("dane_anagramy.txt", "r")
data = f.read().split()

ans = []
for i in range(0, len(data)):
    seq = []
    digits1 = [0,0,0,0,0, 0,0,0,0,0]
    for d in data[i]:
        digits1[int(d)] += 1

    seq.append(data[i])
    for j in range(i+1, len(data)):
        digits2 = [0,0,0,0,0, 0,0,0,0,0]
        for d in data[j]:
            digits2[int(d)] += 1

        ok = True
        for o in range(0, len(digits1)):
            if digits1[o] != digits2[o]:
                ok = False
                break

        if ok:
            seq.append(data[j])

    if len(ans) < len(seq):
        ans = seq

print(len(ans))


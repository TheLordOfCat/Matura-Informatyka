seq = [5, -3, 4, -2, 3, -1, 2]

ans = 0
ansSeq = []

for i in range(0, len(seq)):
    cur = 0
    curSeq = []

    for j in range(i, len(seq)):
        cur += seq[j]
        curSeq.append(seq[j])

        if ans < cur:
            ans = cur
            ansSeq = curSeq.copy()

    if ans < cur:
        ans = cur
        ansSeq = curSeq.copy()

print(ans)
print(ansSeq)

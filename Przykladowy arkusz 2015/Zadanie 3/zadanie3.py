from turtledemo.sorting_animate import start_isort

stairs = [2, 2, 2, 3, 1, 1, 3, 3, 1, 10, 11, 7, 7, 6, 7, 7, 8, 9, 9, 7]

seq = []
steps = []

curSeq = [stairs[0]]
curSteps = 0

for i in range(1, len(stairs)):
    if stairs[i] < curSeq[len(curSeq)-1]:
        curSeq.append(stairs[i])
        curSteps += 1
    elif stairs[i] == curSeq[len(curSeq)-1]:
        curSeq.append(stairs[i])
    else:
        seq.append(curSeq)
        steps.append(curSteps)

        curSeq = [stairs[i]]
        curSteps = 0

seq.append(curSeq)
steps.append(curSteps)

for i in range(0, len(seq)):
    print(seq[i], end = " ")
    print(steps[i])


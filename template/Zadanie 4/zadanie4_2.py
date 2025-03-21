f = open("pary.txt" , "r")
data = f.read().split()

ans = []
ansCount = []

for i in range(0, len(data), 2):
    s = data[i+1]

    bestL = ""
    curL = ""
    for j in range(0, len(s)):
        if len(curL) == 0:
            curL = curL + s[j]
        else:
            if curL[0] == s[j]:
                curL = curL + s[j]
            else:
                if len(bestL) < len(curL):
                    bestL = curL
                curL = ""
                curL = curL + s[j]

    if len(bestL) < len(curL):
        bestL = curL
        curL = ""

    ans.append(bestL)
    ansCount.append(len(bestL))

for i in range(0, len(ans)):
    print(ans[i], end = " ")
    print(ansCount[i])

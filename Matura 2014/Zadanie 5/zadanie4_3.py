f = open("NAPIS.TXT", "r")
data = f.read().split()

ans = []
for o in range(0, len(data)):
    reco = False

    for i in range(o+1, len(data)):
        if data[o] == data[i]:
            reco = True
            break

    if reco:
        found = False
        for i in range(0, len(ans)):
            if ans[i] == data[o]:
                found = True

        if found == False:
            ans.append(data[o])

print(ans)

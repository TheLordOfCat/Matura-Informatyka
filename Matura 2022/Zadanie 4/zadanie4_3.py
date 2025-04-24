f = open("liczby.txt", "r")
data = f.read().split()

ans3 = 0
ans5 = 0

for i in range(0, len(data)):
    for j in range(0, len(data)):
        if int(data[j])%int(data[i]) == 0 and i != j:
            for o in range(0, len(data)):
                if int(data[o])%int(data[j]) == 0 and j != o:
                    ans3 += 1

for i in range(0, len(data)):
    for j in range(0, len(data)):
        if int(data[j])%int(data[i]) == 0 and i != j:
            for o in range(0, len(data)):
                if int(data[o])%int(data[j]) == 0 and j != o:
                    for l in range(0, len(data)):
                        if int(data[l])%int(data[o]) == 0 and o != l:
                            for k in range(0, len(data)):
                                if int(data[k])%int(data[l]) == 0 and l != k:
                                    ans5 += 1

print(ans3)
print(ans5)
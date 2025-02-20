f = open("liczby.txt", "r")
data = f.read().split()

# ans = []
#
# for i in range(0, len(data)):
#     for j in range(0, len(data)):
#         for o in range(0, len(data)):
#             if not i == j and not j == o and not i == o:
#                 x = int(data[i])
#                 y = int(data[j])
#                 z = int(data[o])
#                 if(z%y == 0 and y%x == 0):
#                     temp = [x, y, z]
#                     ans.append(temp)
#
# for l in ans:
#     print(str(l[0]) + " " + str(l[1]) + " " + str(l[2]))

ans = 0

for a in range(0, len(data)):
    for b in range(0, len(data)):
        if not a == b and int(data[b])%int(data[a]) == 0:
            for c in range(0, len(data)):
                if not c == b and int(data[c])%int(data[b]) == 0:
                    for d in range(0, len(data)):
                        if not c == d and int(data[d])%int(data[c]) == 0:
                            for e in range(0, len(data)):
                                if not e == d and int(data[e])%int(data[d]) == 0:
                                    ans += 1;


print(ans)


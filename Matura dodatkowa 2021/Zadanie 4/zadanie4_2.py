f = open("galerie.txt" , "r")
data = f.read().split("\n")

for d in data:
    sen = d.split(" ")

    countBuisness = 0
    countArea = 0

    for i in range(2, len(sen), 2):
        if int(sen[i]) != 0:
            countBuisness += 1
            countArea += int(sen[i])*int(sen[i+1])

    print(sen[1] + " " + str(countArea) + " " + str(countBuisness))
f = open("kody.txt" , "r")
data = f.read().split("\n")

kod = [10101110111010, 11101010101110,10111010101110,11101110101010,10101110101110,11101011101010,10111011101010,10101011101110,11101010111010,10111010111010]

for d in data:
    num = d
    parz = 0
    for i in range(0, len(d), 2):
        parz += int(d[i])

    niep = 0
    for i in range(1, len(d), 2):
        niep += int(d[i])

    liczba = parz*3+niep

    liczba = liczba%10
    liczba = 10-liczba
    liczba = liczba % 10
    print(str(liczba) + " " + str(kod[liczba]))

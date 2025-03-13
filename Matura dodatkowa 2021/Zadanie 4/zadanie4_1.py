f = open("galerie.txt" , "r")
data = f.read().split("\n")

countries = ['GB', 'D', 'E', 'I', 'F', 'RO', 'A', 'H', 'BG', 'CZ', 'B', 'S', 'HR', 'NL', 'LV', 'GR', 'LT', 'FIN', 'DK', 'IRL', '']
countCities = [0]*len(countries)

for d in data:
    sen = d.split(" ")

    for i in range(0, len(countries)):
        if countries[i] == sen[0]:
            countCities[i] += 1

for i in range(0, len(countries)):
    print(countries[i] + " " + str(countCities[i]))

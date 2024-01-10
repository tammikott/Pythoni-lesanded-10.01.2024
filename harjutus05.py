#Ott Tammik
#28.11.2023




'''
Nimede lisamine loendisse
Küsi kasutajalt viis nime. Salvesta need loendisse ja kuva tähestikulises järjekorras. Kuva eraldi viimati lisatud nimi.
'''

nimed = []


for i in range(5):
    nimi = input("lisa nimi pls: ")
    nimed.append(nimi)


print(nimed)
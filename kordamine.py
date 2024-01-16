#Kordamine
#Ott Tammik 16.01.2024


vanused = [12, 2, 1, 29, 34, 20, 18, 46, 13, 8, 24, 40, 5, 12, 11, 8,]

def vanus():
    
    print("suurim vanus on", max(vanused))
    print("väikseim vanus on", min(vanused))
    kogusumma = sum(vanused)
    print("kogusumma on", (kogusumma))
    print("kesmine on", kogusumma/len(vanused))



vanus()


positiivne = [12, 5, 17, 6, 10, 14, 9, 7, 15, 23, 29, 11, 16, 18, 9, 25, 14, 8, ]
negatiivne = [-1, -7, -11, -9, -14, -21, -31, -3, -18, -21, -24,]

def loendid():
    
    arvud = int(input("Kirjuta 5 positiivset või negatiivset arvu: "))
    if arvud == "-":
        print(negatiivne)
    elif arvud == "0"
    else:
        print(positiivne)
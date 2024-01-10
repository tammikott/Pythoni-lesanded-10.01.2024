

'''
Jukebox
Ada tahab valida plaadiautomaadist laulu ja uurib, milliseid laule masin mängib. Muusikapalad on kirjas failis, kus iga laul on eraldi real.
Programmi testimiseks kasutatakse järgmisi faile, mida võite salvestada või koostada ise mõne tekstiredaktoriga (nt Notepad):
'''

failinimi = input("Palun sisesta failinimi: ")
fail = open(failinimi, encoding="utf-8")
nr= 1
for rida in fail:
    print(f"{nr}. {rida}", end="")
    nr+=1
    
    
fail.seek(0)
nr=1
jrk = int(input("Valige laulu järjekorranumber: "))
for rida in fail:
    if nr==jrk:
        print(f"Mängitav muusika pala on: {rida}",end="")
    nr+=1

#Iseseisev töö 3
#Ott Tammik 10.01.2024


import datetime

'''
Tahvli juurde
Mõned õpetajad on tavatsenud õpilasi tahvli juurde vastama kutsuda kuupäeva järgi vastavalt õpilaste nimekirjale. Näiteks 4. kuupäeval tuleb esimesena vastama nimekirjas 4. olev õpilane.
Failis nimekiri.txt on õpilaste nimed, igaüks eraldi real. Üks selline, mis on genereeritud leheküljel Random Name Generator. Võite ise koostada ka teistsuguse nimekirja.
Koostada programm, mis
küsib failinime (eeldame, et kasutaja sisestatud nimega fail leidub ja seal on vähemalt 31 nime);
loeb sisestatud nimega failist andmed;
väljastab vastavalt tänasele kuupäevale õpilase nime, kes peab vastama tulema.
Programm peab tänase kuupäeva leidma automaatselt, aluseks saab võtta järgmise näite:
from datetime import * 
print(datetime.now().day) 
'''
'''
fail = open("nimekiri.txt", encoding="utf-8")

p = datetime,datetime.now().day
nr = 1
for rida in fail:
    if nr==p:
        print(f"Tahvli ette tuleb: {rida}.")
    nr+=1
'''
#Bänner
    
lause = "Osta ja sa ei kahtse!"







print(lause.upper)








































'''
Jukebox
Ada tahab valida plaadiautomaadist laulu ja uurib, milliseid laule masin mängib. Muusikapalad on kirjas failis, kus iga laul on eraldi real.
Programmi testimiseks kasutatakse järgmisi faile, mida võite salvestada või koostada ise mõne tekstiredaktoriga (nt Notepad):
'''
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
'''


















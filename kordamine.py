#Kordamine
#Ott Tammik 16.01.2024

import random

#14. Palkade vordlus - Loo palk.txt fail tootajate nime, soo ja palganumbriga (10 tootajat).
#Koosta programm, mis analuusib kas firmas toimub diskrimineerimist soo jargi.
#Selleks vordle omavahel meeste ja naiste palkade keskmiseid,
#samuti meeste ja naiste kĆµige kĆµrgemat palka. Programm peab tegema otsuse.
#
#	Hubert Hunt m 2340
#	Siim Siil m 2570
#	MĆ¤rt MĆ¤ger m 1960
#	Vilma Vihmauss n 2060
#	Merike Metskits n 2250
#	Kati Karu n 2370
#	Elmar Elevant m 2900
#	Timoteus Tigu m 2850
#	Reet Rebane n 2340
#	Kalev Kaamel m 2570
#	Karmen Kass n 2120
#	Kornelius Koer m 2250

def palgavordlus():
    
    with open("palgad.txt", "r", encoding="utf-8") as f:
        loe = f.readlines()

    meeste_palk = []
    naiste_palk = []


    for line in loe:
        n, s, p = line.split(" ")

        if s == "n":
            naiste_palk.append(int(p))
        else:
            meeste_palk.append(int(p))            

    keskmine_mehed = sum(meeste_palk)/len(meeste_palk)
    keskmine_naised = sum(naiste_palk)(naiste_palk)
    suurim_mehed = max(meeste_palk)
    suurim_naised = max(naiste_palk)

    if keskmine_mehed > keskmine_naised:
        print("Mehed saavad rohkem palka")
    elif keskmine_naised > keskmine_mehed:
        print("Naised saavad rohkem palka")
    else:
        print("Palgad ei ole ebaõiglased")


palgavordlus()



#Eurokalkulaator
#	Koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK vĆµi EEK->EUR.
#	Oluline on kasutada kahte funktsiooni!!



def eur_eek(summa):
    return summa * 15.6466

def eek_eur(summa):
    return summa * 0.0639

def pohifunktsioon():
    print("Tahad teisendada EUR -> EEK või EEK -> EUR?")
    kasutaja_valik = input("Sisesta 'eur2eek' või 'eek2eur': ")

    if kasutaja_valik.lower() == "eur2eek":
        summa = float(input("Sisesta summa eurodes: "))
        teisendatud_summa = eur_eek(summa)
        print(f"{summa} EUR on {teisendatud_summa} EEK.")



    elif kasutaja_valik.lower() == "eek2eur":
        summa = float(input("Sisesta summa Eesti kroonides: "))
        teisendatud_summa = eek_eur(summa)
        print(f"{summa} EEK on {teisendatud_summa} EUR.")




    else:
        print("Aru ei saanud või?")

pohifunktsioon()




#Võtke nimekiri ja kirjutage programm, mis prindib välja kõik loendi elemendid, mis on väiksemad kui 5. 1p
#Selle asemel, et printida elemente ükshaaval, tehke uus loend, milles on kõik selle loendi elemendid alla 5, ja printige see uus loend välja. 1p
#Kirjutage see ühele Pythoni reale. 1p
#Küsige kasutajalt numbrit ja tagastage loend, mis sisaldab ainult algse loendi elemente, mis on väiksemad kui kasutaja antud arv. 1p



a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def list():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [i for i in a if i < 5]
    print(b)
    kasutaja_kusimus = int(input("vali number: \n"))

list()



#Kaugushupe
#	kasutaja sisestab 3 kaugushĆ¼ppe tulemust - 1p
#	sinu programm leiab ning vĆ¤ljastab parima ja keskmise tulemuse - 2p
#	programmi dialoog kasutajaga on arusaadav ja Ć¼heselt mĆµistetav - 1p
#	kood kommenteeritud - 1p


def kaugushupe():
    tulemused = []
    for i in range (3):
        tulemus = float(input("Sisesta oma kaugushupe tulemused: "))
        tulemused.append(tulemus)

    print("Sinu parim tulemus oli", max(tulemused))
    kogusumma = sum(tulemused)
    print("Keskmine tulemus", kogusumma/len(tulemused))


kaugushupe()


#Taringud
#	kuvatakse korrektne arusaadav kĆ¼simus ja hiljem vastus - 1p
#	kasutaja vĆµistleb kahe tĆ¤ringuga arvuti vastu - 1p
#	kasutaja teeb pakkumise ning suurima tĆ¤ringupunktisumma vĆµitja saab laual oleva raha endale - 2p
#	kood kommenteeritud - 1p

def taringud():
    k_konto = 0
    a_konto = 0

    kasutaja = random.randint(1, 20) + random.randint(1, 20)
    arvuti = random.randint(1, 20) + random.randint(1, 20)

    raha = int(input("kui palju raha sisse paned? "))
    print(raha, "Sisse pandud raha")
    if kasutaja > arvuti:
        print("Sa võitsid!")
        k_konto = raha * 2
        print("Kasutaja kontol on nüüd", k_konto + raha * 2)
    elif arvuti > kasutaja:
        print("Sa kaotasid! Arvuti võtab su raha.")
        a_konto = raha * 2
        print("Arvuti kontol on nüüd", a_konto + raha * 2)
    else:
        print("Viik! Saad raha tagasi")




taringud()




# Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris vĆµi paaritu
#	kuvatakse korrektne arusaadav kĆ¼simus ja vastus - 1p
#	eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 1p
#	kood mis teavitab paaris vĆµi paaritust arvust - 1p
#	kuvatakse programmi pealkiri - 1p
#	kood kommenteeritud - 1p

def paarispaaritu():
    sisestamine = input("Sisesta arv: ")
    arv = int(sisestamine)
    if arv % 2 == 0:
        print(f"{arv} on paaris")
    else:
        print(f"{arv} on paaritu")




paarispaaritu()



















#  Vanused
# 	loo vanuste loend 1p
# 	leia numbrite suurim ja vĆ¤ikseim arv  1p
# 	kogusumma  1p
# 	keskmine 1p



vanused = [12, 2, 1, 29, 34, 20, 18, 46, 13, 8, 24, 40, 5, 12, 11, 8]

def vanus(vanused):
    
    print("suurim vanus on", max(vanused))
    print("väikseim vanus on", min(vanused))
    summa = sum(vanused)
    print("kogusumma on", (summa))
    print("keskmine on", summa/len(vanused))

vanus(vanused)

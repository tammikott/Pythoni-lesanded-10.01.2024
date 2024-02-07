#Kordamine
#Ott Tammik 16.01.2024

import random


#14. Palkade vĆµrdlus - Loo palk.txt fail tĆ¶Ć¶tajate nime, soo ja palganumbriga (10 tĆ¶Ć¶tajat).
#	Koosta programm, mis analĆ¼Ć¼sib kas firmas toimub diskrimineerimist soo jĆ¤rgi. Selleks vĆµrdle omavahel meeste ja naiste palkade keskmiseid, samuti meeste ja naiste kĆµige kĆµrgemat palka. Programm peab tegema otsuse.
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

    fail = open("palgad.txt", encoding="UTF-8")
    for rida in fail:
        print("Lugesin sellise rea: " + rida)
    fail.close()



palgavordlus()


#Eurokalkulaator
#	Koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK vĆµi EEK->EUR.
#	Oluline on kasutada kahte funktsiooni!!










#KaugushĆ¼pe
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


#TĆ¤ringud
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
        print("Kasutaja kontol on nüüd", k_konto)
    elif arvuti > kasutaja:
        print("Sa kaotasid! Arvuti võtab su raha.")
        a_konto = raha
        print("Arvuti kontol on nüüd", a_konto)
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














#  List Less Than Ten
# 	Take a list and write a program that prints out all the elements of the list that are less than 5. 1p
# 		a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list. 1p
# 	Write this in one line of Python. 1p
# 	Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user




a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

















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



# positiivne = [12, 5, 17, 6, 10, 14, 9, 7, 15, 23, 29, 11, 16, 18, 9, 25, 14, 8, ]
# negatiivne = [-1, -7, -11, -9, -14, -21, -31, -3, -18, -21, -24,]
# def loendid():
    
#for i in range (5):
#    arvud = int(input("Kirjuta 5 positiivset või negatiivset arvu: "))
#if 

# loendid()


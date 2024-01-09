from os.path import realpath, join, dirname

vysledek=0
k=0

with open(join(dirname(realpath(__file__)), "4aoc.txt"), "r") as file: #otevirani souboru
    for radek in file: #do radek to ukladam ty radky pismenko po pismenku
        karta,cisla =radek.split (":")
        hozeno,dano=cisla.split("|")
        #print(dano)
        #print(hozeno)
        hozene_rozdelene=hozeno.strip().split(" ")
        dane_rozdelene=dano.strip().split(" ")
        #print (hozene_rozdelene)
        #print(dane_rozdelene)
        for h in hozene_rozdelene:
            if h.isdigit():
                for d in dane_rozdelene:
                    if d.isdigit():
                        if d==h:
                            if k == 0:
                                k=1
                            else:
                                k*=2
        vysledek+=k
        k=0
print(vysledek)
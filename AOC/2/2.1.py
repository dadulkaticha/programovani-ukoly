from os.path import realpath, join, dirname

cervena = 12
zelena = 13
modra =  14
vysledek2 = 0
i = 0

dict_barvy = {
    "blue" : 0,
    "green" : 0,
    "red" : 0,
}

with open(join(dirname(realpath(__file__)), "2aoc.txt"), "r") as file: #otevirani souboru
    for radek in file: #do radek to ukladam ty radky pismenko po pismenku
        hra,skupina =radek.split (":")
        kolo = skupina.split(";")
        #print (len(kolo)) #len je velikost kolik je prvku v listu, kolo urcuje v jakem listu
        for group in kolo:
            vstup = group.split(",") # rozdeluje group po carkach
            for v in vstup:
                #print (v)
                pocet,barvy = v.strip().split(" ") # cislo se ulozi do pocet a barva do barvy, rozdeluje dle mezery
                dict_barvy[barvy] = int(pocet)
            if dict_barvy["blue"]<=modra and dict_barvy["green"]<=zelena and dict_barvy["red"]<=cervena:
                #print(hra)
                i += 1 # pricita k i 1 pokud plati if
        if len(kolo) == i: # pokud je pocet kol stejny jako i
            vysledek1 = hra.strip().split(" ") # rozdeluje game a jeji cislo
            print(vysledek1)
            vysledek2 += int(vysledek1[1])
        i=0 # resetuje i na 0
    print(vysledek2)       
from os.path import realpath, join, dirname
import re

m=0
vysledek=0
cisilka=[]
znacky=[]

with open(join(dirname(realpath(__file__)), "3aoc.txt"), "r") as file: #otevirani souboru
    for y,radek in enumerate(file): # enumerate rozdeluje na index (v y) a text (v radku)
        cisla = [(y,m.start(), m.end(), m.group()) for m in re.finditer(r"\d+", radek)] # vypisuji take dany index radku proto y 
        znaky = [(y,m.start(), m.end(), m.group()) for m in re.finditer(r"[^.\d\n]", radek)] #hleda vse krom tecky a cisel # group vypisuje jaky znak to je
        #print (cisla)
        #print (znaky)
        for x, y, z, c in cisla:
            cisilka.append((x, y, z, c))
        for r,s, t, z in znaky:
            znacky.append((r, s, t, z))

    for z in znacky:
        #print(z)
        for c in cisilka:
            #print(c)
            if abs(c[0]-z[0]) <= 1: # pokud je abs. hodnota cisel na prvnim indexu c, z jedna nebo mensi nez jedna tak plati podminka
                if c[1]-1==z[1] or c[1]==z[1] or c[1]+1==z[1] or c[1]+(c[2]-c[1])-1==z[1] or c[1]+(c[2]-c[1])==z[1]:
                    vysledek += int(c[3])
                    #print(f"{c[3]} : {c[1]} : {z[1]} : {c[2]}")
print(vysledek)
from os.path import realpath, join, dirname
import re

m=0
k=0
vysledek=0
cisilka=[]
znacky=[]
dotykaji=[]

with open(join(dirname(realpath(__file__)), "3aoc.txt"), "r") as file: #otevirani souboru
     for y,radek in enumerate(file): #enumerate rozdeluje na index (v y) a text (v radku)
        cisla = [(y,m.start(), m.end(), m.group()) for m in re.finditer(r"\d+", radek)] #vypisuji take dany index radku proto y 
        znaky = [(y,m.start(), m.end(), m.group()) for m in re.finditer(r"[*]", radek)] #hleda hvezdy #group vypisuje jaky znak to je
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
            if abs(c[0]-z[0]) <= 1: #pokud je abs. hodnota cisel na prvnim indexu c, z jedna nebo mensi nez jedna tak plati podminka
                if c[1]-1==z[1] or c[1]==z[1] or c[1]+1==z[1] or c[1]+(c[2]-c[1])-1==z[1] or c[1]+(c[2]-c[1])==z[1]:
                    dotykaji.append ((z, c))
index_0_items = [item[0] for item in dotykaji]
print (index_0_items)
print(dotykaji)
while k < len(dotykaji):
    if index_0_items.count(dotykaji[k][0])==2: #k posouvam, bere to zavorky podle toho kolik je k
        other_index = next(j for j, x in enumerate(dotykaji) if x[0]==dotykaji[k][0] and j != k) #j for j, x- vraci JEN j, j,x in enumerate - j je index prvku a x je item
        vysledek += int(dotykaji[k][1][3])*int(dotykaji[other_index][1][3])
        dotykaji=[x for j, x in enumerate(dotykaji) if j not in [k, other_index]] #list dvou itemu, musi platit oboje - k, other_index
        index_0_items=[item[0] for item in dotykaji]
    else:
        k+=1
print(vysledek)
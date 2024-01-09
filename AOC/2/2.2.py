from os.path import realpath, join, dirname

dict_pocet = {
 "blue" : 0,
 "red" : 0,
 "green" : 0,
}

cisilko=[]
x=0

with open(join(dirname(realpath(__file__)), "2aoc.txt"), "r") as file: #otevirani souboru
    for radek in file: #do radek to ukladam ty radky pismenko po pismenku
        hra,kola =radek.split (":") #rozdeli "Game" a jeji cislo od jednotlivych hodu kostkou
        hody = kola.split(";") #rozdeli jednotliva kola ve hre
        #print(hody)
        for skupiny in hody:
            vstup = skupiny.split(",") #rozdeli jednotliva kola na hody
            #print (vstup)
            for v in vstup:
                cislo,barva = v.strip().split(" ") #cislo ulozim do cislo a barva do barva
                #print(cislo)
                if dict_pocet[barva]<int(cislo):
                    dict_pocet[barva] = int(cislo)
        #print(dict_pocet)
        soucin = dict_pocet["blue"]*dict_pocet["red"]*dict_pocet["green"]
        cisilko.append(soucin)
        #print(cisilko)
        #print(soucin)
        #print (dict_pocet["red"])
        dict_pocet["red"], dict_pocet["blue"], dict_pocet["green"]=0,0,0
        #print(dict_pocet)
for i in cisilko:
    x=x+i
print(x)
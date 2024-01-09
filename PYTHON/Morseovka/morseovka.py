from os.path import realpath, join, dirname

seznam_znaku = [] 
seznam_kod = []
with open(join(dirname(realpath(__file__)), "mors.txt"), "r") as file: # otevirani souboru
    for morse in file: # do morse to ukladam ty radky pismenko po pismenku
        pismenko = morse[0]
        kod = morse[1:].strip() #strip me zbavi mezer na konci
        print (morse)
        seznam_znaku.append(pismenko) # uklada pismena na seznam znaku
        seznam_kod.append(kod)
    print (seznam_znaku)
veta=input("Zadejte libovolnou vetu. (velkymi pismeny) ")

tokens = list(veta)

preklad = ""

for p in tokens: # p je jedno pismenko
    index = seznam_znaku.index(p)
    seznam_kod[index]
    preklad += seznam_kod[index] + print(" ")
print (preklad)

from os.path import realpath, join, dirname

seznam_znaku = []
seznam_kod = []

#otevirani souboru
with open(join(dirname(realpath(__file__)), "mors.txt"), "r") as file:
    #do morse ukladam radky z textaku pismenko po pismenku
    for morse in file:
        pismenko = morse [0]
        #strip me zbavi mezer na konci
        kod = morse[1:].strip()

        #uklada pismenka na seznam znaku
        seznam_znaku.append(pismenko)
        seznam_kod.append(kod)

veta = input("Zadejte libovolnou vetu: ").upper()

tokens = list(veta)
preklad = " "

#p je jedno pismenko
for p in tokens:
    index = seznam_znaku.index(p)
    seznam_kod[index]

    preklad += seznam_kod[index] + " "
print (veta + ":" + preklad)
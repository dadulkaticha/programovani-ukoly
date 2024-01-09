from itertools import pairwise
from os.path import join, realpath, dirname

#vytrvorena fuknce pro nalezeni dalsiho 
def dalsi_cteni(ctena_cast):
    #pokud jsou vsechny hodnoty v sade cteni stejne, vrati to tu hodnotu
    if len(set(ctena_cast)) == 1:
        return ctena_cast[0]
    #pokud tomu tak neni, vola funkci next_reading s rozdily mezi po sobe jdoucimi cisly
    return ctena_cast[-1] + dalsi_cteni([x[1] - x[0] for x in pairwise(ctena_cast)])

#otevre a precte soubor kde je input
with open(join(dirname(realpath(__file__)), "9aoc.txt"), "r", encoding="utf_8") as input:
    #prochazi radky a prevadi je na seznam int (celych cisel)
    cteni = [[int(val) for val in line.split(" ")] for line in input.readlines()]
    #listy pro ulozeni vysledku pro obe casti
    vysledek1 = []
    vysledek2 = []
    #for ktery prochazi jednotlive casti po sobe v celkovem cteni souboru
    for ctena_cast in cteni:
        vysledek1.append(dalsi_cteni(ctena_cast))
        vysledek2.append(dalsi_cteni(ctena_cast[::-1]))
    #vypise do konzole vysledky  pro obe casti
    print(f"Cast 1 : {sum(vysledek1)}")
    print(f"Cast 2 : {sum(vysledek2)}")
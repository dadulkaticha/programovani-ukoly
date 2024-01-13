"""
Ze začátku nám většinou stačí pro zadávání hodnot do skriptu klasický input, 
ale pokročilejší skripty by měly příjímat co nejvíce argumentů z příkazové řádky.
To umožní tyto skripty volat pomoci jiných skriptů, ať už skriptů python, nebo například bash.
"""

#existují dvě metody zastaralá metoda využíva modulu sys rovnou zde vysvětlím modernější s využitím modulu argparse
import argparse

#Vytvoříme instanci nášeho parseru pomocí metody ArgumentParser(), který se stará o zpracování argumentů předaných přes příkazovou řádku
#, můžeme přidat také globální popis, jako například způsob jak mají být argumenty formátovány
parser = argparse.ArgumentParser(description='Program demonstrující předávání argumentů přes vlajky')

#přidáme argumenty pomocí metody add_argument() první definuje vlajku za jakou argument; metavar je celé jméno předávané v nápovědě; typ určuje typ argumentu;
#default určuje hodnotu, která je nastavená v případě že není žádná předána; help je dloubhý popis pro nápovědu
parser.add_argument('-z', metavar='--zprava', type=str, default="nic nebylo předáno", help='Zde zadejte zprávu která má být předána programu')
parser.add_argument('-n',metavar="--nasobnost",type=int, default=1, help="Kolikrát vytisknout řetězec")
parser.add_argument('-f',metavar="--faktorial",type=int, default=1, help="Počítá to faktoriál")
parser.add_argument('-m',metavar="--mocnina",type=int, default=1, help="Počítá to mocninu")
parser.add_argument('-c',metavar="--cislo",type=int, default=1, help="Zadam cislo ktere mocnim")
#můžeme přidat kolik chceme argumentů

#parse_args vrací specialní datový typ který umožňuje přistupovat k jednotlivým argumentům pomocí jejich vlajky bez -
args = parser.parse_args()

#přístup k argumentu
#funkce pocitajici mocninu
def Mocnina(cislo:int, mocnina:int)->int:
    # _ muzeme pouzit misto i, pokud s nim nebudeme dale pracovat
    #uzivatel zada mocninu a cislo a cislo se vynasobi tolikrat, jaka je velikost mocniny
    for _ in range(1, mocnina):
        cislo *=cislo
    return cislo

#funkce pocitajici faktorial
def Faktorial(cislo:int)->int:
    vysledek=1
    #zadane cislo vynasobime tolikrat, jaka je velikost zadaneho cisla+1
    for i in range(1, cislo+1):
        vysledek *=i
    return vysledek
print(args.z*args.n)
print(Faktorial(args.f))
print(Mocnina(args.c, args.m))

#tento příkaz spusťte prvně pomocí příkazu: 	python predavaniArgumentu.py 						(vrátí defaultní hodnotu)
#po té ho spusťte pomocí příkazu: 				python predavaniArgumentu.py -z "Vaše zpráva"		("vaše zpráva" vymněňte za libovolnou zprávu)
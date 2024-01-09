from os.path import realpath, join, dirname

with open(join(dirname(realpath(__file__)), "5aoc.txt"), "r") as file: #otevirani souboru
    x = [l for l in file.read().split("\n\n")] #cte po odstavcich
seminka = [int(i) for i in x[0][7:].split(" ")] #hodnoty seminek davame na int hodnoty a delime je dle mezery
mappings = [[[int(i) for i in line.split(" ")] for line in mapping.splitlines()[1:]] for mapping in x[1:]] 

hodnoty = seminka #inicializace proměnné 'hodnoty' s počátečními hodnotami
for mapping in mappings:
    nove_hodnoty = [] #nový seznam pro uložení aktualizovaných hodnot
    for h in hodnoty: 
        nova_hodnota = h #inicializace 'nova_hodnota' s aktuální hodnotou
        for cil, start, velikost in mapping:
            if start <= h < start + velikost: #kontrolujeme zda aktuální hodnota spadá do určeného rozsahu
                nova_hodnota = h - start + cil
                break #ukončení cyklu
        nove_hodnoty.append(nova_hodnota) #ukladame nove hodnoty do listu novych hodnot
    hodnoty = nove_hodnoty

print("Minimální lokální hodnota je:", min(hodnoty))
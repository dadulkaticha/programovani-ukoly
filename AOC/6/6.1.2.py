import re
from os.path import join, realpath, dirname
from math import prod

#cte vkladana data ze souoru 6aoc
with open(join(dirname(realpath(__file__)), "6aoc.txt"), "r", encoding="utf_8") as file:
    data = file.read().strip()

#tvorime list zavody, bere data ze vstupu pro lepsi pristup
ZAVODY = list(zip(*(map(int, re.findall(r"(\d+)", x)) for x in data.split("\n"))))

#binarni vyhledavani na zjisteni casu, ktery je treba k urazeni nutne vzdalenosti
def binary_search(time, dist, left=True):
    lo, hi = 0, time
    while lo <= hi:
        mid = lo + (hi - lo >> 1)
        if mid * (time - mid) > dist:
            if left:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if left:
                lo = mid + 1
            else:
                hi = mid - 1
    return lo if left else hi

#vytvorena funkce pro vypocet poctu vitezu kteri maji danou cas a vzdalenost
def cislo_vitez(time, dist):
    return binary_search(time, dist, False) - binary_search(time, dist) + 1

#funkce pocitajici pocet vitezu v kazdem zavode
def cast_jedna():
    return prod(cislo_vitez(t, d) for t, d in ZAVODY)

#funkce co pocita pocet vitezu pro konretni dvojici casu a vzdalenosti
def cast_dva():
    return cislo_vitez(*(int("".join(str(x) for x in race)) for race in zip(*ZAVODY)))

#vypise do konzole odpovedi pro obe casti
print(f"Part 1: {cast_jedna()}")
print(f"Part 2: {cast_dva()}")
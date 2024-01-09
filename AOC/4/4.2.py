
from os.path import join, realpath, dirname
from collections import deque

i = 0
k = 0
data = {}
q = deque()

with open(join(dirname(realpath(__file__)), "4aoc.txt"), "r", encoding="utf_8") as file:
    for radek in file:
        karta, cisla = radek.split(":")
        dano, hozeno = cisla.split("|")
        hozeno = hozeno.strip().split(" ")
        dano = dano.strip().split(" ")

        for d in dano:
            for h in hozeno:
                if h.isdigit() and h == d:
                    i += 1  #pocita vyhrane hry

        k += 1  #index hry
        data[k] = i
        q.append(k)
        i = 0
        
suma = 0
while q:
    suma += 1
    k = q.popleft()
    if k in data:
        for i in range(k + 1, k + data[k] + 1):
            q.append(i)

print("Celková suma:", suma)
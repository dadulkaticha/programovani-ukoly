import os
from pathlib import Path
from time import perf_counter
from itertools import cycle
from functools import reduce
from math import lcm
from os.path import join, realpath, dirname

timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
timer_parse_start=perf_counter()
#otevre soubor s inputem jmenem 8.aoc
with open(join(dirname(realpath(__file__)), "8aoc.txt"), "r", encoding="utf_8") as file:
    #deli zahlavi od radku inputu
    header,_,*lines = file.read().splitlines()
#prevede pismenka LR ze zahlavi na cisla L = 0 a R = 1
lrs = list(map('LR'.index,header))
#tvori dict smeru pro kazde misto??
directions = {line[:3]:(line[7:10],line[12:15]) for line in lines}
#najde misto ktere zacina A - to je startovaci pozice
ghost_starts = [loc for loc in directions if loc.endswith('A')]
timer_parse_end=timer_part1_start=perf_counter()

############################## CAST 1 ##############################

#tvori promenne pro prvni cast
p1 = 0
loc = 'AAA'
#dokola prochazi pokyny, dokud se nedostane na misto kde je ZZZ
for lr in cycle(lrs):
    loc = directions[loc][lr]
    p1+=1
    if loc == 'ZZZ':
        break
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()

############################## CAST 2 ##############################

#tvori seznam, aby se do nej ukladaly vsechny pocty
ghost_counts = []
#projde pocatecni polohu kazdeho "ducha"
for i,loc in enumerate(ghost_starts):
    count = 0
    #prochazi pokyny porad dokola, dokud se nedostane na misto, ktere zacina Z
    for lr in cycle(lrs):
        loc = directions[loc][lr]
        count+=1
        if loc.endswith('Z'):
            ghost_counts.append(count)
            break
#pocita nejmensi spolecny nasobem (lcm) vsech poctu
p2 = reduce(lcm, ghost_counts)
print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
#vypise vysledky do konzole
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
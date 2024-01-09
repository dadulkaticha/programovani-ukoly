from collections import Counter
import re
from os.path import join, realpath, dirname

#otevira a cte soubor 7aoc
with open(join(dirname(realpath(__file__)), "7aoc.txt"), "r", encoding="utf_8") as file:
    data = file.read().strip()

#vytvorena funkce ktera rozpoznava typ "poker hand" dle toho jake karty jsou dane
def hand_type(hand):
    #pocita pocet vyskytu kazde karty v kazde "hand" 
    c = Counter(hand)
    #pokud tam je zolik, bude ho to pocitat jako jakoukoli normalni kartu misto toho
    counts = [0] if (jokers := c.pop("*", 0)) == 5 else sorted(c.values())
    #ze zoliku udela normalni kartu, ktera se v "hand" vyskytuje nejcasteji
    counts[-1] += jokers

    #urci typ "hand" dle typu a poctu karet v ni počtu
    match counts:
        case *_, 5:
            return 7 #five of a kind
        case *_, 4:
            return 6 #four of a kind
        case *_, 2, 3:
            return 5 #full house
        case *_, 3:
            return 4 #three of a kind
        case *_, 2, 2:
            return 3 #two pairs
        case *_, 2:
            return 2 #one pair
    return 1

#funkce ktera resi ukol dle dat, ktera jsou zadana v 7aoc.txt
def solve(data):
    ws = [l.split() for l in data.split("\n")]
    return sum(
        rank * bid
        #seradi "hands" dle jejich typu a hodnot karet
        for rank, (*_, bid) in enumerate(
            sorted(
                (hand_type(hand), *map("*23456789TJQKA".index, hand), int(bid))
                for hand, bid in ws
            ),
            1, #radi je od hodnoty 1
        )
    )


#vypise vysledek casti jedna
print(solve(data))

#vypise vysledek casti dva
print(solve(data.replace("J", "*")))
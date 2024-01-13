import urllib.request
import re
from os.path import dirname, join, realpath

soubor = open("othello.txt", "w")
url = "http://www.gutenberg.org/files/1531/1531-0.txt"

stranka = urllib.request.urlopen(url)
obsah = stranka.read().decode("utf-8")
stranka.close()

soubor = open(join(dirname(realpath(__file__)),"othello.txt"), "w", encoding="utf-8")

zacatek = re.search(r"START OF THE PROJECT GUTENBERG EBOOK OTHELLO, THE MOOR OF VENICE", obsah).start()
konec = re.search(r"END OF THE PROJECT GUTENBERG EBOOK OTHELLO, THE MOOR OF VENICE", obsah).end()

kniha = obsah[zacatek:konec]

soubor.write(kniha)

soubor.close()
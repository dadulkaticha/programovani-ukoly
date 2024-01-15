#napsano pomoci copilota
import urllib.request
import re
from os import path

def download_book(url, zacatek, konec, file_path):
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')

    #hleda prvni pismenko za touto vetou
    start = re.search(zacatek, content).start()
    #hleda posledni pismeno pred touto vetou
    end = re.search(konec, content).end()

    obsah_knihy = content[start:end]

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(obsah_knihy)

if __name__ == "__main__":
    url_knihy = "http://www.gutenberg.org/files/1531/1531-0.txt"
    zacatek = r"START OF THE PROJECT GUTENBERG EBOOK OTHELLO, THE MOOR OF VENICE"
    konec = r"END OF THE PROJECT GUTENBERG EBOOK OTHELLO, THE MOOR OF VENICE"
    output_path = path.join(path.dirname(path.realpath(__file__)), "othello.txt")

    download_book(url_knihy, zacatek, konec, output_path)
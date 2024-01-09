from os.path import realpath, join, dirname

cisilka = []
odpoved = 0

with open(join(dirname(realpath(__file__)), "1aoc.txt"), "r") as file: # otevirani souboru
    for radek in file: # do radek to ukladam ty radky pismenko po pismenku
        for char in radek:
            if char == "1" or char=="2" or char=="3" or char=="4" or char=="5" or char=="6" or char=="7" or char=="8" or char=="9":
                 cisilka.append(char) # uklada cisla na seznam cisilek
        odpoved+= int (str (cisilka[0])+ str (cisilka[-1]))
        cisilka.clear()
    print(odpoved)

         
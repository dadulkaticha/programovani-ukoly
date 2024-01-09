from os.path import realpath, join, dirname

cisilka = []
odpoved = 0
text2 =[]

with open(join(dirname(realpath(__file__)), "1aoc.txt"), "r") as file: # otevirani souboru
    for radek in file: # do radek to ukladam ty radky pismenko po pismenku
        if "one" in radek:
            radek =radek.replace("one", "o1e")
        if "two" in radek:
            radek =radek.replace("two", "t2o")
        if "three" in radek:
            radek =radek.replace("three", "th3ee")
        if "four" in radek:
            radek =radek.replace("four", "fo4r")
        if "five" in radek:
            radek =radek.replace("five", "fi5e")
        if "six" in radek:
            radek =radek.replace("six", "s6x")
        if "seven" in radek:
            radek =radek.replace("seven", "se7en")
        if "eight" in radek:
            radek =radek.replace("eight", "ei8ht")
        if "nine" in radek:
            radek =radek.replace("nine", "ni9e")

        text2.append(radek)
    for i in range(len(text2)): #prochází list
        for char in text2[i]: #prochází znaky v jednotlivých blocích listu

            if char == "1" or char=="2" or char=="3" or char=="4" or char=="5" or char=="6" or char=="7" or char=="8" or char=="9":
                cisilka.append(char) # uklada cisla na seznam cisilek
    
        odpoved+= int (str (cisilka[0])+ str (cisilka[-1]))
        cisilka.clear()
print(odpoved)
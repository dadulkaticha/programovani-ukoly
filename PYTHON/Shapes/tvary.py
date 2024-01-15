from math import pi

class Tvar:
    def __init__(self, nazev):
        self.nazev = nazev

    def __str__(self):
        return self.nazev

    def obvod(self):
        pass
    def obsah(self):
        pass
    def objem(self):
        pass
    def vypis(self):
        print("Tvar: " + self.nazev)
        print("Obvod: " + str(self.obvod()))
        print("Obsah: " + str(self.obsah()))
        print("Objem: " + str(self.objem()))

class Ctverec(Tvar):
    def __init__(self, nazev, strana):
        super().__init__(nazev)
        self.strana = strana

    def obvod(self):
        return self.strana * 4
    def obsah(self):
        return self.strana ** 2
    def objem(self):
        pass
    
class Krychle(Ctverec):
    def __init__(self, nazev, strana):
        super().__init__(nazev, strana)

    def obvod(self):
        return self.strana * 12
    def obsah(self):
        return self.strana ** 2 * 6
    def objem(self):
        return self.strana ** 3
    
class Obdelnik(Tvar):
    def __init__(self, nazev, stranaA, stranaB):
        super().__init__(nazev)
        self.stranaA = stranaA
        self.stranaB = stranaB

    def obvod(self):
        return (self.stranaA + self.stranaB) *2
    def obsah(self):
        return self.stranaA * self.stranaB
    def objem(self):
        pass

class Kvadr (Obdelnik):
    def __init__(self, nazev, stranaA, stranaB, stranaC):
        super().__init__(nazev, stranaA, stranaB)
        self.stranaC = stranaC
    
    def obvod (self):
        return (self.stranaA + self.stranaB + self.stranaC) *4
    def obsah (self):
        return (self.stranaA * self.stranaB + self.stranaA * self.stranaC + self.stranaB * self.stranaC) *2
    def objem (self):
        return (self.stranaA * self.stranaB * self.stranaC)

class Kruh(Tvar):
    def __init__(self, nazev, polomer):
        super().__init__(nazev)
        self.polomer = polomer

    def obvod(self):
        return 2 * pi * self.polomer
    def obsah(self):
        return pi * self.polomer ** 2
    def objem(self):
        pass

class Koule (Kruh):
    def __init__ (self, nazev, polomer):
        super().__init__(nazev,polomer)
    
    def obsah(self):
        return 4 * pi * self.polomer ** 2
    def objem(self):
        return 4/3 * pi * self.polomer ** 3
    def obvod(self):
        pass

class Valec (Kruh):
    def __init__ (self, nazev, polomer, vyska):
        super().__init__(nazev,polomer)
        self.vyska = vyska
    
    def obvod(self):
        return 2 * pi * self.polomer
    def objem(self):
        return pi * self.polomer ** 2 * self.vyska
    def obsah(self):
        return 2 * pi * self.polomer ** 2 + 2 * pi * self.polomer * self.vyska
    
def main():
    ctverec = Ctverec("Čtverec", 5)
    ctverec.vypis()
    krychle = Krychle("Krychle", 5)
    krychle.vypis()
    obdelnik = Obdelnik("Obdélník", 5, 10)
    obdelnik.vypis()
    kvadr = Kvadr("Kvádr", 5, 10, 15)
    kvadr.vypis()
    kruh = Kruh("Kruh", 5)
    kruh.vypis()
    koule = Koule("Koule", 5)
    koule.vypis()
    valec = Valec("Válec", 5, 10)
    valec.vypis()

if __name__ == "__main__":
    main()
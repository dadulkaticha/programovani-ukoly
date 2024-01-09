#dedicnost tvaru, vypocty zakladnich hodnot

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

class Ctverec(Tvar):
    def __init__(self, nazev, strana):
        super().__init__(nazev)
        self.strana = strana

    def obvod(self):
        return self.strana * 4

    def obsah(self):
        return self.strana ** 2
    
    def objem(self):
        return self.strana ** 3
    
class Obdelnik(Tvar):
    def __init__(self, nazev, stranaA, stranaB):
        super().__init__(nazev)
        self.stranaA = stranaA
        self.stranaB = stranaB

    def obvod(self):
        return (self.stranaA + self.stranaB) * 2

    def obsah(self):
        return self.stranaA * self.stranaB
    
    def objem(self):
        return self.stranaA * self.stranaB * self.stranaA
    
class Krychle(Tvar):
    def __init__(self, nazev, strana):
        super().__init__(nazev)
        self.strana = strana

    def obvod(self):
        return self.strana * 12

    def obsah(self):
        return self.strana ** 2 * 6
    
    def objem(self):
        return self.strana ** 3
    
class Kvadr(Tvar):
    def __init__(self, nazev, stranaA, stranaB, stranaC):
        super().__init__(nazev)
        self.stranaA = stranaA
        self.stranaB = stranaB
        self.stranaC = stranaC

    def obvod(self):
        return (self.stranaA + self.stranaB + self.stranaC) * 4

    def obsah(self):
        return (self.stranaA * self.stranaB + self.stranaA * self.stranaC + self.stranaB * self.stranaC) * 2
    
    def objem(self):
        return self.stranaA * self.stranaB * self.stranaC
    
class Kruh(Tvar):
    def __init__(self, nazev, polomer):
        super().__init__(nazev)
        self.polomer = polomer

    def obvod(self):
        return self.polomer * 2 * pi

    def obsah(self):
        return self.polomer ** 2 * pi
    
    def objem(self):
        return self.polomer ** 3 * pi * 4 / 3
    
class Valec(Tvar):
    def __init__(self, nazev, polomer, vyska):
        super().__init__(nazev)
        self.polomer = polomer
        self.vyska = vyska

    def obvod(self):
        return self.polomer * 2 * pi

    def obsah(self):
        return self.polomer ** 2 * pi * 2 + self.polomer * 2 * pi * self.vyska
    
    def objem(self):
        return self.polomer ** 2 * pi * self.vyska
    
class Koule(Tvar):
    def __init__(self, nazev, polomer):
        super().__init__(nazev)
        self.polomer = polomer

    def obvod(self):
        return self.polomer * 2 * pi

    def obsah(self):
        return self.polomer ** 2 * pi * 4
    
    def objem(self):
        return self.polomer ** 3 * pi * 4 / 3
    
def main():
    print(Ctverec("Čtverec", 5).obvod())
    print(Ctverec("Čtverec", 5).obsah())
    print(Ctverec("Čtverec", 5).objem())
    print(Obdelnik("Obdélník", 5, 10).obvod())
    print(Obdelnik("Obdélník", 5, 10).obsah())
    print(Obdelnik("Obdélník", 5, 10).objem())
    print(Krychle("Krychle", 5).obvod())
    print(Krychle("Krychle", 5).obsah())
    print(Krychle("Krychle", 5).objem())
    print(Kvadr("Kvádr", 5, 10, 15).obvod())
    print(Kvadr("Kvádr", 5, 10, 15).obsah())
    print(Kvadr("Kvádr", 5, 10, 15).objem())
    print(Kruh("Kruh", 5).obvod())
    print(Kruh("Kruh", 5).obsah())
    print(Kruh("Kruh", 5).objem())
    print(Valec("Válec", 5, 10).obvod())
    print(Valec("Válec", 5, 10).obsah())
    print(Valec("Válec", 5, 10).objem())
    print(Koule("Koule", 5).obvod())
    print(Koule("Koule", 5).obsah())
    print(Koule("Koule", 5).objem())

if __name__ == "__main__":
    main()
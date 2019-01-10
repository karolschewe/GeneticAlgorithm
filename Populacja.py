import Osobnik
class Populacja:
    # wspolcznynniki
    pMutacji = 0.001
    wielkoscPopulacji = 50
    karaBoza = 5


    listaOsobnikow = []

    def __init__(self):
        for i in range(self.wielkoscPopulacji):
            nowy_osobnik = Osobnik.Osobnik(i)
            self.listaOsobnikow.append(nowy_osobnik)

    def wylicz_funkcje_celu(self):
        for i in self.listaOsobnikow:
            i.wyliczFunCelu()


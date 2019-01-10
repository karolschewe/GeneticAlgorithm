import Osobnik
class Populacja:
    # wspolcznynniki
    pMutacji = 0.001
    wielkoscPopulacji = 50


    listaOsobnikow = []

    def __init__(self):
        for i in range(self.wielkoscPopulacji):
            self.listaOsobnikow.append(Osobnik.Osobnik(i))

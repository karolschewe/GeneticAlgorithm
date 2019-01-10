import Osobnik
import random
from numpy.random import choice


class Populacja:
    # wspolcznynniki
    pMutacji = 0.001
    wielkoscPopulacji = 50

    listaOsobnikow = []

    def __init__(self):
        for i in range(self.wielkoscPopulacji):
            nowy_osobnik = Osobnik.Osobnik(i)
            self.listaOsobnikow.append(nowy_osobnik)

    def wylicz_funkcje_celu(self):
        for i in self.listaOsobnikow:
            i.wyliczFunCelu()

    def ruletka(self):
        suma = 0
        probList = []
        kopulacja = []
        for i in self.listaOsobnikow:
            suma += i.funkcja_celu
        for j in self.listaOsobnikow:
            probList.append(j.funkcja_celu/suma)
        for k in range(50):
            kopulacja.append(choice(self.listaOsobnikow,p=probList))
        return (kopulacja)

    def krzyzowanie(self):
        pulaRodzicielska = self.ruletka()
        pary = choice(pulaRodzicielska,size=(25,2))
        nowaPopulacja = []
        id = 0
        for i in pary:
            dziecko1 = []
            dziecko2 = []
            miejsce = random.randint(0,364) # po ktorym genie jest mutacja
            lewa = random.getrandbits(1) #po ktorej stronie zachodzi wymiana 1 - po lewej
            if lewa == 1:
                for j in range(miejsce):
                    dziecko1.append(i[1].genom[j])
                    dziecko2.append(i[0].genom[j])
                for k in range(miejsce,365):
                    dziecko1.append(i[0].genom[j])
                    dziecko2.append(i[1].genom[j])
            else:
                for j in range(miejsce):
                    dziecko1.append(i[0].genom[j])
                    dziecko2.append(i[1].genom[j])
                for k in range(miejsce,365):
                    dziecko1.append(i[1].genom[j])
                    dziecko2.append(i[0].genom[j])
            nowaPopulacja.append(Osobnik.Osobnik(id = id, genom=dziecko1))
            id += 1
            nowaPopulacja.append(Osobnik.Osobnik(id = id, genom=dziecko2))
            id += 1

        self.listaOsobnikow=nowaPopulacja












    def mutacja(self):
        for i in self.listaOsobnikow:
            temp = []
            for j in i.genom_kopia:
                if random.random() < self.pMutacji:
                    if j == 0:
                        temp.append(1)
                    else:
                        temp.append(0)
                else:
                    temp.append(j)
            i.genom = temp


    def printPop(self):
        for i in self.listaOsobnikow:
            print("id:"+str(i.id))
            print(i.genom)




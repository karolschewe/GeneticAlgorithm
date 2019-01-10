import random


def oblicz_wspo_trawy(d):
    if d < 50 or d > 300:
        wzrost_trawy = 0
    elif 50 <= d <= 120:
        wzrost_trawy = 1
    elif 120 < d <= 200:
        wzrost_trawy = 2
    elif 200 < d <= 300:
        wzrost_trawy = 0.5

    else:
        wzrost_trawy =69

    return wzrost_trawy


class Osobnik:
    id = 69
    funkcja_celu = 0
    genom = []
    genom_kopia = []

    def __init__(self,id = 0):
        temp = []
        for i in range(365):
            rand = random.random()

            if rand > 0.5:
                temp.append(1)
            else:
                temp.append(0)
        self.genom = temp
        self.genom_kopia = self.genom
        self.id = id


    def wyliczFunCelu(self):
        temp_val = 1000
        dzien = 1
        dlugosc_trawy = 5
        wzrost_trawy = 0
        for i in self.genom:
            wzrost_trawy = oblicz_wspo_trawy(dzien)
            if i == 1:
                if dzien % 7 == 0:
                    temp_val -= 50

                if dlugosc_trawy > 15:
                    temp_val -= (dlugosc_trawy-15) ** 2
                elif 5 < dlugosc_trawy <= 15:
                    temp_val -= (15 - dlugosc_trawy)
                else:
                    temp_val -= 500

                dlugosc_trawy = 5

            else:
                dlugosc_trawy += wzrost_trawy

            dzien =+ 1
        self.funkcja_celu = temp_val
        #print(temp_val)
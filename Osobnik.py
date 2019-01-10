import random

class Osobnik:
    id = 69
    genom = []
    genom_kopia = []

    def __init__(self,id = 0):
        for i in range(365):
            if random.random() > 0.5:
                self.genom.append(1)
            else:
                self.genom.append(0)

        self.genom_kopia = self.genom
        self.id = id


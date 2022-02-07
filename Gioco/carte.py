import random

SEMI = [('Bastoni', 'basto'), ('Coppe', 'coppe'), ('Denari', 'denar'), ('Spade', 'spade')]
VALORI = [('Asso', '01'), ('2', '02'), ('3', '03'), ('4', '04'), ('5', '05'), ('6', '06'), ('7', '07'), ('Fante', '08'), ('Cavallo', '09'), ('Re', '10')]


def get_mazzo():
    a = []
    i = 0
    for seme in SEMI:
        for valore in VALORI:
            a.append({'seme': seme[0], 'valore': valore[0], 'file': seme[1]+valore[1]+'.png', 'id': i})
            i += 1
    return a


# MAZZO = _calcola_mazzo()

def mischia(mazzo):
    random.shuffle(mazzo)


class Carta:
    def __init__(self, seme: str, valore: str, file: str, _id: int):
        self.seme = seme
        self.valore = valore
        self.file = file
        self.id = _id


class Mazzo:
    def __init__(self):
        self.carte = []
        self.genera()

    def pesca(self):
        return self.carte.pop()

    def genera(self):
        self.carte = []
        i = 0
        for seme in SEMI:
            for valore in VALORI:
                self.carte.append(Carta(seme[0], valore[0], seme[1] + valore[1] + '.png', i))
                i += 1

    def mischia(self):
        random.shuffle(self.carte)

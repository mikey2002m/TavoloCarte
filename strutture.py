import random
import math
from typing import Optional

SEMI = [('Bastoni', 'basto'), ('Coppe', 'coppe'), ('Denari', 'denar'), ('Spade', 'spade')]
VALORI = [('Asso', '01'), ('2', '02'), ('3', '03'), ('4', '04'), ('5', '05'), ('6', '06'), ('7', '07'), ('Fante', '08'), ('Cavallo', '09'), ('Re', '10')]


class Carta:
    def __init__(self, seme: str, valore: str, file: str, _id: int):
        self.seme = seme
        self.valore = valore
        self.file = file
        self.id = _id


class Giocatore:
    def __init__(self, nome: str):
        self.nome: str = nome
        self.carte = []
        self.fondi = 1000

    def rimuovi_carte(self):
        self.carte = []

    def get_carta(self, carta: Carta):
        self.carte.append(carta)

    def trova_carta(self, c_id: int):
        for i in range(self.carte.__len__()):
            if self.carte[i].id == c_id:
                return i

    def scarta_carta(self, c_id):
        return self.carte.pop(self.trova_carta(c_id))



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
        for _ in range(100):
            random.shuffle(self.carte)


class Tavolo:
    def __init__(self):
        self.mazzo: Mazzo = Mazzo()
        self.giocatori = []
        self.scarti = []
        self.visibili = []
        self.mazziere: int = 0
        self.aggiornamento = 0
        self.piatto = 0

    def nuovo_giocatore(self, giocatore: Giocatore):
        self.giocatori.append(giocatore)
        self.aggiornamento += 1

    def ritira_carte(self):
        self.scarti = []
        self.visibili = []
        for giocatore in self.giocatori:
            giocatore.rimuovi_carte()
        self.mazzo = Mazzo()
        self.mazzo.mischia()
        self.aggiornamento += 1

    def prossimo_mazziere(self):
        if self.mazziere + 1 > self.giocatori.__len__():
            self.mazziere = 0
        self.mazziere += 1
        self.aggiornamento += 1

    def trova_giocatore(self, nome) -> Optional[Giocatore]:
        for giocatore in self.giocatori:
            if giocatore.nome == nome:
                return giocatore
        return None

    def scarta_tavolo(self, giocatore: Giocatore, c_id: int):
        self.visibili.append({'giocatore': giocatore.nome, 'carta': giocatore.scarta_carta(c_id)})
        self.aggiornamento += 1

    def rimuovi_tavolo(self, id_carta: int):
        n = -1
        for i in range(self.visibili.__len__()):
            if self.visibili[i]['carta'].id == id_carta:
                n = i
                break
        self.scarti.append(self.visibili.pop(n)['carta'])
        self.aggiornamento += 1

    def scarta(self, giocatore: Giocatore, c_id: int):
        self.scarti.append(giocatore.scarta_carta(c_id))
        self.aggiornamento += 1

    def mazziere_carta_tavolo(self):
        self.visibili.append({'giocatore': 'Mazziere', 'carta': self.mazzo.pesca()})
        self.aggiornamento += 1

    def mazziere_dai_carta(self, giocatore: Giocatore):
        giocatore.get_carta(self.mazzo.pesca())
        self.aggiornamento += 1

    def dividi_piatto(self, a: str, b: str, c: str):
        if self.piatto <= 0:
            return
        div = math.ceil(self.piatto / 3)
        self.piatto = 0
        self.trova_giocatore(a).fondi += div
        self.trova_giocatore(b).fondi += div
        self.trova_giocatore(c).fondi += div

    def invia_piatto(self, giocatore: str, importo: int):
        g = self.trova_giocatore(giocatore)
        if g.fondi - importo >= 0:
            g.fondi -= importo
            self.piatto += importo

    def invia_a(self, giocatore: str, ricevente: str, importo: int):
        g1 = self.trova_giocatore(giocatore)
        g2 = self.trova_giocatore(ricevente)
        if g1.fondi - importo >= 0:
            g1.fondi -= importo
            g2.fondi += importo
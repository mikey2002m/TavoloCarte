from carte import Mazzo
from giocatore import Giocatore


class Tavolo:
    def __init__(self):
        self.mazzo: Mazzo = Mazzo()
        self.giocatori = []
        self.scarti = []
        self.visibili = []
        self.mazziere: int = 0

    def nuovo_giocatore(self, giocatore: Giocatore):
        if self.giocatori.__len__() == 0:
            self.mazziere = giocatore
        self.giocatori.append(giocatore)

    def ritira_carte(self):
        self.scarti = []
        self.visibili = []
        for giocatore in self.giocatori:
            giocatore.rimuovi_carte()

    def prossimo_mazziere(self):
        if self.mazziere + 1 > self.giocatori.__len__():
            self.mazziere = 0
        self.mazziere += 1

    def trova_giocatore(self, nome):
        for giocatore in self.giocatori:
            if giocatore.nome == nome:
                return giocatore
        return None

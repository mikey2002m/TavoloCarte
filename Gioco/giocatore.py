from carte import Mazzo, Carta


class Giocatore:
    def __init__(self, nome: str):
        self.nome: str = nome
        self.carte = []

    def rimuovi_carte(self):
        self.carte = []

    def get_carta(self, carta: Carta):
        self.carte.append(carta)

# Creare una classe player

class Player:

    def __init__(self, nickname, punteggio):
        self.nickname = nickname
        self.punteggio = punteggio

    def __str__(self):
        return f'{self.nickname}, {self.punteggio}'

    def __repr__(self):
        return f'{self.nickname}, {self.punteggio}'
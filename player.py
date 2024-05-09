# Creare una classe player

class Player:

    # Creare il metodo __init__
    def __init__(self, nickname, punteggio):
        self.nickname = nickname
        self.punteggio = punteggio

    # Creare il metodo __str__ solo per confermare la correttezza del codice scritto nel main
    def __str__(self):
        return f'{self.nickname}, {self.punteggio}'

    # Creare il metodo __repr__ solo per confermare la correttezza del codice scritto nel main
    def __repr__(self):
        return f'{self.nickname}, {self.punteggio}'
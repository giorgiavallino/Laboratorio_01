from random import shuffle

# Creare una classe domanda

class Domanda:

    # Creazione del metodo __init__()
    def __init__(self, domanda, livello, corretta, risposte):
        self.domanda = domanda
        self.livello = livello
        self.corretta = corretta
        self.risposte = risposte

    # Creazione del metodo __repr__ usato soltanto per fare la print delle domande disposte in un lista e assicurarsene
    # la giusta visualizzazione
    def __repr__(self):
        return f'{self.domanda} {self.livello} {self.corretta} {self.risposte}'

    def __str__(self):
        return f'{self.corretta}'

    # Creazione del metodo cambio_ordine al fine di modificare l'ordine delle risposte (giuste e sbagliate) in maniera
    # casuale
    def cambio_ordine(self):
        shuffle(self.risposte)
        return self.risposte
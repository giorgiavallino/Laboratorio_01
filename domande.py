# Importare la funzione shuffle dalla libreria random al fine di permettere lo svolgimento della funzione
# cambio_ordine()

from random import shuffle

# Creare una classe domanda

class Domanda:

    # Creare il metodo __init__
    def __init__(self, domanda, livello, corretta, risposte):
        self.domanda = domanda
        self.livello = livello
        self.corretta = corretta
        self.risposte = risposte

    # Creare il metodo __repr__ usato soltanto per fare la print delle domande disposte in un lista e assicurarsene
    # la giusta visualizzazione
    def __repr__(self):
        return f'{self.domanda} {self.livello} {self.corretta} {self.risposte}'

    # Creare il metodo __str__ usato soltanto per fare la print e controllare la corretta del codice scritto nel
    # main
    def __str__(self):
        return f'{self.corretta}'

    # Creare il metodo cambio_ordine al fine di modificare l'ordine delle risposte (giuste e sbagliate) in maniera
    # casuale
    def cambio_ordine(self):
        shuffle(self.risposte)
        return self.risposte
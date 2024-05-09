from random import randint

# Importare le classi

from domande import Domanda
from player import Player

# Codice del gioco

# Leggere il file delle domande e dividerlo in righe

with open("domande.txt", "r") as file:
    linee_01 = file.readlines()

# Creare una lista all'interno della quale ogni elemento corrisponda a uan domanda compresa del suo testo, del suo
# punteggio e delle sue risposte

domande = []

for i in range(0, len(linee_01), 7):
    domande.append(Domanda(linee_01[i], linee_01[i+1], linee_01[i+2], linee_01[i+2:i+6]))

print(f'Questo è Trivia Game ed è appena arrivato il momento di giocare')
print(" ")

# Inizializzare le variabili iniziali

difficoltà = 0
punti = 0

# Game

while True:

    domande_possibili = [domanda for domanda in domande if int(domanda.livello) == difficoltà]

    if not domande_possibili:
        print(f'Hai completato il gioco raggiungendo la difficoltà massima. Congratulazioni!')
        nome = input("Inserisci il tuo nickname: ")
        break

    k = randint(0, len(domande_possibili)-1)

    domanda_assegnata = domande_possibili[k]

    print(f'Livello di difficoltà {domanda_assegnata.livello}'f'{domanda_assegnata.domanda}')

    risposte_possibili = domanda_assegnata.cambio_ordine()

    for j in range(0,(len(risposte_possibili))):
        print(f'{j+1}. {risposte_possibili[j]}')

    numero_risposta = int(input("Inserisci il numero della risposta corretta: "))

    risposta = risposte_possibili[numero_risposta-1]

    if risposta != domanda_assegnata.corretta:
        print(f'Risposta sbagliata! La risposta corretta era: {domanda_assegnata.corretta}')
        nome = input("Inserisci il tuo nickname: ")
        break

    else:
        print("Risposta corretta")
        punti = punti + 1
        difficoltà = difficoltà + 1

with open("punti.txt", "r") as file:
    contenuto = file.read()
    parole = contenuto.split()

giocatori = []

for i in range(0, len(parole), 2):
    giocatori.append(Player(parole[i], parole[i+1]))

giocatori.append(Player(nome, punti))

giocatori.sort(key=lambda x: int(x.punteggio), reverse = True)

print(f'Classifica finale visualizzabile anche nel file punti.txt')

with open("punti.txt", "w") as file:
    for giocatore in giocatori:
        file.write(f'{giocatore.nickname} {giocatore.punteggio}\n')
        print(f'{giocatore.nickname} {giocatore.punteggio}')
# Importare la funzione choice dalla libreria random

from random import choice

# Importare le classi Domanda e Player

from domande import Domanda
from player import Player

# Codice del gioco

# Leggere il file delle domande e dividerlo in righe

with open("domande.txt", "r") as file:
    linee_01 = file.readlines()

# Creare una lista all'interno della quale ogni elemento corrisponda a una domanda compresa del suo testo, del suo
# punteggio e delle sue risposte
# Questo procedimento crea una lista annidata, ossia una lista all'interno di una lista

domande = []

for i in range(0, len(linee_01), 7):
    domande.append(Domanda(linee_01[i], linee_01[i+1], linee_01[i+2], linee_01[i+2:i+6]))

#

print(f'Questo è Trivia Game ed è appena arrivato il momento di giocare')
print(" ")

# Inizializzare le variabili iniziali riferite alla difficoltà della domanda, inizialmente zero, e ai punti di ciascun
# giocatore, anch'essi inizialmente zero

difficoltà = 0
punti = 0

# Creare un ciclo while il quale gestisca le domande sottoposte all'utente e le relative risposte

while True:

    # Creare una lista domande_possibili contenente le domande a cui è possibile sottoporre l'utente in base
    # al livello di difficoltà

    domande_possibili = [domanda for domanda in domande if int(domanda.livello) == difficoltà]

    # Creare un ciclo che gestisca la situazione nella quale si giunge al massimo livello di difficoltà... in questo
    #caso, infatti, si conclude il gioco e si ottiene il punteggio massimo

    if not domande_possibili:
        print(f'Hai completato il gioco raggiungendo la difficoltà massima. Congratulazioni!')
        nome = input("Inserisci il tuo nickname: ")
        break

    # Scegliere una domanda da assegnare all'utente tra le domande possibili selezionate precedentemente

    domanda_assegnata = choice(domande_possibili)

    #

    print(f'Livello di difficoltà {domanda_assegnata.livello}'f'{domanda_assegnata.domanda}')

    # Inizializzare le risposte possibili alla domanda assegnata all'utente cambiandone l'ordine di visualizzazione

    risposte_possibili = domanda_assegnata.cambio_ordine()

    #

    for j in range(0,(len(risposte_possibili))):
        print(f'{j+1}. {risposte_possibili[j]}')

    # Craere un input tramite il quale l'utente può inserire il numero della risposta che vuole dare

    numero_risposta = int(input("Inserisci il numero della risposta corretta: "))

    # Creare un correlazione tra il numero della risposta e la risposta effettiva in stringa (come Europa, AFrica,...)

    risposta = risposte_possibili[numero_risposta-1]

    # Creare un ciclo nel quale viene gestista la correttezza della risposta data:
    # se la risposta è incorretta, allora indicare che la risposta è sbagliata, segnalare la risposta corretta e
    # interrompere il gioco chiedendo il nickname dell'utente

    if risposta != domanda_assegnata.corretta:
        print(f'Risposta sbagliata! La risposta corretta era: {domanda_assegnata.corretta}')
        nome = input("Inserisci il tuo nickname: ")
        break

    # se la risposta è corretta, il gioco prosegue segnalando che la risposta data era giusta e aumentando sia i
    # punti di un'unità che il livello di difficoltà

    else:
        print("Risposta corretta!")
        punti = punti + 1
        difficoltà = difficoltà + 1

# Aprire il file contenente i punti e dividerlo in singole parole

with open("punti.txt", "r") as file:
    contenuto = file.read()
    parole = contenuto.split()

# Creare una lista giocatori in cui per ogni giocatore venga inserito il suo nickname e il suo punteggio

giocatori = []

for i in range(0, len(parole), 2):
    giocatori.append(Player(parole[i], parole[i+1]))

giocatori.append(Player(nome, punti))

# Ordinare la lista giocatori in base al punteggio decresecente

giocatori.sort(key=lambda x: int(x.punteggio), reverse = True)

#

print(f'Classifica finale visualizzabile anche nel file punti.txt')

# Scrivere sul file punti.txt per ogni giocatore il nickname e il punteggio aggiornandolo ogni qualvolta entri in
# gioco un nuovo utente

with open("punti.txt", "w") as file:
    for giocatore in giocatori:
        file.write(f'{giocatore.nickname} {giocatore.punteggio}\n')
        print(f'{giocatore.nickname} {giocatore.punteggio}')
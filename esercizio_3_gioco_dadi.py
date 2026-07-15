#ESERCIZIO_3

#importo modulo 'random' per simulare il lancio dei dadi tramite '.randint'
import random
#stringa di benvenuto
print("\nBENVENUTI NEL GAME!\nfaremo una partita a dadi, max due giocatori\ninserisci il nome dei due giocatori")
#inserimento dei nomi di due giocatori
giocatore_1 = input()
giocatore_2 = input()
print(f"benvenuti \n{giocatore_1} e {giocatore_2} \n====================GAME START====================")

#definisco il valore iniziale delle variabili che useremo dopo
punteggio_g1 = 0
punteggio_g2 = 0

#funzione che simula il gioco
def lancio_dadi():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    return dado1, dado2

def giocata():
    global punteggio_g1, punteggio_g2
    input("premi invio per lanciare i dadi")
    
    tiro1g1, tiro2g1 = lancio_dadi()
    print(f"{giocatore_1} ha fatto {tiro1g1} - {tiro2g1}")
    
    tiro1g2, tiro2g2 = lancio_dadi()
    print(f"{giocatore_2} ha fatto {tiro1g2} - {tiro2g2}")
    
    if tiro1g1 in (tiro1g2, tiro2g2) or tiro2g1 in (tiro1g2, tiro2g2):
        print(f"\n{giocatore_1} ha vinto il round")
        punteggio_g1 = (punteggio_g1 + 1)
    else:
        print(f"\n{giocatore_2} ha vinto il round")
        punteggio_g2 = (punteggio_g2 + 1)

# Il ciclo continua finché NESSUNO dei due ha ancora raggiunto 3 vittorie
while punteggio_g1 < 3 and punteggio_g2 < 3:
    giocata()

# Chi ha raggiunto 3 vittorie vince la partita
if punteggio_g1 > punteggio_g2:
    print(f"\ncongratulazioni {giocatore_1}! hai vinto la partita per {punteggio_g1} round a {punteggio_g2}")
elif punteggio_g1 < punteggio_g2:
    print(f"\ncongratulazioni {giocatore_2}! hai vinto la partita per {punteggio_g2} round a {punteggio_g1}")
import math


# Menù scelta figura geometrica
def menu():
    print("A: perimetro del quadrato")
    print("B: perimetro del cerchio")
    print("C: perimetro del rettangolo")
    scelta= input("inserisci la lettera corrispondente alla figura scelta: ").upper()
    return scelta 



# Funzione calcolo perimetro quadrato
def calcolo_perimetro_quadrato():
    lato = float(input("inserisci la lunghezza del lato del quadrato: "))
    perimetro = lato * 4
    print(f"Il perimetro del quadrato è: {perimetro}")

# Funzione calcolo perimetro cerchio
def calcolo_perimetro_cerchio():
    raggio = float(input("Inserisci il raggio del cerchio: "))
    circonferenza = 2 * math.pi * raggio
    print(f"La circonferenza del cerchio è: {circonferenza}")

# Funzione calcolo perimetro rettangolo
def calcolo_perimetro_rettangolo():
    base = float(input("Inserisci la lunghezza della base del rettangolo "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    perimetro = 2 * (base + altezza)
    print(f"Il perimetro del rettangolo è: {perimetro}")


# Funzione principale per eseguire il calcolo del perimetro
def calcolo_perimetro():
    scelta = menu()
    if scelta == 'A':
        calcolo_perimetro_quadrato()
    elif scelta == 'B':
        calcolo_perimetro_cerchio()
    elif scelta == 'C':
        calcolo_perimetro_rettangolo()
    else:
        print("Scelta non valida. Riprova.")

# Esecuzione del programma
calcolo_perimetro()
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Funzione per mostrare l'introduzione
void showIntroduction() {
    printf("Benvenuto al gioco di domanda/risposta!\n");
    printf("Rispondi correttamente alle domande per ottenere il punteggio più alto possibile.\n\n");
}

// Funzione per mostrare il menu
void showMenu() {
    printf("Menu:\n");
    printf("A) Iniziare una nuova partita\n");
    printf("B) Uscire dal gioco\n");
}

// Funzione per ricevere l'input dell'utente per il menu
char getMenuChoice() {
    char choice;
    printf("Inserisci la tua scelta (A/B): ");
    scanf(" %c", &choice);
    return choice;
}

// Funzione per iniziare una nuova partita
void startNewGame() {
    char name[50];
    int score = 0;
    int answer;

    // Ricevere il nome dell'utente
    printf("Inserisci il tuo nome: ");
    scanf("%s", name);

    // Domanda 1
    printf("\nDomanda 1: Qual è la capitale d'Italia?\n");
    printf("1) Milano\n2) Roma\n3) Napoli\n");
    printf("Risposta: ");
    scanf("%d", &answer);
    if (answer == 2) {
        score++;
    }

    // Domanda 2
    printf("\nDomanda 2: Qual è il risultato di 5 + 3?\n");
    printf("1) 6\n2) 8\n3) 9\n");
    printf("Risposta: ");
    scanf("%d", &answer);
    if (answer == 2) {
        score++;
    }

    // Domanda 3
    printf("\nDomanda 3: Quale tra questi è un linguaggio di programmazione?\n");
    printf("1) HTML\n2) CSS\n3) Python\n");
    printf("Risposta: ");
    scanf("%d", &answer);
    if (answer == 3) {
        score++;
    }

    // Mostrare il punteggio finale
    printf("\n%s, hai totalizzato un punteggio di %d punti.\n\n", name, score);
}

// Funzione principale
int main() {
    char choice;

    // Mostrare l'introduzione
    showIntroduction();

    // Ciclo principale del gioco
    while (1) {
        // Mostrare il menu
        showMenu();
        
        // Ricevere la scelta dell'utente
        choice = getMenuChoice();

        if (choice == 'A' || choice == 'a') {
            // Iniziare una nuova partita
            startNewGame();
        } else if (choice == 'B' || choice == 'b') {
            // Uscire dal gioco
            printf("Grazie per aver giocato! Arrivederci.\n");
            break;
        } else {
            // Scelta non valida
            printf("Scelta non valida. Riprova.\n");
        }
    }

    return 0;
}

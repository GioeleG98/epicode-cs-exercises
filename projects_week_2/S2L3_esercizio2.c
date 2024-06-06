#include <stdio.h>

int main() {
     int numero1, numero2;  // Dichiarazione delle variabili per i numeri inseriti    
     float media; // Dichiarazione della variabile per la media 
      
      printf("Calcoliamo la media di due numeri.\n");
      // Chiediamo all'utente di scrivere il primo numero  
     printf("Inserisci il primo numero: "); scanf("%d", &numero1);
     
     // Chiediamo all'utente di scrivere il secondo numero
    printf("Inserisci il secondo numero: "); scanf("%d", &numero2); 
    
    // Calcoliamo la media dei due numeri 
    media = (numero1 + numero2) / 2; // Ora usiamo '2' invece di '2.0'    
     
     // Stampiamo il risultato    
     printf("La media dei due numeri è: %.2f\n", media); return 0;
    
}
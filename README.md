# [TO]Bike scraping

## Premessa

[TO]Bike è un servizio di bike sharing disponibile nel Comune di Torino e in
altri comuni limitrofi.

Nonostante l'impegno del Comune di Torino verso gli open data i dati delle
stazioni non sono disponibili per terze parti, vedi laconica risposta:

```
Gentilissimo,

siamo spiacenti ma i dati non sono disponibili per terze parti.

Cordiali saluti

Lo Staff [TO]BIKE
```

Per usufruire degli stessi occorre quindi arrangiarsi.

## Come recuperare i dati

Scarichiamo la pagina che contiene le stazioni nel sito per il comune di Torino:
```
wget http://www.tobike.it/frmLeStazioni.aspx
```

Fortunatamente le stazioni sono contenute in un oggetto js chiamato RefreshMap:
```
grep -o "{RefreshMap(.*}" frmLeStazioni.aspx
```

## Descrizione dei dati

I dati delle singole stazioni sono contenuti in stringhe separati dal carattere
*|*. Ogni stringa contiene lo stesso tipo di dato per tutte le stazioni nel
seguente ordine:
- id delle stazioni
- numero voti per le stazioni
- media voto per le stazioni
- latitudine delle stazioni
- longitudine delle stazioni
- nomi delle stazioni
- stato biciclette nelle stazioni
- indicazione geografica delle stazioni (con markup html)
- indicazione dello stato della stazione
- il numero 14
- latitudine del Lidl di via Carlo Alberto in Torino
- longitudine del Lidl di via Carlo Alberto in Torino

Lo stato biciclette delle stazioni è un campo a larghezza fissa di 30 caratteri dove:
- il carattere 0 indica un posto bici vuoto
- il carattere 4 indica una bicicletta disponibile
- il carattere 5 indica una bicicletta non attiva
- le x sono segnaposto

Per esempio:
```
40x500000000000xxxxxxxxxxxxxxx
```
indica una bici disponibile, una bicicletta non attiva e dodici posti bici vuoti.

Per quanto riguarda lo stato della stazione:
- il carattere 0 indica che non ci sono problemi
- il carattere 2 indica che la stazione non è operativa
- il carattere 3 indica che la stazione è in cantiere
- il carattere 4 indica che la stazione è in fase di definizione

Gli stati diverso da 0 indicano che la stazione non è utilizzabile.

## Note

Questo sistema recupera solo i dati della città di Torino. Per recuperare i dati di
tutti i comuni dove funziona il servizio [TO]Bike serve un sistema di scraping più
evoluto.

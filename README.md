![Logo_retro](https://github.com/AssortedMine70/naoornever/assets/163904638/be38c79e-513b-4552-9f68-d98c554a9beb)
# [NAOorNever](http://naoornever.it/)

## CONTENT

## NAO Challenge 2024
Nelle precedenti edizioni, le missioni proposte ai team coinvolti riguardavano l'utilizzando del robot NAO per attività di solidarietà sociale, quest'anno il tema scelto è il **retail**, un settore che abbraccia la vendita di beni e servizi al pubblico.

### Progetto
Il presente report analizza l'implementazione di un sistema avanzato che unisce il robot umanoide NAO con un **modello di ai** hostato da un server llamafile (Licenza Apache) in grado di analizzare i dati dei clienti, comprendere i loro bisogni e adattare le interazioni del robot in tempo reale.
Ciò permette di ottimizzare il processo di vendita dei prodotti dell'azienda e posizionare **SICIS** all'avanguardia nel settore del **retail**.
Durante la conversazione con il cliente, il robot NAO non è statico ma interagisce con il cliente attraverso micro movimenti per rendere la customer experience più gradevole. I movimenti riguardano saluti, inchini, movimenti nei momenti di attesa e indicazioni a schermo quando sono presenti prodotti da mostrare al cliente.

Inoltre abbiamo posto soluzione anche alla necessità dell’azienda di essere più inclusiva. Questo fondamentale punto è stato reso possibile grazie ai sottotitoli del dialogo che vengono stampati a schermo, permettendo così per la prima volta ai non udenti di fare shopping in completa autonomia.
Altro aspetto di rilievo per il progetto è stato quello di garantire un'ottima tutela ambientale tramite una app che comunica col nao gestendo un inventario. In questo modo i lavoratori di **SICIS** possono adesso monitorare con agilità gli ordini, abbattendo il numero di spedizioni (decurtando quelle superflue), dunque salvaguardando l’ambiente.
- [x] accessibilità
- [x] sostenibilità

## Report codice

### Database

### AI

All'interno della directory [server]([https://github.com/AssortedMine70/naoornever/server/)](https://github.com/AssortedMine70/naoornever/tree/main/server) è contenuto il programma in python che funge da interfaccia tra il NAO e il modello di ai hostato in locale attraverso [llamafile](https://github.com/Mozilla-Ocho/llamafile) che aiuta il cliente a trovare il prodotto che cerca.
La connessione al NAO è effettuata dalla libreria [IOinterface.py]([https://github.com/AssortedMine70/naoornever/server/IOinterface.py) atrraverso un socket, il server riceve un file audio che il nao registra (che contiene la richiesta del cliente) e converte il file in testo attraverso [openai whisper](https://github.com/openai/whisper), poi impacchetta la richiesta in un contesto dedicato alal richiesta fatta e questa rinterazione si ripete finchè il cliente non decide di comprare un prodotto.

### Monitor

Il monitor consiste in una pagina web che si connette al server con un websocket, iil server invia i prodotti che il montor deve mostrare e ciò che il NAO sta dicendo al cliente in modo da fornire contemporaneamente informazioni sui pordotti e sottotitoli per garantitre accessibilità anche per chi ha problemi di udito. 

### App

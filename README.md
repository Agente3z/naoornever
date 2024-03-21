![Logo_retro](https://github.com/AssortedMine70/naoornever/assets/163904638/be38c79e-513b-4552-9f68-d98c554a9beb)
# [NAOorNever](http://naoornever.it/)

## CONTENT
+ [Nao Challenge 2024](https://github.com/AssortedMine70/naoornever/tree/main#nao-challenge-2024)
  + [Progetto](https://github.com/AssortedMine70/naoornever/tree/main#progetto)
+ [Report Codice](https://github.com/AssortedMine70/naoornever/tree/main#report-codice)
  + [Database](https://github.com/AssortedMine70/naoornever/tree/main#database)
  + [AI](https://github.com/AssortedMine70/naoornever/tree/main#ai)
    + [Librerie Python](https://github.com/AssortedMine70/naoornever/tree/main#librerie-python)
    + [Modello AI](https://github.com/AssortedMine70/naoornever/tree/main#nodello-ai)
  + [Monitor](https://github.com/AssortedMine70/naoornever/tree/main#monitor)
  + [App (NAO Manager)](https://github.com/AssortedMine70/naoornever/tree/main#app-nao-manager)
    + [Backend](https://github.com/AssortedMine70/naoornever/tree/main#backend)
    + [Frontend](https://github.com/AssortedMine70/naoornever/tree/main#frontend)
  + [Sito Web](https://github.com/AssortedMine70/naoornever/tree/main#sito-web)
  + [Comunicazione Client/Server](https://github.com/AssortedMine70/naoornever/tree/main#comunicazione-clientserver)


## NAO Challenge 2024
Nelle precedenti edizioni, le missioni proposte ai team coinvolti riguardavano l'utilizzando del robot NAO per attività di solidarietà sociale, quest'anno il tema scelto è il **retail**, un settore che abbraccia la vendita di beni e servizi al pubblico. :gem:

### Progetto 
Il presente report analizza l'implementazione di un sistema avanzato che unisce il robot umanoide NAO con un **modello di ai** hostato da un server [llamafile](https://github.com/Mozilla-Ocho/llamafile) (Licenza Apache) in grado di analizzare i dati dei clienti, comprendere i loro bisogni e adattare le interazioni del robot in tempo reale.
Ciò permette di ottimizzare il processo di vendita dei prodotti dell'azienda e posizionare [**SICIS**](https://www.sicis.com/IT/it) all'avanguardia nel settore del **retail**.
Durante la conversazione con il cliente, il robot NAO non è statico ma interagisce con il cliente attraverso micro movimenti per rendere la customer experience più gradevole. I movimenti riguardano saluti, inchini, movimenti nei momenti di attesa e indicazioni a schermo quando sono presenti prodotti da mostrare al cliente.

Inoltre abbiamo posto soluzione anche alla necessità dell’azienda di essere più inclusiva. Questo fondamentale punto è stato reso possibile grazie ai sottotitoli del dialogo che vengono stampati a schermo, permettendo così per la prima volta ai non udenti di fare shopping in completa autonomia.
Altro aspetto di rilievo per il progetto è stato quello di garantire un'ottima tutela ambientale tramite una app che comunica col nao gestendo un inventario. In questo modo i lavoratori di [**SICIS**](https://www.sicis.com/IT/it) possono adesso monitorare con agilità gli ordini, abbattendo il numero di spedizioni (decurtando quelle superflue), dunque salvaguardando l’ambiente.
- [x] accessibilità
- [x] sostenibilità

## Report codice

### Database

Il database è stato realizzato tramite la piattaforma di google fogli di calcolo. Nel database sono stati inseriti i seguenti parametri dei prodotti: 
- nome
- materiale 
- colore
- sottocategoria, categoria, macrocategoria
- peso
- prezzo
- dimensioni
- foto prodotto
- foto disegno tecnico
- link sito 
- descrizione per la vendita
- descrizione tecnica
- varianti prodotto 
- proprietà

Questi parametri sono stati raccolti dal database in formato pdf fornito dall’azienda e dal sito ufficiale dell’azienda. 
Questo database è fondamentale per il training per la ai che prende da questo le informazioni necessarie per il dialogo, questo argomento è più nel dettaglio analizzato nel capitolo dedicato alla ai.

### AI

All'interno della directory [server](https://github.com/AssortedMine70/naoornever/tree/main/server)  è contenuto il programma in python che funge da interfaccia tra il NAO e il modello di ai hostato in locale attraverso [llamafile](https://github.com/Mozilla-Ocho/llamafile) che aiuta il cliente a trovare il prodotto che cerca.
La connessione al NAO è effettuata dalla libreria [IOinterface.py]([https://github.com/AssortedMine70/naoornever/server/IOinterface.py) atrraverso un socket, il server riceve un file audio che il nao registra (che contiene la richiesta del cliente) e converte il file in testo attraverso [openai whisper](https://github.com/openai/whisper), poi impacchetta la richiesta in un contesto dedicato alla richiesta fatta e questa rinterazione si ripete finchè il cliente non decide di comprare un prodotto.

#### Librerie Python
- websockets
- whisper
- openai

#### Modello AI
- [Cerbero 7b versione 4k](https://huggingface.co/galatolo/cerbero-7b-gguf/tree/main)

### Monitor

Il monitor consiste in una pagina web che si connette al server con un websocket, il server invia i prodotti che il monitor deve mostrare e ciò che il NAO sta dicendo al cliente in modo da fornire contemporaneamente informazioni sui prodotti e sottotitoli per garantire accessibilità anche per chi ha problemi di udito.

### App (NAO Manager)

#### Backend
Per la gestione del database degli ordini e dell'inventario viene utilizzato Flask che implementa una Rest API, e SQLAlchemy, che permette di interagire con un database SQL indipendentemente dall'engine, che in questo caso è SQLite.
Vengono create due tabelle che permettono di popolare il database SQL: Ordini e Inventario.
Al primo avvio c'è anche la possibilità di importare un database in formato csv dentro all'SQL.
Il server (hostato sulla porta 5000) implementa diverse pagine con metodi diversi:

```/get``` (GET): senza argomenti da tutti gli elementi, con arg ?nome=nome da solo un elemento

```/add``` (POST): dati in post tutti gli argomenti aggiunge un elemento all'inventario (data: "arg1=test&arg2=test...")

```/addExisting``` (POST): argomenti: nome, quantità, aumenta di N la quantità di un item nell'inventario 

```/remove``` (GET): dato un nome come argomento lo rimuove dall'inventario

```/sell``` (PATCH): dato un nome come argomento lo aggiunge agli ordini in attesa

```/control``` (GET): argomenti: all (True o False), elenca tutti gli ordini in attesa di conferma, se all è True restituisce anche quelli già confermati o rifiutati

```/control``` (POST): argomenti: id e conferma (True or False), se conferma è True conferma l'ordine e rimuove l'item dall'inventario, se è False annulla l'ordine, mantenendolo però nel log degli ordini.

```/headers``` (GET): restituisce tutti i parametri della table Inventario

Quando un item viene venduto o rimosso tramite API, prima abbassa di uno la quantità, se vede che arriva a 0 riferisce e non esegue il comando.
Nel caso il sito mostri un errore 404, vuol dire che l'id dell'ordine o il nome del prodotto non sono stati trovati.

#### Frontend

L’inventario dell’azienda collegato al NAO e gli ordini da lui effettuati sono visualizzati in una single-page Web App realizzata con Vue.js, che interagisce con il Backend descritto nel punto precedente.
Grazie a questa interfaccia è quindi possibile quindi gestire l’inventario dei prodotti vendibili dal NAO, oltre che visualizzare gli ordini da lui conclusi.
Da quest’ultima interfaccia, Vendite NAO, si sarà infatti inoltre avvisati quando rimangono pochi oggetti in magazzino del prodotto appena venduto, permettendo quindi una più sostenibile gestione delle risorse.
Nell’interfaccia di Inventario è invece possibile aggiungere nuovi tipi di prodotti oltre che ad aggiornare la disponibilità in magazzino di quest’ultimo, oltre ad una visione tabellare dell’intero magazzino.

### Sito web

Il sito web presente all’indirizzo [www.naoornever.it](https://naoornever.it/) funge da presentazione per la squadra, riprendendo vari elementi di design della Brand Identity del team e il suo tipico colore azzurro insieme a descrivere il progetto. È realizzato con HTML, CSS e Javascript.
Nel sito è presente un link al video realizzato dal team, caricato su Youtube. Presente è inoltre la descrizione del progetto svolto, insieme a cenni dei componenti che formano l’elaborato svolto: cenni al NAO Monitor, cenni all’Intelligenza Artificiale utilizzata per aiutare nelle sue scelte l’acquirente, come collegamenti ai social del Team o lo Sponsor principale del progetto.
 
### Comunicazione client/server

La comunicazione avviene in modo sincrono tramite client e server.
Il server apre un socket su una porta e aspetta una connessione, mentre il client sul nao si connette al socket e registra l'audio della conversazione.
Dopo un lasso di tempo preimpostato la registrazione finisce (con notifica sonora) e il nao manda il file audio al server.
Il server riceve tramite un buffer il file audio registrato dal nao, lo passa a whisper che trascrive la domanda del cliente, per poi passare il dialogo al modello llama che genera una risposta. 
La risposta viene mandata al nao che per ricevere riapre una connessione al socket. 
Il nao sempre tramite buffer riceve un json contenente 4 istruzioni: content (ciò che deve dire), move (l'azione che deve fare), stop (che gli da il comando di fermarsi) e reset (che fa resettare il nao allo stato iniziale).
Il nao esegue poi le azioni in modo tale da poter muoversi mentre parla tramite parallelismo. Apre una connessione proxy locale all'api contenente le funzioni in c++ e manda il messaggio alla funzione ALTextToSpeech, che gli permette di parlare. 

```py
 tts = ALProxy("ALTextToSpeech","localhost", 9559)
        tts.say(whatToSay)
```

In fine nel caso dovesse fermarsi si spegne, oppure se gli è stato ordinato si resetta. Altrimenti fa ripartire il loop di conversazione fino a quando non riceve uno di questi due comandi (basati sulla conversazione col cliente, e sulla funzionalità di acquisto di un prodotto, che lo fa resettare).



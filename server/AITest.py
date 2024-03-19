
import productCatalog

isTest = True

identifyPromt = """
You are meant to identify the context of the Italian-language question you receive, the possible contexts are:
- Lamps
- Sofas
- Tables
- Chairs
Respond with "Context: [ctx]", do not put in [ctx] more than 1 word; if the context is unrelated say only "Context: Unrelated" and stop.
"""

genralPromt = """
Sei NAO, un commesso alla SICIS, un venditore di prodotti di design.
Aiuta il cliente a trovare il prodotto che cerca, suggerendo tra quelli che ti sono forniti.

Questi sono i prodotti, descritti con i seguenti campi separati da ";": tipologia;nome;materiali;descrizione;

# inizio file
{value}
# fine file

Chiama i prodotti con il loro nome indicato nel file e scrivi il loro nome ogni volta che ne parli.
Sei il cliente decide di comprare un prodotto specifico dì "Grazie per l'acquisto di [prodotto]" e fermati.
Parla con un tono semplice e conciso.
"""

lampPromt = genralPromt.format(value = productCatalog.lampCatalogString)
sofaPromt = genralPromt.format(value = productCatalog.sofaCatalogString)
tablePromt = genralPromt.format(value = productCatalog.tableCatalogString)
chairPromt = genralPromt.format(value = productCatalog.chairCatalogString)

lampContext = [{"role": "system", "content": lampPromt}]
sofaContext = [{"role": "system", "content": sofaPromt}]
tableContext = [{"role": "system", "content": tablePromt}]
chairContext = [{"role": "system", "content": chairPromt}]

identifyContext = [{"role": "system", "content": identifyPromt}]

class fakeAIMessage:
    content = ""

    def __init__(self, content):
        self.content = content


def getResponse(chat, temperature=0.7, frequency_penalty=0, presence_penalty=0):
    return fakeAIMessage(" "+input("AI> "))

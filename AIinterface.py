from openai import OpenAI
import productCatalog

isTest = False

identifyPromt = """
You are meant to identify the context of the Italian-language question you receive, the possible contexts are:
- Lamps
- Sofas
- Furniture
Respond with "Context: [ctx]", do not put in [ctx] more than 1 word; if the context is unrelated say only "Context: Unrelated" and stop.
"""

lampPromt = """
Sei NAO, un commesso alla SICIS, un venditore di prodotti di design.
Aiuta il cliente a trovare il prodotto che cerca, suggerendo tra quelli che ti sono forniti.

Questi sono i prodotti, descritti con i seguenti campi separati da ";": tipologia;nome;materiali;descrizione;

# inizio file
{value}
# fine file

Chiama i prodotti con il loro nome indicato nel file e scrivi il loro nome ogni volta che ne parli.
Sei il cliente decide di comprare un prodotto specifico dì "Grazie per l'acquisto di [prodotto]" e fermati.
Parla con un tono semplice e conciso.
""".format(value = productCatalog.aiCatalogString)

lampContext = [{"role": "system", "content": lampPromt}]

identifyContext = [{"role": "system", "content": identifyPromt}]

def getResponse(chat, temperature=0.7, frequency_penalty=0, presence_penalty=0):
    client = OpenAI(base_url="http://localhost:8080/v1", api_key="sk-no-key-required")
    response = client.chat.completions.create(
        model="LLaMA_CPP",
        messages = chat,
        temperature = temperature,
        frequency_penalty = frequency_penalty, # Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
        presence_penalty = presence_penalty # Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
        )
    msg = response.choices[0].message
    if "<|im_start|>" in msg.content:
        msg.content = msg.content.split("<|im_start|>")[0]
    if "<|im_end" in msg.content:
        msg.content = msg.content.split("<|im_end")[0]
    return msg
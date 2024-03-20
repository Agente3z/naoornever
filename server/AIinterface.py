#!/usr/bin/env python3

# AI library

# Imports
import productCatalog
from openai import OpenAI

# AI globals
testMode = False

# Fake message class
class fakeAIMessage:
    content = ""
    def __init__(self, content):
        self.content = content

# Identification prompt
identifyPrompt = """
Devi trovare l'argomento della domanda che ti viene posta tra quelli che trovi qui sotto (fornisci l'argomento pià vicino)
- Lampade
- Poltrone
- Tavoli
- Sedie
Rispondi con "Contesto: [ctx]", se non ha rientra in nessun argomento rispondi "Contesto: Altro" e fermati.
"""

# General sell prompt
genralPrompt = """
Sei NAO, un commesso alla SICIS, un venditore di prodotti di design, aiuta il cliente a trovare il prodotto che cerca, suggerendo tra quelli che ti sono forniti, non dimenticare mai i prodotti che sono descritti con i seguenti campi separati da "/": tipologia/nome/materiali/
# inizio prodotti
{value}
# fine prodotti
Chiama sempre i prodotti con il loro nome completo e riscrivi il loro nome ogli volta che ne parli, se il cliente vuole terminare la conversazione dì "stop" e fermati, se invece vuole acquistare un prodotto specifico dì "Grazie per l'acquisto di [prodotto]" e fermati.
"""
"""
Chiama i prodotti con il loro nome completo indicato nel file e scrivi il loro nome ogni volta che ne parli.
Se il cliente chiede di terminare la conversazione dì "stop" e fermati.
Sei il cliente decide di comprare un prodotto specifico dì "Grazie per l'acquisto di [prodotto]" e fermati.
Parla in modo semplice e conciso.
Le prossime cose che ti vengono dette sono dette dal cliente.
"""

# Specific prompt creation
lampPrompt = genralPrompt.format(value = productCatalog.lampCatalogString)
sofaPrompt = genralPrompt.format(value = productCatalog.sofaCatalogString)
tablePrompt = genralPrompt.format(value = productCatalog.tableCatalogString)
chairPrompt = genralPrompt.format(value = productCatalog.chairCatalogString)

# Context creation
lampContext = [{"role": "Sistema","content": lampPrompt}]
sofaContext = [{"role": "Sistema","content": sofaPrompt}]
tableContext = [{"role": "Sistema","content": tablePrompt}]
chairContext = [{"role": "Sistema","content": chairPrompt}]

identifyContext = [{"role": "Sistema","content": identifyPrompt}]

# Response request function
def getResponse(chat, temperature=0.7, frequency_penalty=0, presence_penalty=0):
    global isTest

    if testMode:
        return fakeAIMessage(" "+input("AI> "))
    else:
        # Connection to llamafile and copletion request
        client = OpenAI(base_url="http://localhost:8080/v1", api_key="sk-no-key-required")
        response = client.chat.completions.create(
            model="LLaMA_CPP",
            messages = chat,
            temperature = temperature,
            frequency_penalty = frequency_penalty, # Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
            presence_penalty = presence_penalty # Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
            )
        
        # Only 1st choice is selected
        msg = response.choices[0].message
        if "<|im_start|>" in msg.content:
            msg.content = msg.content.split("<|im_start|>")[0]
        if "<|im_end" in msg.content:
            msg.content = msg.content.split("<|im_end")[0]
        if "[|" in msg.content:
            msg.content = msg.content.split("[|")[0]
        return msg
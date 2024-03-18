#!/usr/bin/env python3

#import AIinterface as ai
import AITest as ai
import IOinterface as io
import copy as cp
import json
import productCatalog as pc

def makePkgString(content, move=0, stop=False, reset=False):
    return json.dumps({"content": content, "move": move, "stop": stop, "reset": reset})

def parse(string):
    move = 0
    reset = False
    io.webPack = {"products":[], "subtitle":string}

    if "acquisto" in string.lower() or "carrello" in string.lower():
        reset = True
        move = 1
    if "<debug>" in string:
        string = "Buongiorno prof, ci siamo riusciti"
        move = 1
    
    for prod in pc.allrecords:
        if prod.name.lower() in string.lower():
            io.webPack["products"].append(prod)
            print("found")
        print("test "+ prod.name.lower())

    print(io.webPack["products"][0])
    
    return string, move, reset

debugMode = True
def debug(string):
    global debugMode
    if debugMode:
        print("Debug: "+string)


def main():
    debug("Main function started")
    io.mode = "debug" + "manual" + "web" #+ "nao" + "stt" #"nao" + "stt"#"stt" + "nao" # +"manual" + "web"
    io.naoPort = 50015
    io.initialize()

    stop = False

    while not stop:
        debug("Main loop start")

        intrest = None
        bought = False
        chat = None

        #io.sendOutput(makePkgString("Chiedimi quello che cerchi"))

        while not bought:
            debug("Buy loop start")
            qst = str(io.getInput()) # get input from user

            if "spegniti" in qst.lower(): # end condition
                debug("End condition detected")
                io.sendOutput(makePkgString("Mi sto spegnendo...", stop=True))
                bought = True
                stop = True
                continue

            if intrest == None:
                debug("Trying to find intrest")
                chat = ai.identifyContext
                chat.append({"role": "user", "content": qst})
                intrest = (ai.getResponse(chat, temperature=0.7).content+" null").split(" ")[1]

                debug(intrest)

                if "Lamps".lower() in intrest.lower():
                    chat = ai.lampContext
                elif "Unrelated".lower() in intrest.lower():
                    bought = True
                    io.sendOutput(makePkgString("Mi dispiace ma non sono in grado di gestire queste richieste", reset=True))
                else:
                    bought = True
                    io.sendOutput(makePkgString("Mi dispiace ma non sono in grado di gestire queste richieste", reset=True))
            
            if bought:
                continue
            
            chat.append({"role": "user", "content": qst})
            ans = ai.getResponse(chat, temperature=0.7)
            chat.append(cp.deepcopy(ans))

            whatToSay, whatToDo, shouldIReset = parse(ans.content)

            io.sendOutput(makePkgString(content=whatToSay, move=whatToDo, reset=shouldIReset))

            if shouldIReset:
                debug("Customer has bought")
                bought = True
            
            debug("Buy loop end")

        debug("Main loop end")

    io.close()

if __name__ == "__main__":
    main()

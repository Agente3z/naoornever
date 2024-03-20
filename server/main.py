#!/usr/bin/env python3

# Main program

# Imports
import json
import copy as cp
import AIinterface as ai
import IOinterface as io
import productCatalog as pc


# Output string creation
def makePkgString(content, move=0, stop=False, reset=False):
    return json.dumps({"content": content, "move": move, "stop": stop, "reset": reset})

# Input string parsing 
def parse(string):
    move = 0
    reset = False
    io.webPack = {"products":[], "subtitle":string}

    # Customer purchase check
    if "acquisto" in string.lower() or "stop" in string.lower():
        reset = True
        move = 1
    
    # Product parsing for monitor
    for prod in pc.allrecords:
        if prod.name.lower() in string.lower():
            io.webPack["products"].append(prod)
            debug("found "+prod.name.lower())

    return string, move, reset

# Toggleable debug function
debugMode = False
def debug(string):
    global debugMode
    if debugMode:
        print("Debug: "+string)


# Main function
def main():
    debug("Main function started")

    # IO modes and init
    io.mode = "debug" + "manual" + "web" #+ "nao" + "stt" #"nao" + "stt"#"stt" + "nao" # +"manual" + "web"
    io.naoPort = 50015
    io.initialize()

    # AI mode
    ai.testMode = False

    # Main loop check variable
    stop = False

    # Main loop
    while not stop:
        debug("Main loop start")

        intrest = None
        chat = None
        
        # Buy loop check function
        bought = False

        # Buy loop
        while not bought:
            debug("Buy loop start")

            # Input
            qst = str(io.getInput())

            # End condition for main loop
            if "spegniti" in qst.lower():
                debug("End condition detected")
                io.sendOutput(makePkgString("Mi sto spegnendo...", stop=True))
                bought = True
                stop = True
                continue

            # Intrest detection with ai
            if intrest == None:
                debug("Trying to find intrest")
                chat = ai.identifyContext
                chat.append({"role": "Umano", "content": qst})
                intrest = (ai.getResponse(chat, temperature=0.7).content+" null").split(" ")[1]

                debug(intrest)

                # Intrest check
                if "lampade" in intrest.lower():
                    chat = cp.deepcopy(ai.lampContext)
                elif "poltrone" in intrest.lower():
                    chat = cp.deepcopy(ai.sofaContext)
                elif "tavoli" in intrest.lower():
                    chat = cp.deepcopy(ai.tableContext)
                elif "sedie" in intrest.lower():
                    chat = cp.deepcopy(ai.chairContext)
                else:
                    bought = True
                    io.sendOutput(makePkgString("Mi dispiace ma non sono in grado di gestire queste richieste", reset=True))
            
            # No intrest detection starts a new buy loop
            if bought:
                continue
            
            # AI chat
            chat.append({"role": "Umano", "content": qst})
            ans = ai.getResponse(chat, temperature=0.7)
            chat.append(cp.deepcopy(ans))

            # AI response parsing
            whatToSay, whatToDo, shouldIReset = parse(ans.content)

            # Output
            io.sendOutput(makePkgString(content=whatToSay, move=whatToDo, reset=shouldIReset))

            # Buy loop end check
            if shouldIReset:
                debug("Customer has bought")
                bought = True
            
            debug("Buy loop end")

        debug("Main loop end")

    # IO closing
    io.close()


if __name__ == "__main__":
    main()

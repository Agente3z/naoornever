import socket
import websockets
import asyncio
import json
import time
from threading import *
import copy
#import whisper as wh

naoAddress = "172.16.7.250"
naoPort = 50015
serverSocket = None
bufSize = 1024*16
sttModel = None
webPack = {"products":[], "subtitle":None}

mode = "" # "test" and/or "nao" and/or stt and/or web

def initialize():
    global mode
    global serverSocket
    global naoPort
    global sttModel

    if "debug" in mode: print("IOinterface: Starting interface")

    if "nao" in mode:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serverSocket.bind((socket.gethostname(), naoPort))
        serverSocket.listen(1)

        # printing ip
        if "debug" in mode:
            print("IOinterface IP: " + socket.gethostbyname(socket.gethostname()))
            input("Press any button...")
    
#    if "stt" in mode:
#        sttModel = wh.load_model("medium")

    if "web" in mode:
        t = Thread(target=threadFunction, daemon=True)
        t.start()

def threadFunction():
    asyncio.run(webSockManager())

async def webSockManager():
    async with websockets.serve(sendArr, "localhost", 8766):
        await asyncio.Future()

async def sendArr(websocket):
    global webPack
    while True:
        #print(webPack["products"])

        sendPack = {"subtitle":webPack["subtitle"], "products":[]}

        for i in webPack["products"]:
            #print(i)
            sendPack["products"].append(i.to_dict())

        #print(json.dumps(sendPack))

        await websocket.send(json.dumps(sendPack))
        time.sleep(0.5)
        await asyncio.sleep(0)

def close():
    global mode
    global serverSocket

    if "nao" in mode:
        serverSocket.close()

def getInput():
    global mode
    global serverSocket
    global bufSize

    string = ""
    
    if "nao" in mode:
        clientConnection, addr = serverSocket.accept()
        with open("audio/file.wav", "wb") as f:

            if "debug" in mode: print("IOinterface: Started writing audio file")

            while True:
                b = clientConnection.recv(bufSize)
                if not b:
                    break
                f.write(b)

            if "debug" in mode: print("IOinterface: Finished writing audio file")

        clientConnection.close()
    
    if "manual" in mode:
        string = str(input("Input> "))

    elif "stt" in mode:
        string = sttModel.transcribe("audio\\file.wav", language="it", fp16=False)["text"]

    string = string.lower().strip()
    
    if "debug" in mode: print("IOinterface input: " + string)

    return string

def sendOutput(msg=""):
    global mode
    global serverSocket

    if "debug" in mode:
        print("Output> "+msg)
    
    if "nao" in mode:
        clientConnection, addr = serverSocket.accept()
        clientConnection.send(msg.encode("utf-8"))
        clientConnection.close()
#!/usr/bin/env python3

# IO library

# Imports
import json
import time
import socket
import asyncio
import websockets
import whisper as wh
from threading import *

# IO globals
naoAddress = "172.16.7.250"
naoPort = 50015
serverSocket = None
bufSize = 1024*16
sttModel = None
webPack = {"products":[], "subtitle":None}

# IO mode global
mode = ""
# mode += "debug" # -> Library debug messages
# mode += "nao" # -> NAO IO
# mode += "stt" # -> Whisper SpeechToText input
# mode += "manual" # -> Input
# mode += "web" # -> Web monitor

# IO init function
def initialize():
    global mode
    global serverSocket
    global naoPort
    global sttModel

    # Init debug
    if "debug" in mode: print("IOinterface: Starting interface")

    # NAO socket creation
    if "nao" in mode:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serverSocket.bind((socket.gethostname(), naoPort))
        serverSocket.listen(1)

        # Debugging host ip to ease connection
        if "debug" in mode:
            print("IOinterface IP: " + socket.gethostbyname(socket.gethostname()))
            input("Press any button...")
    
    # Whisper model loading
    if "stt" in mode:
        sttModel = wh.load_model("medium")

    # Web async thread strarting
    if "web" in mode:
        t = Thread(target=threadFunction, daemon=True)
        t.start()

# Thread function
def threadFunction():
    asyncio.run(webSockManager())

# Async socket management
async def webSockManager():
    async with websockets.serve(sendArr, "localhost", 8766):
        await asyncio.Future()

# Async socket send
async def sendArr(websocket):
    global webPack
    global mode

    while True:
        # Json convertable dictionary creation
        sendPack = {"subtitle":webPack["subtitle"], "products":[]}
        for i in webPack["products"]:
            print(i)
            sendPack["products"].append(i.to_dict())

        await websocket.send(json.dumps(sendPack))

        # Package debugging
        if "debug" in mode: print("IOinterface Monitor Package:"+json.dumps(sendPack))

        time.sleep(0.5)
        await asyncio.sleep(0)

# IO cloing function
def close():
    global mode
    global serverSocket

    if "nao" in mode:
        serverSocket.close()

# Input function
def getInput():
    global mode
    global serverSocket
    global bufSize

    # Input string
    string = ""
    
    # NAO audio file acquisition
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
    
    # Manual input acquisition
    if "manual" in mode:
        string = str(input("Input> "))
    
    # Whisper SpeechToText conversion 
    elif "stt" in mode:
        string = sttModel.transcribe("audio\\file.wav", language="it", fp16=False)["text"]

    # Input cleaning
    string = string.lower().strip()
    
    # Input debugging
    if "debug" in mode: print("IOinterface input: " + string)

    return string

# Output function
def sendOutput(msg=""):
    global mode
    global serverSocket

    # Output debugging
    if "debug" in mode:
        print("Output> "+msg)
    
    # Nao output
    if "nao" in mode:
        clientConnection, addr = serverSocket.accept()
        clientConnection.send(msg.encode("utf-8"))
        clientConnection.close()
        
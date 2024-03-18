# -*- encoding: UTF-8 -*-
import socket
import json
import struct
import copy as cp
from time import sleep
from naoqi import ALProxy
import time
import sys

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        reload(sys)
        sys.setdefaultencoding('utf8')

    def onLoad(self):
        pass

    def onUnload(self):
        pass

    def onInput_onStart(self):
        pass

    def onInput_onStop(self):
        self.onUnload()
        self.onStopped()

    def parla(self, s):
        data = s.recv(16384).decode('utf-8')
        msg = ""
        if not data:
            return
        while data:
            if not data:
                break
            else:
                msg += data
                data = s.recv(16384).decode('utf-8')
        msg = json.loads(msg)
        whatToSay = str(msg["content"])
        whatToDo = int(msg["move"])
        shouldIStop = bool(msg["stop"])
        shouldIReset = bool(msg["reset"])

        if (whatToDo == 1):
            self.inchino()
        if (whatToDo == 2):
            self.indicazione()
        if (whatToDo == 3):
            self.movimentialscolto()


        tts = ALProxy("ALTextToSpeech","localhost", 9559)
        tts.say(whatToSay)

        if (shouldIStop == True):
            self.spegnimento()
            time.sleep(2)
        elif (shouldIReset == True):
            self.reset()
            time.sleep(2)
        else:
            self.risposta()

    def manda(self, s, path):
        with open(path, "rb") as file:
            for b in file:
                s.sendall(b)

    def apriSocket(self, HOST, PORT):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while s.connect_ex((HOST, PORT)) != 0:
            sleep(1)
        return s

    def onInput_domanda_audio(self, path):
        HOST = '10.0.50.111'        #ip server
        PORT = 50015
        s = self.apriSocket(HOST,PORT)
        self.manda(s, path)
        s.close()

        s = self.apriSocket(HOST,PORT)
        self.parla(s)
        s.close()
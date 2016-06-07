# Orwell - Cross Platform Botnet and RAT package.

Orwell is a RAT and Botnet designed as a trio of programs. 
The bigbro.py, which is ran on a remote server and used to 
give commands and information to proles; the innerPart.py,
used to send commands to BB that are given to the proles;
and prole.py, used as the zombie client. Prole.py currently
supports Unix-Like OSes (MacOS and Linux) and Windows.

## A quick tutorial on the use of Orwell - 
* Run `bigbro.py` on a server of your choice, and forward the port '1984'.
* The `bigbro.py` file will ask for a password. Set and remember a secure one.
* Change the `bigBro` variable on line 9 of `prole.py` to `bigbro.py`'s IP.
* Compile `prole.py` for the OSes you're targeting using the resources below.
* Run your compiled prole executable on zombie systems. 
* Run the `innerParty.py` file on your home computer. Consider a proxy or Torify.
* The `innerParty.py` file will ask you for BB's IP and for BB's password. 
* Congrats, you're now running a full Orwell botnet.

## Orwell commands - 
* `shell`   - Run command line code on a prole.
* `log`     - Print a string to a prole's prompt.
* `kill`    - Shuts down a prole's system.
* `~`, `s`, or `switch` - Change who a command is sent to based upon an IP.
* `?`, `l`, or `listen` - Listen for emits for a given time, or even 'forever'.

# TO COMPILE OR RUN, - 
## You'll need this stuff - 
*    https://pypi.python.org/pypi/socketIO-client
*    https://pypi.python.org/pypi/python-socketio
*    https://pypi.python.org/pypi/eventlet

## And these are default, but you also need them - 
*    https://docs.python.org/2/library/urllib2.html
*    https://docs.python.org/2/library/hashlib.html

This is the work of Landon Powell, and is licensed under 
Creative Commons Zero. A non-professional and 
not-applicable-in-a-court-of-law summary of the license 
is effectively: do whatever you want with this.
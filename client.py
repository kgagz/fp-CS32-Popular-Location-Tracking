'''
client.py forms the client/users end of the network. It finds the users ip address using https://ident.me
API, and then sends that ip address to the server.
'''
import socket
import os
from urllib.request import urlopen

def get_ip():
    '''
    get_ip finds the public ip address of the device where the code is run
    '''
    public_ip = urlopen('https://ident.me').read().decode('utf8')
    return public_ip

#initializes our socket
s=socket.socket()

host='127.0.0.1' #run through local host for now
port=6557 #same as server

#connects to server socker and sends ip address as a string
s.connect((host,port))
content = str(get_ip())
s.send(content.encode())
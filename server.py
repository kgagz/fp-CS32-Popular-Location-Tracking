'''
server.py forms the server end of the network piece. It collects the ip addresses sent from the users,
collects them into a list, and then uses this list to create a csv file of ip addresses.
'''
import socket
import csv
import os
import sys

#initializes our socket
s=socket.socket()

host= '127.0.0.1' #run through local host for now
port=6557 #ports after 6000 are free

#bind to socket
s.bind((host,port))

s.listen(10)

#initializes list in which to place the ip addresses
ip_addresses = []
while True:
    #receives messages
    c,addr=s.accept()
    content=c.recv(100).decode()
    if not content:
        print('no msg')
        break

    #adds ip address to list
    ip_addresses.append(str(content))

    #creates a new csv file "test2.csv" with all of the ip addresses
    data = ['ip']
    new = "C:\\Users\\Kathryn\\desktop\\fp\\test2.csv"
    with open(new, 'w', newline= '') as work:
        z = csv.writer(work)
        z.writerow(data)
        for num in range(len(ip_addresses)):
            z.writerow(ip_addresses[num:num+1])
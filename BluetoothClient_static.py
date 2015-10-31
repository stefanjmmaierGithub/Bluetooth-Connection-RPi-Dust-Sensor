
"""
A simple Python script to send messages to a sever over Bluetooth using 
Python sockets (with Python 3.3 or above). 
"""

import socket
size =1204
serverMACAddress = '00:1A:7D:DA:71:15' #Test mit Mac Raspi
port = 5

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
print("Which message to send? ")

    
while 1:
       print("Which message to send?")
       text = input()
       if text == "quit":
          break
       s.send(bytes(text, 'UTF-8'))
       data = s.recv(size)
       print("Respond from Server:", data)

s.close()


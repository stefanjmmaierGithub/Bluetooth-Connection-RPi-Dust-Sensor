
"""
A simple Python script to send messages to a sever over Bluetooth using 
Python sockets (with Python 3.3 or above). 
"""

import socket
import time

serverMACAddress = '00:1A:7D:DA:71:15' #Test mit Mac Raspi
port = 3 
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
 
class BluetoothClient(object):
        
      def connectToServer():                      
                         s.connect((serverMACAddress,port))
                         print("Which message to send? ")
                         return "Connection to Server Enabled"

      def getData(datatyp):
                         size =1204
                         s.send(bytes(datatyp, 'UTF-8'))
                         data = s.recv(size)
                         print("Respond from Server:", data)
                         return data
      
      def closeServerConnection():
                               s.send(bytes("quit", 'UTF-8'))
                               time.sleep(0.5)
                               s.close()
                               return "Connection to Server Closed"

      def __del__(self):
        print (self.name, 'died')
        


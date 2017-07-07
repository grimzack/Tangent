# client.py

# This serves as the Client Agent for the Tangent Chat Client

''' 
Example Socket program from https://docs.python.org/2/library/socket.html#example
'''

# Echo client program
import socket
import sys

HOST = 'localhost'    # The remote host
PORT = 1111              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while 1:
	message = raw_input("user$ ")
	if (message == '/exit'):
		break

	s.sendall(message)
	data = s.recv(1024)
s.close()
print 'Received', repr(data)
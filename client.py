# client.py

# This serves as the Client Agent for the Tangent Chat Client

''' 
Example Socket program from https://docs.python.org/2/library/socket.html#example
'''

# Echo client program
import socket
import sys

HOST = 'localhost'    # The remote host
PORT = 1111           # The same port as used by the server
username = ''

def send_message():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))

	print "Username = " + username
	while 1:
		message = raw_input(username + "$ ")
		if (message == '/exit'):
			message = 'Leaving chat'
			break

		s.sendall(message)
		data = s.recv(1024)
	s.close()

def main():
	global username
	for arg in sys.argv:
		if 'user' in arg:
			username = arg[5:]

	if (username == ''):
		username = "John"

	print "Connecting with user " + username
	send_message()

main()
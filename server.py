# server.py

# This serves as the server agent for Tangent Chat Client

'''
Example Socket program from https://docs.python.org/2/library/socket.html#example
'''

# Echo server program
import socket
import threading

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 1111              # Arbitrary non-privileged port


def server_receive_message(conn, addr):
	# conn = args[0]
	# addr = args[1]
	print 'Connected by', addr
	while 1:
	    data = conn.recv(1024)
	    if not data: break
	    print 'Received message: ', data
	    conn.sendall(data)
	conn.close()

client_cxns = []
client_threads = []

def accept_clients():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	while 1: 
		s.listen(1)
		conn, addr = s.accept()
		client_cxns.append(conn)
		thread = threading.Thread(target=server_receive_message, args=(conn,addr))
		client_threads.append(thread)
		thread.start()

def main():
	print "Running main()"
	accept_clients()

main()
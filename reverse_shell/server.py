import socket
import sys

def socket_create():
	try:
		global host
		global port
		global s
		host = ''
		port = 9998
		s =socket.socket()
	except socket.error as message:
		print("Socket createion error " + str(message))

def socket_bind():
	try:
		print("Binding to port:" + str(port))
		s.bind((host,port))
		s.listen(400)
	except socket.error as message:
		print("Socket binding error "+ str(message) + "\n" + "Retrying")
		socket_bind()

def socket_accept():
	connection,address = s.accept()
	print("connection has benn established "+ " IP " + address[0] + "on port " + str(address[1]))
	send_commands(connection)
	connection.close()

def send_commands(connection):
	while True:
		command = input()
		if command == 'quit':
			connection.close()
			s.close()
			sys.exit()
		if len(str.encode(command)) > 0:
			connection.send(str.encode(command))
			client_response = str(connection.recv(1024), 'utf-8')
			print(client_response,end="")

def main():
	socket_create()
	socket_bind()
	socket_accept()
	
main()
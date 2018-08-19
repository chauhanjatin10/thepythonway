import socket
import struct
import textwrap

def main():
	connection = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,proto=0,fileno=None)
	while True:
		raw_data,address = connection.recv(65535)
		dest_mac,src_mac,eth_proto,data = ethernet_frame(raw_data)
		print("Ethernet frame: ")
		print("Destinatio: {}, Source: {},Protocol: {}".format(dest_mac,src_mac,eth_proto))

def ethernet_frame(data):
	dest_mac,src_mac,proto = struct.unpack('! 6s 6s H',data[:14])
	return get_mac_address(dest_mac),get_mac_address(src_mac),socket.htons(proto),data[:14]

def get_mac_address(byte_address):
	byte_string = map('{:02x}'.fromat,byte_address)
	return ':'.join(byte_string).upper()
	
main()
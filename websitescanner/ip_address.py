import os

def get_ip_address(url):
	command = "host " + url
	process = os.popen(command)
	final = str(process.read())
	results = final.find('has address') + 12
	return final[results:].splitlines()[0]
	

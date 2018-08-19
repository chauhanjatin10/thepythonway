import os

def get_dig(url):
	command = "dig " + url
	process = os.popen(command)
	results = str(process.read())
	return results


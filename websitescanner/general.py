import os

def create(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

def write(path,data):
	f = open(path,'w')
	f.write(data)
	f.close()


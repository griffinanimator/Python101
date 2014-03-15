import json
<<<<<<< HEAD

def writeJson(fileName, data, *args):
=======
def writeJson(fileName, data):
>>>>>>> More examples
	with open(fileName, 'w') as outfile:
		json.dump(data, outfile)

	file.close(outfile)

def readJson(fileName, *args):
	print fileName
	with open(fileName[0], 'r') as infile:
		data = (open(infile.name, 'r').read())
	return data

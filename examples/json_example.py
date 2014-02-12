import maya.cmds as cmds
import json
import tempfile

# An empty dictionary that will be used to store locator_info
locator_info_dictionary = {}

# Define a list containing locator info
locator_info = (['lctr1', [0.0,0.0,0.0]], ['lctr2', [1.0,0.0,-1.0]], ['lctr3', [2.0,0.0,0.0]])

# Assign locator_info to dictionary keys
# For this example we will look at using list comprehensions
# Read documentation here... http://docs.python.org/2/tutorial/datastructures.html#list-comprehensions        
        
locator_info_dictionary['names']= [locator_info[x][0] for x in range(len(locator_info))]
locator_info_dictionary['positions']= [locator_info[x][1] for x in range(len(locator_info))]

print "Here is the locator info "
print locator_info_dictionary
data = locator_info_dictionary


""" BREAK """



# These functions can be used to read and write json
# Define a path to the json file.
  
# NOTE: Change this to a path on your computer.
fileName = 'C:/Users/Griffy/Documents/GitHub/Python101/data/locator_info.json'

def writeJson(fileName, data):
	with open(fileName, 'w') as outfile:
		json.dump(data, outfile)

	file.close(outfile)

def readJson(fileName):
    with open(fileName, 'r') as infile:
        data = (open(infile.name, 'r').read())
    return data



""" Break """

    
# Now we will save to a json file
writeJson(fileName, data)

# Read the Json file
data = readJson(fileName)
info = json.loads( data )
info2 = json.dumps( data )


""" BREAK """

# Now take a look at the different data types returned by loads and dumps
print type(json.dumps( data ))
print type(json.loads( data ))

for key, value in info.iteritems():
    print key, value
    print type(value)

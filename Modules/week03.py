"""
    Stephanie Wagner
    week03 assignment
    I used the script you posted at the Week03 topic as a guidance and went through it step by step to understand the use of dictionaries.
"""

import maya.cmds as cmds
import json

locator_info_dictionary = {} #dic
locator_info = (["L_arm01",[0,0,0]],["L_arm02", [1,0,0]],["L_Wrist",[2,0,0]],["L_WristEnd", [3,0,0]]) #list
fileName = "C:/Users/Wagner/PersonalArt/Scripting/Rigging_Dojo/Python101/rigging/locator_info.json" #path

# Assign the list locator_info to locator_info_dictionary dictionary keys (name and position)
locator_info_dictionary["MyLOCNames"]=[locator_info[LOCname][0]for LOCname in range(len(locator_info))]
locator_info_dictionary["MyPosition"]=[locator_info[position][1]for position in range(len(locator_info))]

print locator_info_dictionary.items()

#json file

#write file name and dictionary
def writeJson(fileName, data): 
    with open(fileName, "w") as outfile:
        json.dump(data, outfile)
 
    file.close(outfile)
    
# read file name and dictionary
def readJson(fileName):
    with open(fileName, 'r') as infile:
        data = (open(infile.name, 'r').read())
    return data
 
data = readJson(fileName)
info = json.loads(data)
info2 = json.dumps(data)

writeJson(fileName, data) # save to Json

# Creae Locators and Joints
for name, position in locator_info:
   cmds.spaceLocator(name = name +("_LOC"), p = position)
   print ("This is " + name +"_LOC at position"), position

cmds.select(clear = True)

for name, position in locator_info:
   cmds.joint(name = name + ("_JNT"), p = position)
   print ("This is " + name +"_JNT at position"), position
   
cmds.select(clear = True)
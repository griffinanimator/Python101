# character_parts.py
import maya.cmds as mc
import json

jsonPath="D:/Users/Toby/Documents/GitHub/Python101/data/locator_info.json"

def writeJson(fileName, data):
    with open(fileName,"w") as outfile:
        json.dump(data,outfile)

    file.close(outfile)

def readJson(fileName):
    with open(fileName,"r") as infile:
        data=(open(infile.name,"r").read())
    return data


armDict={}

# arm dictionary
armDict["armJointNames"]=["ljnt_Shoulder","ljnt_Elbow","ljnt_Wrist"]
armDict["armJointPositions"]=[[32,0,0],[64,0,-16],[96,0,0]]
armDict["armIkHandle"]=["ljnt_Shoulder","ljnt_Wrist"]

writeJson(jsonPath,armDict)

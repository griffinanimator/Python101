# character_parts.py
import maya.cmds as mc
import json

tempDict={}

# arm dictionary
tempDict["armJointNames"]=["jnt_Shoulder","jnt_Elbow","jnt_Wrist"]
tempDict["armJointPositions"]=[[32,0,0],[64,0,-16],[96,0,0]]
tempDict["armIkHandle"]=["jnt_Shoulder","jnt_Wrist"]

print(tempDict["armJointNames"])
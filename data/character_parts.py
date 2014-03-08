# character_parts.py
import maya.cmds as mc
import json
import utils.jsonUtils as jsonUtils
jsonPath="C:/Users/Ganapathi K A/Documents/GitHub/Python101/data/locator_info.json"



armDict={}

# arm dictionary
armDict["armJointNames"]=["jnt_Shoulder","jnt_Elbow","jnt_Wrist"]
armDict["armJointPositions"]=[[32,0,0],[64,0,-16],[96,0,0]]
armDict["armAxis"]=["xyz"]
armDict["armIkHandle"]=["jnt_IKShoulder","jnt_IKWrist"]
armDict["IKJointNames"]=["jnt_IKShoulder","jnt_IKElbow","jnt_IKWrist"]
armDict["FKJointNames"]=["jnt_FKShoulder","jnt_FKElbow","jnt_FKWrist"]
armDict["FKControlNames"]=["FKshoulder","FKelbow","FKwrist"]
armDict["reverseNodes"]=["FKIKshoulderReverse","FKIKelbowReverse","FKIKwristReverse"]

jsonUtils.writeJson(jsonPath,armDict)

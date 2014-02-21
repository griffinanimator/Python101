# trArmRig.py
import maya.cmds as mc
import data.character_parts as parts
import json

def createJoints(suffix="_C"):
    for i in range(len(jsonData["armJointNames"])):
        mc.joint(name="{jointName}_{suffix}".format(jointName=jsonData["armJointNames"][i],suffix=suffix),
            position=jsonData["armJointPositions"][i])
    mc.select(clear=True)

jsonPath="D:/Users/Toby/Documents/GitHub/Python101/data/locator_info.json"
jsonData=parts.readJson(jsonPath)
jsonData=json.loads(jsonData)





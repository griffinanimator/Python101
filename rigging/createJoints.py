# createJoints.py
import maya.cmds as mc
import rigging.character_parts as parts


def createJoints(jointNames,jointPosition,suffix="_C"):
    for i in range(len(parts.tempDict[jointNames])):
        mc.joint(name="{jointName}_{suffix}".format(jointName=parts.tempDict[jointNames][i],suffix=suffix),
            position=parts.tempDict[jointPosition][i])

jointNames="armJointNames"
jointPosition="armJointPositions"
createJoints(jointNames,jointPosition,suffix="L")
###Orient Joint Tool
###Want to build this tool to be able to be selectable
import maya.cmds as cmds

def awOrientJoint():
    sel = cmds.ls(sl=1)
    for each in sel:
        cmds.joint(e=True, oj='xyz', secondaryAxisOrient='yup', ch=1, zso=True)
#awOrientJoint()
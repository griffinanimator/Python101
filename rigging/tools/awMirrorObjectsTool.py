##Mirrors the object that is selected
import maya.cmds as cmds

def awMirrorObjects():
    objects = cmds.ls(sl=1)
    if len(objects) == 0:
        cmds.warning('Select objects')
    else:
        cmds.duplicate(rr=True)
        myGroup = cmds.group()
        cmds.xform(os=True, piv=(0, 0, 0))
        cmds.setAttr(myGroup + '.sx', -1)
        cmds.select(myGroup)
        cmds.ungroup
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        
awMirrorObjects()
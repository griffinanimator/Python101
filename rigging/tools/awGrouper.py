#until I figure out a more logical way to write this, you can only use
#one instance of this within a scene. 
#If you use it more than once, you have to delete all the groups this creates to be able to reuse it. 


import maya.cmds as cmds

def awMasterGroupCreator():
    group = cmds.group(n='character01', em=True, w=True)
    cmds.setAttr('character01.tx', lock=True, k=False, cb=False)
    cmds.setAttr('character01.ty', lock=True, k=False, cb=False)
    cmds.setAttr('character01.tz', lock=True, k=False, cb=False)
    cmds.setAttr('character01.rx', lock=True, k=False, cb=False)
    cmds.setAttr('character01.ry', lock=True, k=False, cb=False)
    cmds.setAttr('character01.rz', lock=True, k=False, cb=False)
    cmds.setAttr('character01.sx', lock=True, k=False, cb=False)
    cmds.setAttr('character01.sy', lock=True, k=False, cb=False)
    cmds.setAttr('character01.sz', lock=True, k=False, cb=False)
    for grp in range(10):
        cmds.duplicate(group)
    joints = cmds.rename('character02', 'joints01')
    locators = cmds.rename('character03', 'locators01')
    ikHandles = cmds.rename('character04', 'ikHandles01')
    fkControls = cmds.rename('character05', 'fkControls01')
    ikControls = cmds.rename('character06', 'ikControls01')
    transforms = cmds.rename('character07', 'to_transforms01')
    blendshapes = cmds.rename('character08', 'blendshapes01')
    model = cmds.rename('character09', 'model01')
    toShow = cmds.rename('character010', 'extra_toShow01')
    toHide = cmds.rename('character011', 'extra_toHide01')
    globalM = cmds.group(n='globalMove01', em=True, w=True)
    cmds.parent(globalM, group)
    cmds.parent(joints, locators, ikHandles, fkControls, ikControls01, globalM)
    cmds.parent(transforms, blendshapes, model, toShow, toHide, group)

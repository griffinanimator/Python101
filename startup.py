import os
import sys
import maya.cmds as cmds
print sys.path

# check sys.path
if "C:\\Users\\Wagner\\PersonalArt\\Scripting\\Rigging_Dojo\\Python101" in sys.path:
    pass
else:
    sys.path.append("C:\Users\Wagner\PersonalArt\Scripting\Rigging_Dojo\Python101")


import startup as startup
reload (startup)

# add RiggingDojo menu to maya menu
def create_Menu(*args):
    mayaWindow = cmds.window("MayaWindow", ma = True, q = True)
    for obj in mayaWindow:
        if obj == "RDojo_Menu":
            
            cmds.deleteUI("RDojo_Menu", m = True) # if menu exists delete it

        # create menu

    cmds.menu("RDojo_Menu", label = "Dojo", to = True, p = "MayaWindow")        
    cmds.menuItem(label = "myArm", command = "myArmCallback()")
    cmds.menuItem(label = "DojoUi", command = "myDojoUiCallback()")
        
        
create_Menu()

def myArmCallback(*args):
    import arm_rig as arm_rig
    arm_rig.UI() 
    
def myDojoUiCallback(*args):
    import dojo_ui
    reload(dojo_ui)
    
"""
Week 2 Rigging Dojo Assignment
Stephanie Wagner

I created a small UI for the arm rig. To create the arm joints
I placed four locators in the arm_rig_scene which need to be
selected to run the script. To place the joints at the locators
I used the xform command. When all joints are created I orient
the joints and clear the selection afterwards.

I added two additionally thoughts about the script in line 65 and 102 ;)

"""

import maya.cmds as cmds

# Locator
def myupperArmLOCCallback(*args):
    mySelection = cmds.ls(sl=True)
    if len(mySelection) == 0:
        # create a warning
        cmds.warning("select a locator")
    else:
        # fill in the textfield with the name of the control
        myupperArmLOCName = mySelection[0]
        cmds.select(clear=True)
        cmds.textField("upperArmLOC",e=True,en=True,tx=myupperArmLOCName)
    
def myElbowCallback(*args):
    mySelection = cmds.ls(sl=True)
    if len(mySelection) == 0:
        # create a warning
        cmds.warning("select a locator")
    else:
        # fill in the textfield with the name of the control
        myElbowLOCName = mySelection[0]
        cmds.select(clear=True)
        cmds.textField("ElbowLOC",e=True,en=True,tx=myElbowLOCName)
    
def myWristCallback(*args):
    mySelection = cmds.ls(sl=True)
    if len(mySelection) == 0:
        # create a warning
        cmds.warning("select a locator")
    else:
        # fill in the textfield with the name of the control
        myWristLOCName = mySelection[0]
        cmds.select(clear=True)
        cmds.textField("WristLOC",e=True,en=True,tx=myWristLOCName)

def myWristEndCallback(*args):
    mySelection = cmds.ls(sl=True)
    if len(mySelection) == 0:
        # create a warning
        cmds.warning("select a locator")
    else:
        # fill in the textfield with the name of the control
        myWristEndLOCName = mySelection[0]
        cmds.select(clear=True)
        cmds.textField("WristEndLOC",e=True,en=True,tx=myWristEndLOCName)
        
    
# JointChain
def myHiCallback(*args):
    """ I still need to implement a check if four locates were previously selected"""
    # Storing the selected Locators into variables
    myupperArmLOC = cmds.textField("upperArmLOC",q = True, tx = True)
    myElbowLOC = cmds.textField("ElbowLOC",q = True, tx = True)
    myWristLOC = cmds.textField("WristLOC",q = True, tx = True)
    myWristEndLOC = cmds.textField("WristEndLOC",q = True, tx = True)
    
    # Creating the joints at the Locator position
    myupperArmPOS = cmds.xform (myupperArmLOC,query=True, ws=True, t=True)
    myupperArmJNT = cmds.joint(n="upperArm_JNT", p =myupperArmPOS)    
    myElbowPOS = cmds.xform (myElbowLOC,query=True, ws=True, t=True)
    myElbowJNT = cmds.joint(n="Elbow_JNT", p =myElbowPOS)    
    myWristPOS = cmds.xform (myWristLOC,query=True, ws=True, t=True)
    myWristJNT = cmds.joint(n="Wrist_JNT", p =myWristPOS)    
    myWristEndPOS = cmds.xform (myWristEndLOC,query=True, ws=True, t=True)
    myristEndJNT = cmds.joint(n="Wrist_END", p =myWristEndPOS)
    
    # Orienting the joints (xyz)
    cmds.select(myupperArmJNT)
    myHierachy = cmds.select(hi = True)
    cmds.joint(e=True, oj='xyz', sao='yup', ch=1, zso=1)
    
    cmds.select(cl= True)
    cmds.warning("successfully created joint hierachy and xyz joint orientation")
 
    
## UI Creation

def UI():
    # window name, title and size
    if cmds.window("ArmRig", exists = True):
        cmds.deleteUI("ArmRig")
    myWindow = cmds.window("ArmRig", title = "Arm Rig UI", w = 300, h = 80, mxb = False, mnb = False, s = True)
    # buttons
    cmds.columnLayout( adjustableColumn=True )
    cmds.text(label="Create Locator", align="left", h=30, fn="boldLabelFont")
    cmds.button( label="Select upperArm Locator", command=myupperArmLOCCallback)
    """ Probably not the best way to let the user select each locater instead of all four locators at once.
    I wanted to make sure that it is clear which locators need to be created to run the script (because of roll joints etc)"""
    cmds.separator(h=5,style='none')
    cmds.textField("upperArmLOC", w = 300, en = False, text ="no selection")
    cmds.separator(h=5,style='none')
    cmds.button( label="Select Elbow Locator", command=myElbowCallback)
    cmds.textField("ElbowLOC", w = 300, en = False, text ="no selection")
    cmds.separator(h=5,style='none')
    cmds.button( label="Select Wrist Locator", command=myWristCallback)
    cmds.separator(h=5,style='none')
    cmds.textField("WristLOC", w = 300, en = False, text ="no selection")
    cmds.separator(h=5,style='none')
    cmds.button( label="Select Wrist End Locator", command=myWristEndCallback)
    cmds.separator(h=5,style='none')
    cmds.textField("WristEndLOC", w = 300, en = False, text ="no selection")
    cmds.separator(h=15,style='none')
    cmds.button( label="Create and orient joint hierachy", h = 30, en = True, command=myHiCallback)

    cmds.showWindow()

UI()
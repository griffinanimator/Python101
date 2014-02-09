"""
Arm Rig Setup
Stephanie Wagner

progress:
    - basic UI (week02)
    - Create, orient and rename joints from given locators (week02)
    - created a dictionary to assign names and positions to joints from given locators (week03 - line 64 - 86)

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
    
    locator_info_dictionary = {}
    
    # Storing the selected Locators into variables
    myupperArmLOC = cmds.textField("upperArmLOC",q = True, tx = True)
    myElbowLOC = cmds.textField("ElbowLOC",q = True, tx = True)
    myWristLOC = cmds.textField("WristLOC",q = True, tx = True)
    myWristEndLOC = cmds.textField("WristEndLOC",q = True, tx = True)
   
    # Getting the positions of the locators
    myupperArmPOS = cmds.xform (myupperArmLOC,query=True, ws=True, t=True)  
    myElbowPOS = cmds.xform (myElbowLOC,query=True, ws=True, t=True) 
    myWristPOS = cmds.xform (myWristLOC,query=True, ws=True, t=True) 
    myWristEndPOS = cmds.xform (myWristEndLOC,query=True, ws=True, t=True)
    
    # fill in dictionary
    locator_info = (["L_upperArm", myupperArmPOS],["L_Elbow", myElbowPOS],["L_Wrist", myWristPOS],["L_WristEnd", myWristEndPOS])
    locator_info_dictionary["MyNames"]=[locator_info[name][0]for name in range(len(locator_info))]
    locator_info_dictionary["MyPosition"]=[locator_info[position][1]for position in range(len(locator_info))]
    
    # Joint creation
    for name, position in locator_info:
       cmds.joint(name = name + ("_JNT"), p = position)
       print ("This is " + name +"_JNT at position"), position      

    # Orienting the joints (xyz)
    cmds.select("L_upperArm_JNT")
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
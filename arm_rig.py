"""
Arm Rig Setup
Stephanie Wagner

progress:
    - basic UI (week02)
    - Create, orient and rename joints from given locators (week02)
    - created a dictionary to assign names and positions to joints from given locators (week03)
    - using a loop and a function to get the locators(week04)
    - FK IK joints and controlrig creation (week04)
    - FK IK blending (week04)

to do:
    - correctly place polevector
    - update controlcurves (set drawing override, lock attributes, delete non-deformer history,update shapes)
    - use variables and loops to connect the fkik switch
    - stretchy IK
    - cleanup scene, store everything to groups

"""

import maya.cmds as cmds
import pymel.core as pm


def lOCCallback(loc, *args):
    
    mySelection = cmds.ls(sl=True)
    if len(mySelection) == 0:
        # create a warning
        cmds.warning("select a locator")
    else:
        # fill in the textfield with the name of the control
        myLOCName = mySelection[0]
        cmds.select(clear=True)
        cmds.textField(loc[1], e=True,en=True,tx=myLOCName)

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
    listofJoints = []
    for name, position in locator_info:
       myJoint = cmds.joint(name = name + ("_JNT"), p = position)
       listofJoints.append(myJoint)
       #print ("This is " + name +"_JNT at position"), position      
    
    # Orienting the joints (xyz)
    cmds.select(listofJoints[0])
    cmds.select(hi = True)
    cmds.joint(e=True, oj='xyz', sao='yup', ch=1, zso=1)
    cmds.delete(listofJoints[3])

    # Duplicating and renaming the jointchain  
    myNames = ("L_upperArm", "L_Elbow", "L_Wrist")
    myFKJoints = cmds.duplicate(listofJoints[0], rc = True)
    for fk in myFKJoints:
         cmds.rename(fk, fk.replace("_JNT1", "_FK"))
         myFKJoints[myFKJoints.index(fk)] = fk.replace("_JNT1", "_FK")
    
    myIKJoints = cmds.duplicate(listofJoints[0], rc = True)
    for ik in myIKJoints:
         cmds.rename(ik, ik.replace("_JNT1", "_IK"))
         myIKJoints[myIKJoints.index(ik)] = ik.replace("_JNT1", "_IK")

    """ FK CON"""
    cmds.select(clear = True) 
    myNames = ("L_upperArm", "L_Elbow", "L_Wrist")
    # create FK null and con
    listFKNull= []
    for nullname in myNames:
       myNull = cmds.group(n = nullname +("_FK_CON_GRP"), em = True)
       listFKNull.append(myNull)

    listFKCtrl = []
    for ctrlName in myNames:
        myFKCurve = cmds.circle(n = ctrlName +("_FK_CON"), r = .2, nr = (1,0,0))
        listFKCtrl.append(myFKCurve)
    # parent the control under the null group
    for i in range(len(listFKCtrl)):
        cmds.parent(listFKCtrl[i], listFKNull[i])
    
    # place null group at joint
    for i in range(len(listFKNull)):
        tempCons = cmds.parentConstraint(myFKJoints[i], listFKNull[i], mo = False)
        cmds.delete(tempCons)
        
    # parentconstrain control and joint
    for i in range(len(myFKJoints)):
        cmds.orientConstraint(listFKCtrl[i], myFKJoints[i], mo = False)
        
    # hierachy creation      
    cmds.parent(listFKNull[1],listFKCtrl[0])
    cmds.parent(listFKNull[2],listFKCtrl[1])
    
    """ IK CON """
    # create IKHandle
    myIK = cmds.ikHandle(sj=myIKJoints[0], ee = myIKJoints[2], n = "L_Arm_IKRP", sol = "ikRPsolver")

    # create IK con and null
    myIKWristnull = cmds.group(n = myNames[2]+"_IK_CON_GRP", em = True)
    myIKWristcon = cmds.circle(n = myNames[2]+"IK_CON", r = 0.3, nr = (1,0,0))
    cmds.parent(myIKWristcon, myIKWristnull)
    
    myIKElbownull = cmds.group(n = myNames[1]+"_IK_CON_GRP", em = True)
    myIKElbowcon = cmds.circle(n = myNames[1]+"IK_CON", r = 0.3, nr = (1,0,0))
    cmds.parent(myIKElbowcon, myIKElbownull)    
    
    # place null group at joint    
    myTempCons =  cmds.pointConstraint(myIKJoints[1], myIKElbownull, mo = False)
    cmds.delete(myTempCons)
    myTempCons =  cmds.parentConstraint(myIKJoints[2], myIKWristnull, mo = False)
    cmds.delete(myTempCons)   
    
    # set constraints
    cmds.pointConstraint(myIKWristcon, myIK[0], mo = False)
    cmds.poleVectorConstraint(myIKElbowcon, myIK[0] )
    cmds.orientConstraint(myIKWristcon,myIKJoints[2], mo = False )
    
    """ Create FKIK Switch"""
    # create constraints
    listmyConstraint = []
    for i in range(len(myFKJoints)):
        myConstraint = cmds.parentConstraint(myFKJoints[i], myIKJoints[i], listofJoints[i], mo = False) 
        listmyConstraint.append(myConstraint)
    print listmyConstraint
    
    # create control
    myFKIKnull = cmds.group(n = "L_Arm_FKIK_CON_GRP", em = True)
    myFKIKcon = cmds.circle(n = "L_Arm_FKIK_CON", r = 0.5, nr = (1,0,0))
    cmds.addAttr(k = True, ln = "FK_to_IK", attributeType = "float", minValue = 0, maxValue = 1)
    cmds.parent(myFKIKcon, myFKIKnull)       
    cmds.parentConstraint(listofJoints[2], myFKIKnull, mo = False)
    
    # connect control
    
    cmds.connectAttr("L_Arm_FKIK_CON.FK_to_IK" , "L_upperArm_JNT_parentConstraint1.L_upperArm_IKW1")
    cmds.connectAttr("L_Arm_FKIK_CON.FK_to_IK" , "L_Elbow_JNT_parentConstraint1.L_Elbow_IKW1")
    cmds.connectAttr("L_Arm_FKIK_CON.FK_to_IK" , "L_Wrist_JNT_parentConstraint1.L_Wrist_IKW1")
    cmds.connectAttr("L_Arm_FKIK_CON.FK_to_IK","L_Wrist_IK_CON_GRP.visibility")
    cmds.connectAttr(" L_Arm_FKIK_CON.FK_to_IK","L_Elbow_IK_CON_GRP.visibility")
    cmds.createNode("reverse", n = "L_Arm_Reverse")    
    cmds.connectAttr("L_Arm_FKIK_CON.FK_to_IK" , "L_Arm_Reverse.input.inputX")
    cmds.connectAttr("L_Arm_Reverse.output.outputX ","L_upperArm_JNT_parentConstraint1.L_upperArm_FKW0")
    cmds.connectAttr("L_Arm_Reverse.output.outputX ","L_Elbow_JNT_parentConstraint1.L_Elbow_FKW0")
    cmds.connectAttr("L_Arm_Reverse.output.outputX ","L_Wrist_JNT_parentConstraint1.L_Wrist_FKW0")
    cmds.connectAttr("L_Arm_Reverse.output.outputX","L_upperArm_FK_CON_GRP.visibility" )
    
"""Create UI"""
def UI():
    # window name, title and size
    if cmds.window("ArmRig", exists = True):
        cmds.deleteUI("ArmRig")
    myWindow = cmds.window("ArmRig", title = "Arm Rig UI", w = 300, h = 80, mxb = False, mnb = False, s = True)
    # buttonlists
    labelList = ("Select upperArm Locator", "Select Elbow Locator", "Select Wrist Locator", "Select Wrist End Locator")
    textList = ("upperArmLOC", "ElbowLOC", "WristLOC", "WristEndLOC")
    # button creation 
    cmds.columnLayout( adjustableColumn=True )
    cmds.text(label="Create four Locator and select them", align="left", h=30, fn="boldLabelFont")     
    for l in range(len(labelList)):
        cmds.separator(h=5,style='none')
        pm.button( label=labelList[l], command = pm.Callback(lOCCallback, [labelList[l], textList[l]] ))
        cmds.separator(h=5,style='none')
        cmds.textField(textList[l], w = 300, en = False, text ="no selection")
    cmds.separator(h=15,style='none')
    cmds.button( label="Create and orient joint hierachy", h = 30, en = True, command=myHiCallback)     
    cmds.showWindow()
 
#UI() 
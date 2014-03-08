# trArmRig.py
import maya.cmds as mc
import data.jsonUtils as jsonUtils
import json
import utils.rig_utils as rig_utils

class ArmRig:
    ''' Class that creates Arm Rig'''

    def __init__(self,*args):
        # Create dictionaries
        armData = {}


    def install(self,*args):
        # Load arm data dictionary from Json
        jsonPath="D:/Users/Toby/Documents/GitHub/Python101/data/locator_info.json"
        armData=jsonUtils.readJson(jsonPath)
        armData=json.loads(armData)

        # Create drive skeleton
        jointNames=armData["armJointNames"]
        jointPositions=armData["armJointPositions"]

        rig_utils.createJoints(jointNames,jointPositions)

        # Create IK joints
        ikJointNames=armData["IKJointNames"]
        rig_utils.createJoints(ikJointNames,jointPositions)

        # Create FK joints
        fkJointNames=armData["FKJointNames"]
        rig_utils.createJoints(fkJointNames,jointPositions)

        # Constrain drive skeleton to IK and FK joints, set default constraint weight
        armData["driveConstraints"]=rig_utils.constrainJoints(jointNames,ikJointNames,fkJointNames)

        # Create RPIK on IK joints
        ikHandlePosition=armData["armIkHandle"]
        IKHandleName="ikHandle_arm_L"
        rig_utils.rpIKHandle(IKHandleName,ikHandlePosition)

        # Create Pole Vector Control
        poleVectorPosition = rig_utils.poleVectorPosition(ikHandlePosition)
        name="PVarm"
        rig_utils.createController(poleVectorPosition,name)

        # Create IK control, point contrain to ikhandle (set orientation to world not local to hand)
        ikControl=armData["ikJointNames"][2]
        ikControlName="IKHand"
        rig_utils.createController(ikControl,ikControlName)
        mc.pointConstraint()


        # Create FK controls, orient constrain to fk bones
        fkControls = armData["FKControlNames"]
        for i in range(len(fkJointNames)):
            fkControl = rig_utils.createController(jointPositions,fkControls)
            oc=mc.orientConstrain(fkJointNames[i],fkControl)
            mc.delete(oc)
            fkOC = mc.orientConstrain(fkControl,fkJointNames[i])
            mc.select(clear=True)

        # Create switch controller, follow drive hand joint, add switch attribute
        switchControlName ="HandSwitch"
        handSwitchPos = armData["armJointPositions"][2]
        switchControl=rig_utils.createController(handSwitchPos,switchControlName)
        mc.parentContraint(jointNames[2],switchControl[0])
        switchAttr=mc.addAttr(shortName="IKFKSwitch",longName="IK_FK_Switch",attributeType="enum",enumName="IK:FK:")
        mc.setAttr(switchAttr, edit=True, keyable=True)
        switchAttr="ctrl_ArmSwitches.IKFKSwitch"
        mc.select(clear=True)

        # create reverse nodes
        reverseNodeNames=[armData["reverseNodes"]]
        for i in range(len(jointNames)):
            mc.shadingNode(reverse,name=reverseNodeNames[i],asUtility=True)

        # connect IKFK switch attribute and reverse nodes to parent constraints

        mc.connectAttr(switchAttr ,"{parentConstraint}.{IK} W0".format(parentConstraint=rmData["driveConstraints"][0],IK=armData["ikJointNames"][0]) )
        mc.connectAttr(switchAttr , "{reverseNode}.inputX".format(reverseNode=armData["reverseNodes"][0]))
        mc.connectAttr("{reverseNode}.outputX".format(reverseNode=armData["reverseNodes"][0]),"{parentConstraint}.{FK} W0".format(parentConstraint=rmData["driveConstraints"][0],FK=armData["fkJointNames"][0]))

        mc.connectAttr(switchAttr ,"{parentConstraint}.{IK} W0".format(parentConstraint=rmData["driveConstraints"][1],IK=armData["ikJointNames"][1]) )
        mc.connectAttr(switchAttr , "{reverseNode}.inputX".format(reverseNode=armData["reverseNodes"][1]))
        mc.connectAttr("{reverseNode}.outputX".format(reverseNode=armData["reverseNodes"][1]),"{parentConstraint}.{FK} W0".format(parentConstraint=rmData["driveConstraints"][1],FK=armData["fkJointNames"][1]))

        mc.connectAttr(switchAttr ,"{parentConstraint}.{IK} W0".format(parentConstraint=rmData["driveConstraints"][2],IK=armData["ikJointNames"][2]))
        mc.connectAttr(switchAttr , "{reverseNode}.inputX".format(reverseNode=armData["reverseNodes"][2]))
        mc.connectAttr("{reverseNode}.outputX".format(reverseNode=armData["reverseNodes"][2]),"{parentConstraint}.{FK} W0".format(parentConstraint=rmData["driveConstraints"][2],FK=armData["fkJointNames"][2]))

        # connect IKFK switch to joint visibilty, and controller visibility
        for i in range(len(fkJointNames)):
            mc.connectAttr(switchAttr , "{FK}.visibility".format(FK=armData["FKJointNames"][i]))

        for i in range(len(ikJointNames)):
            mc.connectAttr("{reverseNode}.outputX".format(reverseNode=armData[reverseNodeNames][0]), "{IK}.visibility".format(IK=armData["ikJointNames"][i]))

arm =ArmRig()
arm.install()

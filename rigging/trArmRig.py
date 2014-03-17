# trArmRig.py
import maya.cmds as mc
import data.jsonUtils as jsonUtils
import json
import utils.rig_utils as rig_utils


TITLE = "ArmRig"
class ArmRig:
    ''' Class that creates Arm Rig'''

    def __init__(self,*args):
        # Create dictionaries
        self.armData = {}


    def install(self,*args):
        # Load arm data dictionary from Json
        jsonPath="D:/Users/Toby/Documents/GitHub/Python101/data/locator_info.json"
        self.armData=jsonUtils.readJson(jsonPath)
        self.armData=json.loads(self.armData)

        # Create drive skeleton
        jointNames=self.armData["armJointNames"]
        jointPositions=self.armData["armJointPositions"]

        rig_utils.createJoints(jointNames,jointPositions)

        # Create IK joints
        ikJointNames=self.armData["IKJointNames"]
        rig_utils.createJoints(ikJointNames,jointPositions)

        # Create FK joints
        fkJointNames=self.armData["FKJointNames"]
        rig_utils.createJoints(fkJointNames,jointPositions)

        # Constrain drive skeleton to IK and FK joints, set default constraint weight
        self.armData["driveConstraints"]=rig_utils.constrainJoints(jointNames,ikJointNames,fkJointNames)
        print(self.armData["driveConstraints"])
        # Create RPIK on IK joints
        ikHandlePosition=self.armData["armIkHandle"]
        IKHandleName="ikHandle_arm"
        rig_utils.rpIKHandle(IKHandleName,ikHandlePosition)

        # Create Pole Vector Control
        poleVectorPosition = rig_utils.poleVectorPosition(ikHandlePosition)
        name="PVarm"
        pvControl = rig_utils.createController(poleVectorPosition,name)
        mc.poleVectorConstraint(pvControl[0],IKHandleName)

        # Create IK control, point contrain to ikhandle (set orientation to world not local to hand)
        ikControl=self.armData["armJointPositions"][2]
        print(ikControl)
        ikControlName="IKHand"
        ikHandControl = rig_utils.createController(ikControl,ikControlName)
        mc.pointConstraint(ikHandControl[0],IKHandleName)
        mc.select(clear=True)

        # Create FK controls, orient constrain to fk bones
        fkControls = self.armData["FKControlNames"]
        for i in range(len(fkJointNames)):
            fkControl = rig_utils.createController(jointPositions[i],fkControls[i])
            oc=mc.orientConstraint(fkJointNames[i],fkControl[1])
            mc.delete(oc)
            fkOC = mc.orientConstraint(fkControl[0],fkJointNames[i])
            mc.select(clear=True)
        # Create hierarchy of FK controllers

        # Create switch controller, follow drive hand joint, add switch attribute
        switchControlName ="HandSwitch"
        handSwitchPos = self.armData["armJointPositions"][2]
        switchControl=rig_utils.createController(handSwitchPos,switchControlName)
        mc.parentConstraint(jointNames[2],switchControl[1])
        mc.addAttr(shortName="IKFKSwitch",longName="IK_FK_Switch",attributeType="enum",enumName="IK:FK:")
        switchAttr="ct_HandSwitch.IKFKSwitch"
        mc.setAttr(switchAttr, edit=True, keyable=True)
        mc.select(clear=True)

        # create reverse nodes
        reverseNodeNames=self.armData["reverseNodes"]
        for i in range(len(jointNames)):
            mc.shadingNode("reverse",name=reverseNodeNames[i],asUtility=True)

        # connect IKFK switch attribute and reverse nodes to parent constraints
        self.armData["constraintWeightAttributes"]=mc.parentConstraint(self.armData["driveConstraints"][0],query =True,weightAliasList=True)
        print(self.armData["constraintWeightAttributes"])

        mc.connectAttr(switchAttr ,"{parentConstraint}.{IK}W0".format(parentConstraint=self.armData["driveConstraints"][0],IK=self.armData["IKJointNames"][0]) )
        mc.connectAttr(switchAttr , "{reverseNode}.inputX".format(reverseNode=self.armData["reverseNodes"][0]))
        mc.connectAttr("{reverseNode}.outputX".format(reverseNode=self.armData["reverseNodes"][0]),"{parentConstraint}.{FK}W1".format(parentConstraint=self.armData["driveConstraints"][0],FK=self.armData["FKJointNames"][0]))

        mc.connectAttr(switchAttr ,"{parentConstraint}.{IK}W0".format(parentConstraint=self.armData["driveConstraints"][1],IK=self.armData["IKJointNames"][1]) )
        mc.connectAttr(switchAttr , "{reverseNode}.inputX".format(reverseNode=self.armData["reverseNodes"][1]))
        mc.connectAttr("{reverseNode}.outputX".format(reverseNode=self.armData["reverseNodes"][1]),"{parentConstraint}.{FK}W1".format(parentConstraint=self.armData["driveConstraints"][1],FK=self.armData["FKJointNames"][1]))

        mc.connectAttr(switchAttr ,"{parentConstraint}.{IK}W0".format(parentConstraint=self.armData["driveConstraints"][2],IK=self.armData["IKJointNames"][2]))
        mc.connectAttr(switchAttr , "{reverseNode}.inputX".format(reverseNode=self.armData["reverseNodes"][2]))
        mc.connectAttr("{reverseNode}.outputX".format(reverseNode=self.armData["reverseNodes"][2]),"{parentConstraint}.{FK}W1".format(parentConstraint=self.armData["driveConstraints"][2],FK=self.armData["FKJointNames"][2]))

        # connect IKFK switch to joint visibilty, and controller visibility
        for i in range(len(fkJointNames)):
            mc.connectAttr(switchAttr , "{FK}.visibility".format(FK=self.armData["FKJointNames"][i]))

        reverseNode=self.armData["reverseNodes"][0]
        print(reverseNode)
        for i in range(len(ikJointNames)):
            mc.connectAttr("{reverseNode}.outputX".format(reverseNode=reverseNode), "{IK}.visibility".format(IK=self.armData["IKJointNames"][i]))


    def layout(self,*args):
        # Create joints from dictionary in default position

        # Create layout joint controls


arm =ArmRig()
arm.install()

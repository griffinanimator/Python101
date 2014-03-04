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
        rig_utils.constrainJoints(jointNames,ikJointNames,fkJointNames)

        # Create RPIK on IK joints
        ikHandlePosition=armData["armIkHandle"]
        IKHandleName="ikHandle_arm_L"
        rig_utils.rpIKHandle(IKHandleName,ikHandlePosition)

        # Create Pole Vector Control
        poleVectorPosition = rig_utils.poleVectorPosition(ikHandlePosition)
        name="PVarm"
        rig_utils.createController(poleVectorPosition,name)

        # Create IK control, point contrain to ikhandle (set orientation to world not local to hand)

        rig_utils.createController(position,name)

        # Create FK controls, orient constrain to fk bones

        for i in range(len(fkJointNames)):
            fkControl = rig_utils.createController(position,name)
            oc=mc.pointConstrain(fkJointNames[i],fkControl)
            mc.delete(oc)
            mc.select(clear=True)

        # Create switch controller, follow drive hand joint, add switch attribute
        name ="HandSwitch"
        switchControl=rig_utils.createController(position,name)
        mc.parentContraint(jointNames[2],switchControl[0])
        switchAttr=mc.addAttr(shortName="IKFKSwitch",longName="IK_FK_Switch",attributeType="enum",enumName="IK:FK:")
        mc.setAttr(switchAttr, edit=True, keyable=True)

        # create reverse nodes
        reverseNodeNames=[]
        for i in range(len(jointNames)):
            mc.shadingNode(name=reverseNodeNames[i],asUtility=True, reverse)

        # connect IKFK switch attribute and reverse nodes to parent constraints

        # connect IKFK switch to joint visibilty, and controller visibility








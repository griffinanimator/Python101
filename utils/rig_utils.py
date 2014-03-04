import maya.cmds as mc
import json
import utils.jsonUtils as jsonUtils
import maya.OpenMaya as om


jsonPath="D:/Users/Toby/Documents/GitHub/Python101/data/locator_info.json"
armData=jsonUtils.readJson(jsonPath)
armData=json.loads(armData)


def createJoints(*args):
    for i in range(len(jointNames)):
        # replace ljnt prefix with the correct prefix
        #jointName = jointNames[i].replace("ljnt","jnt")
        # create joint chain
        mc.joint(name="{jointNames}".format(jointNames=jointNames[i]),
            position=jointPositions[i])
    mc.select(clear=True)

jointNames=armData["armJointNames"]
jointPositions=armData["armJointPositions"]
suffix="L"

createJoints(jointNames,jointPositions)

jointNames=armData["IKJointNames"]
createJoints(jointNames,jointPositions)

jointNames=armData["FKJointNames"]
createJoints(jointNames,jointPositions)

jointNames=armData["armJointNames"]
IKJointNames=armData["IKJointNames"]
FKJointNames=armData["FKJointNames"]

def constrainJoints(*args):
    for i in range(len(jointNames)):
        # Parent constrain drive bones to IK and FK arm chains
        pc = mc.parentConstraint(IKJointNames[i],FKJointNames[i],jointNames[i], mo =True)

        # Edit constraint weight to IK by default
        mc.setAttr("{pc}.{FKJointNames}W1".format(pc=pc[0],FKJointNames=FKJointNames[i]),0)

constrainJoints(jointNames,IKJointNames,FKJointNames)

def poleVectorPosition(*args):
    for joint in ikJoints:
        position = mc.xform(joint, query = True, translation = True, worldSpace = True)
        jointPosition.append(position)

    position = mc.listRelatives(selection[1], parent = True)
    position = mc.xform(position, query = True, translation = True, worldSpace = True)
    jointPosition.append(position)

    # Determine position of Pole Vector Control
    A = om.MVector(jointPosition[0][0],jointPosition[0][1],jointPosition[0][2])
    B = om.MVector(jointPosition[1][0],jointPosition[1][1],jointPosition[1][2])
    C = om.MVector(jointPosition[2][0],jointPosition[2][1],jointPosition[2][2])

    D = B -A
    E = A + (D * 0.5)
    F = C - E
    G = C + (F * 2)

    PVPosition = [G[0], G[1], G[2]]

    return PVPosition
ikJoints=armData["armIkHandle"]


ikHandlePosition=armData["armIkHandle"]
def rpIKHandle(*args):
    mc.ikHandle(name=IKHandleName,startJoint=ikHandlePosition[0],endEffector=ikHandlePosition[1], solver="ikRPsolver")

IKHandleName="ikHandle_arm_L"
rpIKHandle(ikHandlePosition)


def createController(*args):
    # Create control group and transform group
    controlGroup=mc.group(name="ct_{name}".format(name=name),em=True,w=True)
    transformGroup=mc.group(name="grp_{name}".format(name=name),em=True,w=True)
    mc.parent(controlGroup,transformGroup)
    # Position transform group at location
    mc.xform(transformGroup,worldSpace=True,t=(jointPositions[0],jointPositions[1],jointPositions[2]))

name="IKHand"
jointPositions=armData["armJointPositions"][2]
createController(jointPositions,name)
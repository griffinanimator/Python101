import maya.cmds as mc
import json
import tempfile

arm_info={}
locatorTransforms=[]
locatorPositions=[]
layoutJntInfo=[]

# List locators in scene
locators=mc.ls(type="locator")

# Find transform nodes of locators
for locator in locators:
    transformNode=mc.listRelatives(locator,parent=True,type="transform")[0]
    locatorTransforms.append(transformNode)

# Find locator position
for transform in locatorTransforms:
    pos=mc.xform(transform,query=True, worldSpace=True,translation=True)
    locatorPositions.append(pos)

# Combine position and name lists
# Populate layoutJntInfo with information
for i in range(len(locatorTransforms)):
    temp="{transformName}".format(transformName=locatorTransforms[i]),locatorPositions[i]
    layoutJntInfo.append(temp)
# Delete locators
#mc.delete(locatorTransforms)

jsonPath="D:/Users/Toby/Documents/GitHub/Python101/data/locator_info.json"
def writeJson(fileName, data):
    with open(fileName,"w") as outfile:
        json.dump(data,outfile)

    file.close(outfile)

writeJson(jsonPath,layoutJntInfo)

def readJson(fileName):
    with open(fileName,"r") as infile:
        data=(open(infile.name,"r").read())
    return data

# Build joints
# Create empty list to store information
ljntList = []

for jnt in layoutJntInfo:
    # Create joint based off layout joint info
    layoutJnt=mc.joint(name=jnt[0],position=jnt[1])
    # Append joint to layout list
    ljntList.append(layoutJnt)

arm_info["ljntInfo"]=layoutJntInfo

def createJoints():
    pass

jntInfo = []
mc.select(d=True)
for ljnt in arm_info["ljntInfo"]:
    # Replace ljnt string with jnt
    jntName=ljnt[0].replace("ljnt","jnt")
    jntPos=mc.xform(ljnt[0],q=True,worldSpace=True,t=True)
    mc.joint(name=jntName,position=jntPos)
    jntInfo.append(jntName)
arm_info["JntInfo"]=jntInfo

# Draw Ik Handle
ikh = mc.ikHandle(n="rpIK_l_arm01",solver="ikRPsolver",
    startJoint=arm_info["JntInfo"][0],endEffector=arm_info["JntInfo"][2])
arm_info["IKH"]=ikh

def createController(objectName="",position=[],name=""):
    '''
    Creates a controller group and a transform group at location
    Takes either an object name or position as argument.
    '''
    # Validate arguments
    # If object name and position aren't given raise error
    if len(objectName)==0 and len(position) is not 3:
        raise RuntimeError("You have not specified an object or position at which to create controller")
    # If object name is not given store position as position, else query object names position
    if len(objectName) == 0:
        position=position
    else:
        position=mc.xform(objectName,query=True,worldSpace=True,t=True)

    # Create control group and transform group
    controlGroup=mc.group(name="ctrl_{name}".format(name=name),em=True,w=True)
    transformGroup=mc.group(name="ORT_{name}".format(name=name),em=True,w=True)
    mc.parent(controlGroup,transformGroup)
    # Position transform group at location
    mc.xform(transformGroup,worldSpace=True,t=(position[0],position[1],position[2]))

    # if OrientConstraint:
        #mc.orientConstraint(controlGroup,objectName)
    # if PointConstrain:
        #mc.pointConstraint(controlGroup,objectName)

# Create pole vector control.
#createController(position=poleVectorPosition(arm_info["JntInfo"][0],arm_info["JntInfo"][2])
# Create a control transform function

# Delete Layout Joints
#mc.select(arm_info["ljntInfo"])
#mc.delete()
# Clean scene of empty transforms

createController("ljnt_wrist",name="wrist_L")
mc.pointConstraint("ctrl_wrist_L","rpIK_l_arm01")
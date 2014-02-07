import maya.cmds as mc

arm_info={}

# Layout joint list
# Experiment with populating this from selection
layoutJntInfo=(["ljnt_shoulderA",[0.0,0.0,2.0]],["ljnt_elbowA",[0.0,2.0,5.0]],["ljnt_wristA",[0.0,0.0,8.0]])

# Build joints
# Create empty list to store information
ljntList = []

for jnt in layoutJntInfo:
    # Create joint based off layout joint info
    layoutJnt=mc.joint(name=jnt[0],position=jnt[1])
    # Append joint to layout list
    ljntList.append(layoutJnt)#
print(ljntList)

arm_info["ljntInfo"]=ljntList

jntInfo = []
mc.select(d=True)
for ljnt in arm_info["ljntInfo"]:
    # Replace ljnt string with jnt
    jntName = ljnt.replace("ljnt","jnt")
    jntPos =mc.xform(ljnt,q=True,worldSpace=True,t=True)
    mc.joint(name=jntName,position=jntPos)
    jntInfo.append(jntName)
arm_info["JntInfo"]=jntInfo

# Draw Ik Handle
ikh = mc.ikHandle(n="rpIK_l_arm01",solver="ikRPsolver",
    startJoint=arm_info["JntInfo"][0],endEffector=arm_info["JntInfo"][2])
arm_info["IKH"]=ikh

#------------------------------------------------------------------------------------------
# Parent IK handle to the control
# Find location of ikhandle
ikPos=mc.xform(ikh[0],query=True,worldSpace=True,t=True)
# Create an empty group to act as the controller, parent this to another null to store its
# Transform and rotation values and keep the controller zeroed.
ikControl=mc.group(name="ctrl_arm_L",em=True,w=True)
ikTransform=mc.group(name="ORT_ikArm_L",em=True,w=True)
mc.parent(ikControl,ikTransform)
# Parent IK handle to the controller
mc.xform(ikTransform,worldSpace=True,t=(ikPos[0],ikPos[1],ikPos[2]))
mc.parent(ikh[0],ikControl)
#------------------------------------------------------------------------------------------

# Rewrite controller group creation as a function
def createController(objectName="",position=[]):
    '''
    Creates a controller group and a transform group at location
    Takes either an object name or position as argument.
    '''
    # Validate arguments
    # If object name and position aren't given raise error
    if len(objectName)==0 and len(position) is not 3:
        raise RuntimeError "You have not specified an object or position at which to create controller"
    # If object name is not given store position as position, else query object names position
    if len(objectName) == 0:
        position=position
    else:
        position=mc.xform(objectName,worldSpace=True,t=True)

    # Create control group and transform group
    controlGroup=mc.group(name="ctrl_arm_L",em=True,w=True)
    transformGroup=mc.group(name="ORT_ikArm_L",em=True,w=True)
    mc.parent(controlGroup,transformGroup)
    # Position transform group at location
    mc.xform(transformGroup,worldSpace=True,t=(position[0],position[1],position[2]))

    # if OrientConstraint:
        #mc.orientConstraint(controlGroup,objectName)
    # if PointConstrain:
        #mc.pointConstraint(controlGroup,objectName)

# Create pole vector control.

# Create a control transform function

# Delete Layout Joints

# Clean scene of empty transforms
mc.select(arm_info["ljntInfo"])
mc.delete()

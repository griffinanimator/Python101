import maya.cmds as mc

#Creation of controllers

### Arm

mc.select (clear=True)
mc.circle (name='hp_l_arm', center = [0,0,0], normal= [0,1,0], sweep=360, radius=2, degree=3, sections=8, constructionHistory=1)
mc.group (name='hp_l_arm_grp', world=True, empty=True)
mc.group (name='hp_l_arm_Xtransf', world=True, empty=True)
mc.parent ('hp_l_arm_grp', 'hp_l_arm_Xtransf')
mc.parent ('hp_l_arm','hp_l_arm_grp')

mc.rotate ('-90deg',0,0,'hp_l_arm_Xtransf', relative=True,)
mc.move (0,19,0,'hp_l_arm_Xtransf', absolute=True,)
mc.setAttr ('hp_l_arm.overrideEnabled', 1)
mc.setAttr ('hp_l_arm.ove', lock=1)
mc.setAttr ('hp_l_arm.overrideColor', 6)

### Elbow

mc.select (clear=True)
mc.circle (name='hp_l_elbow', center = [0,0,0], normal= [0,1,0], sweep=360, radius=2, degree=3, sections=8, constructionHistory=1)
mc.group (name='hp_l_elbow_grp', world=True, empty=True)
mc.group (name='hp_l_elbow_Xtransf', world=True, empty=True)
mc.parent ('hp_l_elbow_grp', 'hp_l_elbow_Xtransf')
mc.parent ('hp_l_elbow','hp_l_elbow_grp')

mc.rotate ('-90deg',0,0,'hp_l_elbow_Xtransf', relative=True,)
mc.move (12,19,-3,'hp_l_elbow_Xtransf', absolute=True,)
mc.setAttr ('hp_l_elbow.overrideEnabled', 1)
mc.setAttr ('hp_l_elbow.ove', lock=1)
mc.setAttr ('hp_l_elbow.overrideColor', 13)

### Hand

mc.select (clear=True)
mc.circle (name='hp_l_hand', center = [0,0,0], normal= [0,1,0], sweep=360, radius=2, degree=3, sections=8, constructionHistory=1)
mc.group (name='hp_l_hand_grp', world=True, empty=True)
mc.group (name='hp_l_hand_Xtransf', world=True, empty=True)
mc.parent ('hp_l_hand_grp', 'hp_l_hand_Xtransf')
mc.parent ('hp_l_hand','hp_l_hand_grp')

mc.rotate ('-90deg',0,0,'hp_l_hand_Xtransf', relative=True,)
mc.move (24,19,0,'hp_l_hand_Xtransf', absolute=True,)
mc.setAttr ('hp_l_hand.overrideEnabled', 1)
mc.setAttr ('hp_l_hand.ove', lock=1)
mc.setAttr ('hp_l_hand.overrideColor', 17)

#Groups for helpers
mc.select (clear=True)
mc.group (name='Helpers', empty=True) 
mc.parent ('hp_l_arm_Xtransf', 'Helpers')
mc.parent ('hp_l_elbow_Xtransf', 'hp_l_arm')
mc.parent ('hp_l_hand_Xtransf', 'hp_l_elbow')

#Creation of joints

armJoint= mc.xform ('hp_l_arm', query=True, worldSpace=True, translation=True)
elbowJoint= mc.xform ('hp_l_elbow', query=True, worldSpace=True, translation=True)
handJoint= mc.xform ('hp_l_hand', query=True, worldSpace=True, translation=True)

mc.select (clear=True)
mc.joint (name='armJoint', position=armJoint, radius=2)
mc.select (clear=True)
mc.joint (name='elbowJoint', position=elbowJoint, radius=2)
mc.select (clear=True)
mc.joint (name='handJoint', position=handJoint, radius=2)

#Parenting joints
mc.parent ('handJoint','elbowJoint')
mc.parent ('elbowJoint','armJoint')
mc.select (clear=True)

#Orientation of joints
mc.select (clear=True)
mc.joint (exists='armJoint', orientJoint='xyz', secondaryAxisOrient='yup', children=True, zeroScaleOrient=True)

#Creation of two chains for IK/FK
#IK
mc.duplicate ('armJoint', renameChildren=True)
mc.rename ('armJoint1', 'armJointIK')
mc.rename ('elbowJoint1', 'elbowJointIK')
mc.rename ('handJoint1', 'handJointIK')

#FK
mc.duplicate ('armJoint', renameChildren=True)
mc.rename ('armJoint1', 'armJointFK')
mc.rename ('elbowJoint1', 'elbowJointFK')
mc.rename ('handJoint1', 'handJointFK')

#Creating groups
jointsGroups = ('JointChain', 'IKJoints', 'FKJoints', 'ArmRig')
for items in jointsGroups:
    mc.group (name=items, empty=True, world=True)
    
mc.parent ('armJointFK', 'FKJoints')
mc.parent ('armJointIK', 'IKJoints')
mc.parent ('armJoint', 'JointChain')

grpsToParent = ('JointChain','IKJoints','FKJoints')
for items in grpsToParent:
    mc.parent (items, 'ArmRig')
    
#Creation of nodes for IK FK Switch
mc.shadingNode ('blendColors', asUtility=True, name='blendNode_arm_rotate')
mc.shadingNode ('blendColors', asUtility=True, name='blendNode_elbow_rotate')
mc.shadingNode ('blendColors', asUtility=True, name='blendNode_hand_rotate')

mc.shadingNode ('blendColors', asUtility=True, name='blendNode_arm_translate')
mc.shadingNode ('blendColors', asUtility=True, name='blendNode_elbow_translate')
mc.shadingNode ('blendColors', asUtility=True, name='blendNode_hand_translate')


#Connecting blending Nodes
#Arm
mc.connectAttr ('armJointIK.rotate', 'blendNode_arm_rotate.color1')
mc.connectAttr ('armJointIK.translate', 'blendNode_arm_translate.color1')

mc.connectAttr ('armJointFK.rotate', 'blendNode_arm_rotate.color2')
mc.connectAttr ('armJointFK.translate', 'blendNode_arm_translate.color2')

mc.connectAttr ('blendNode_arm_rotate.output', 'armJoint.rotate')
mc.connectAttr ('blendNode_arm_translate.output', 'armJoint.translate')

#Elbow
mc.connectAttr ('elbowJointIK.rotate', 'blendNode_elbow_rotate.color1')
mc.connectAttr ('elbowJointIK.translate', 'blendNode_elbow_translate.color1')

mc.connectAttr ('elbowJointFK.rotate', 'blendNode_elbow_rotate.color2')
mc.connectAttr ('elbowJointFK.translate', 'blendNode_elbow_translate.color2')

mc.connectAttr ('blendNode_elbow_rotate.output', 'elbowJoint.rotate')
mc.connectAttr ('blendNode_elbow_translate.output', 'elbowJoint.translate')

#Hand
mc.connectAttr ('handJointIK.rotate', 'blendNode_hand_rotate.color1')
mc.connectAttr ('handJointIK.translate', 'blendNode_hand_translate.color1')

mc.connectAttr ('handJointFK.rotate', 'blendNode_hand_rotate.color2')
mc.connectAttr ('handJointFK.translate', 'blendNode_hand_translate.color2')

mc.connectAttr ('blendNode_hand_rotate.output', 'handJoint.rotate')
mc.connectAttr ('blendNode_hand_translate.output', 'handJoint.translate')

#Helper for IK_FKSwitch
mc.circle (name='Switcher')
mc.group (name='Switcher_grp', empty=True, world=True)
mc.parent ('Switcher','Switcher_grp')
mc.parentConstraint ('handJoint','Switcher_grp', maintainOffset=False)
mc.delete ('Switcher_grp_parentConstraint1')
mc.move (-2,'Switcher_grp', z=True)
mc.parent ('Switcher_grp', 'hp_l_hand')
mc.addAttr ('Switcher', shortName='IK_FK', longName='IK_FK', defaultValue=0, keyable=True, minValue=0, maxValue=1 )
mc.setAttr ('Switcher.tx',lock=True ,keyable=False, channelBox=False)
mc.setAttr ('Switcher.ty',lock=True ,keyable=False, channelBox=False)
mc.setAttr ('Switcher.tz',lock=True ,keyable=False, channelBox=False)
mc.setAttr ('Switcher.rx',lock=True ,keyable=False, channelBox=False)
mc.setAttr ('Switcher.ry',lock=True ,keyable=False, channelBox=False)
mc.setAttr ('Switcher.rz',lock=True ,keyable=False, channelBox=False)
mc.setAttr ('Switcher.sx',lock=True ,keyable=False, channelBox=False)
mc.setAttr ('Switcher.sy',lock=True ,keyable=False, channelBox=False)
mc.setAttr ('Switcher.sz',lock=True ,keyable=False, channelBox=False)
mc.setAttr ('Switcher.v',lock=True ,keyable=False, channelBox=False)

#IK switch Connect
mc.connectAttr ('Switcher.IK_FK', 'blendNode_arm_rotate.blender')
mc.connectAttr ('Switcher.IK_FK', 'blendNode_arm_translate.blender')
mc.connectAttr ('Switcher.IK_FK', 'blendNode_elbow_rotate.blender')
mc.connectAttr ('Switcher.IK_FK', 'blendNode_elbow_translate.blender')
mc.connectAttr ('Switcher.IK_FK', 'blendNode_hand_rotate.blender')
mc.connectAttr ('Switcher.IK_FK', 'blendNode_hand_translate.blender')

#Create IK on arm

mc.ikHandle (name='ikh_arm',startJoint='armJointIK', endEffector='handJointIK', solver='ikRPsolver')

#Elbow pole vector constraint
mc.spaceLocator (name='lc_PoleVector_Elbow')
mc.setAttr ('lc_PoleVector_Elbow.overrideEnabled', 1)
mc.setAttr ('lc_PoleVector_Elbow.ove', lock=1)
mc.setAttr ('lc_PoleVector_Elbow.overrideColor', 13)

mc.group (name='lc_PoleVector_Elbow_grp', empty=True)
mc.parent ('lc_PoleVector_Elbow','lc_PoleVector_Elbow_grp')

elbowPos = mc.xform ('elbowJoint', query=True, worldSpace=True, translation=True)
mc.xform ('lc_PoleVector_Elbow_grp', worldSpace=True, translation=elbowPos)

mc.poleVectorConstraint ('lc_PoleVector_Elbow','ikh_arm',weight=1)

#Create IK helper
mc.curve (name='hp_IK_Hand', degree=1, point=[(2.269305, 1.74098, 1.74098), (-2.269305, -1.74098, 1.74098), (-2.269305, -1.74098, -1.74098), (-2.269305, 1.74098, -1.74098), (-2.269305, 1.74098, 1.74098), (-2.269305, -1.74098, 1.74098), (3.490972, -1.74098, 1.74098), (3.490972, 0.936389, 1.74098), (-2.269305, 1.74098, 1.74098), (3.490972, 0.936389, -1.74098), (3.490972, -1.74098, -1.74098), (-2.269305, -1.74098, -1.74098), ( -2.269305, 1.74098, -1.74098), (3.490972, 0.936389, -1.74098), (3.490972, 0.936389, 1.74098), (3.490972, -1.74098, -1.74098), (3.490972, 0.936389, -1.74098)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
mc.delete ('hp_IK_Hand.cv[0]')
mc.group (name='hp_IK_Hand_grp', empty=True)
mc.parent ('hp_IK_Hand','hp_IK_Hand_grp')

mc.setAttr ('hp_IK_Hand.overrideEnabled', 1)
mc.setAttr ('hp_IK_Hand.ove', lock=1)
mc.setAttr ('hp_IK_Hand.overrideColor', 13)

handPos = mc.xform ('handJoint', query=True, worldSpace=True, translation=True)
mc.xform ('hp_IK_Hand_grp', worldSpace=True, translation=handPos)

mc.parent ('ikh_arm', 'hp_IK_Hand')

#Extra attributes
mc.addAttr ('hp_IK_Hand', shortName='Twist', longName='Twist', defaultValue=0, keyable=True)
mc.addAttr ('hp_IK_Hand', shortName='Stretch', longName='Stretch', defaultValue=0, keyable=True)
mc.addAttr ('hp_IK_Hand', shortName='Roll', longName='Roll', defaultValue=0, keyable=True)

#Stretchy IK Arm
mc.shadingNode ('addDoubleLinear', asUtility=True, name='adlNode_ArmStretch')
mc.shadingNode ('clamp', asUtility=True, name='clampNode_ArmStretch')
mc.shadingNode ('multiplyDivide', asUtility=True, name='mdNode_ArmStretch')
mc.shadingNode ('multiplyDivide', asUtility=True, name='mdNode_elbowStretch')
mc.shadingNode ('multiplyDivide', asUtility=True, name='mdNode_handStretch')

#Measure tool
mc.select (clear=True)
armPos= mc.xform ('armJoint', query=True, worldSpace=True, translation=True)
handPos= mc.xform ('handJoint', query=True, worldSpace=True, translation=True)
disDim= mc.distanceDimension (startPoint=armPos, endPoint=handPos)

mc.rename ('distanceDimension1', 'disDimNode_ArmStretch')
mc.rename ('locator1', 'lctrDis_Arm')
mc.rename ('locator2', 'lctrDis_hand')
mc.parent ('lctrDis_Arm','JointChain')
mc.parent ('lctrDis_hand','hp_IK_Hand')

#Getting distances for the stretch
elbowLen = mc.getAttr ('elbowJoint.tx')
print elbowLen
handLen = mc.getAttr ('handJoint.tx')
print handLen
ArmLen = (elbowLen+handLen)
print ArmLen

mc.setAttr ('adlNode_ArmStretch.input2', ArmLen)
mc.setAttr ('mdNode_ArmStretch.input2X', ArmLen)
mc.setAttr ('mdNode_elbowStretch.input2X', elbowLen)
mc.setAttr ('mdNode_handStretch.input2X', handLen)

#Connecting the nodes

mc.connectAttr ('hp_IK_Hand.Stretch','adlNode_ArmStretch.input1')
mc.setAttr ('clampNode_ArmStretch.minR', 12)
mc.setAttr ('mdNode_ArmStretch.operation', 2)

mc.connectAttr ('disDimNode_ArmStretch.distance','clampNode_ArmStretch.inputR')
mc.connectAttr ('adlNode_ArmStretch.output','clampNode_ArmStretch.maxR')

mc.connectAttr ('clampNode_ArmStretch.outputR','mdNode_ArmStretch.input1X')
mc.connectAttr ('mdNode_ArmStretch.outputX','mdNode_elbowStretch.input1X')
mc.connectAttr ('mdNode_ArmStretch.outputX','mdNode_handStretch.input1X')

mc.connectAttr ('mdNode_elbowStretch.outputX','elbowJointIK.tx')
mc.connectAttr ('mdNode_handStretch.outputX','handJointIK.tx')

#Twist connection - No Flip
mc.select (clear=True)
mc.spaceLocator (name='lctrPv_arm')
armPos=mc.xform ('armJoint', query=True, worldSpace=True, translation=True)
mc.xform ('lctrPv_arm', worldSpace=True, translation=armPos)

mc.poleVectorConstraint ('lctrPv_arm','ikh_arm',weight=1)

mc.shadingNode ('plusMinusAverage', asUtility=True, name='pmaNode_ArmTwist')
mc.shadingNode ('multiplyDivide', asUtility=True, name='mdNode_ArmTwist')

mc.connectAttr ('hp_IK_Hand.Twist','mdNode_ArmTwist.input1X')
mc.connectAttr ('hp_IK_Hand.ry','mdNode_ArmTwist.input1Y')
mc.connectAttr ('armJoint.ry','mdNode_ArmTwist.input1Z')

mc.setAttr ('mdNode_ArmTwist.input2X',-1)
mc.setAttr ('mdNode_ArmTwist.input2Y',-1)
mc.setAttr ('mdNode_ArmTwist.input2Z',-1)

mc.connectAttr ('mdNode_ArmTwist.input1X','pmaNode_ArmTwist.input1D[0]')
mc.connectAttr ('mdNode_ArmTwist.input1Y','pmaNode_ArmTwist.input1D[1]')
mc.connectAttr ('pmaNode_ArmTwist.output1D','ikh_arm.twist')

mc.parent ('lctrPv_arm','armJoint')
mc.setAttr ('lctrPv_arm.visibility', 0)

#----------------------------------------------------------------------------------------#

#Clean Up

mc.parent ('lc_PoleVector_Elbow_grp','Helpers')
mc.group (name='Xtras', empty=True)
mc.parent ('hp_IK_Hand_grp','Xtras')
mc.parent ('disDimNode_ArmStretch','Xtras')

mc.group (name='Arm_Py_Week02', empty=True)
listOfGroups = ('Helpers','ArmRig','Xtras')
for items in listOfGroups:
    mc.parent (items, 'Arm_Py_Week02')

#Connections of FK's
mc.parentConstraint ('hp_l_arm', 'armJointFK', mo=True)
mc.parentConstraint ('hp_l_elbow', 'elbowJointFK', mo=True)
mc.parentConstraint ('hp_l_hand', 'handJointFK', mo=True)

#Visibilities
mc.setAttr ('disDimNode_ArmStretch.visibility',0)

mc.shadingNode ('reverse', asUtility=True, name='rvNode_SwitchIKFK')

mc.connectAttr ('Switcher.IK_FK','rvNode_SwitchIKFK.inputX')
mc.connectAttr ('rvNode_SwitchIKFK.outputX','hp_l_arm.visibility')
mc.connectAttr ('rvNode_SwitchIKFK.outputX','lc_PoleVector_Elbow.visibility')
mc.connectAttr ('Switcher.IK_FK','hp_IK_Hand.visibility')

#IKFK Constraints
mc.parentConstraint ('hp_l_hand', 'hp_IK_Hand', 'Switcher_grp', mo=True)

mc.connectAttr ('Switcher.IK_FK','Switcher_grp_parentConstraint1.hp_IK_HandW1')

mc.shadingNode ('reverse', asUtility=True, name='rvNode_SwitchPCIKFK')

mc.connectAttr ('Switcher.IK_FK','rvNode_SwitchPCIKFK.inputX')
mc.connectAttr ('rvNode_SwitchPCIKFK.outputX', 'Switcher_grp_parentConstraint1.hp_l_handW0')

mc.group (name='Switcher_grp_Xtransf', empty=True)
mc.parent ('Switcher_grp', 'Switcher_grp_Xtransf')
mc.parent ('Switcher_grp_Xtransf', 'Xtras')
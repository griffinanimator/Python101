#Creates a dictionary
arm_info={}
#Creates list that goes in a dictionary that defines placement. Note when creating points think of how they will look placed on a grid.
jntlytPlmt=(['ljnt_shldr', [0.0,0.0,2.0]], ['ljnt_elbow', [0.0,2.0,4.0]], ['ljnt_wrist', [0.0,0.0,7.0]])
#Build joints with a list
ljntList=[]
for jnt in jntlytPlmt:
    #create a name for the command to represent the making of joints
    jntlyt=cmds.joint(name=jnt[0], position=jnt[1])
    #Add jntlyt which holds the placement
    ljntList.append(jntlyt)
print ljntList
#Next another key will be added to the list. The arm_info is the dictionary or house every else goes in it.
arm_info['LjntInfo']=ljntList
cmds.select(all=True)
cmds.move(10,10,10)
#The layout was used to put items in the scene 
#Create an empty list
jntInfo=[]
cmds.select(deselect=True)
for ljnt in arm_info['LjntInfo']:
    #change name to a string
    jntName= ljnt.replace('ljnt', 'jnt')
    #Grabs positions of ljnt which not yet determined and places new joints from list in exact spot. This is for jnt placement
    PosJnt=cmds.xform(ljnt, query=True, worldSpace=True, translation=True)
    cmds.joint(name=jntName, position=PosJnt)
    jntInfo.append(jntName)
arm_info['jntInfo']=jntInfo

#Make IK
ikH=cmds.ikHandle(n='rp_lArm', solver='ikRPsolver', startJoint=arm_info['jntInfo']
[0], endEffector=arm_info['jntInfo'][2])
arm_info['IKH']=ikH
#Now hide joints for layout
cmds.setAttr('ljnt_shldr.visibility',0)
cmds.setAttr('ljnt_elbow.visibility',0)
cmds.setAttr('ljnt_wrist.visibility',0)
#Make Control
arm_info['ikControl']=cmds.curve( p=[(1.5,1.5,1.5),(1.5,1.5,-1.5), (-1.5,1.5,-1.5), (-1.5,1.5,1.5), (1.5,1.5,1.5), (1.5,-1.5,1.5),
(1.5,-1.5,-1.5), (1.5,1.5,-1.5), (-1.5,1.5,-1.5), (-1.5,-1.5,-1.5), (1.5,-1.5,-1.5),
(1.5,1.5,-1.5), (-1.5,1.5,-1.5),(-1.5,-1.5,-1.5), (-1.5,-1.5,1.5), (-1.5,1.5,1.5), 
(-1.5,1.5,-1.5), (1.5,1.5,-1.5), (1.5,1.5,1.5), (-1.5,1.5,1.5), (-1.5,-1.5,1.5),
(1.5,-1.5,1.5), (1.5,1.5,1.5)], d=1 )
cmds.rename(arm_info['ikControl'], 'anim_l_wrist01')
#This snaps control at wrist and freezes transformations
ikPos=cmds.xform('rp_lArm', q=True, ws=True, translation=True)
cmds.xform("anim_l_wrist01", ws=True, translation=ikPos)
cmds.scale(0.2, 0.2, 0.2)
cmds.makeIdentity(apply=True)
#Make a locator at ik
loc=cmds.spaceLocator(name='lctrl')
cmds.xform("lctrl", ws=True, translation=ikPos)
cmds.parent('rp_lArm', 'lctrl')
cmds.parent('lctrl', 'anim_l_wrist01')










   



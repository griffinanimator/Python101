import maya.cmds as mc

#Creates locators in defined positions
locList = (['loc_clavicleA', [0.0, 0.0, 0.0]], ['loc_shldrA',[10.0, 2.0, 0.0]], ['loc_elbowA',[30.0, 2.0, -2.0]], ['loc_wristA',[50.0, 2.0, 0.0]], ['loc_palmA',[60.0, 2.0, 0.0]])
cmds.select(d=True)
for l in range(len(locList)):
    print l
    print locList[l][0]
    print locList[l][1]
    mc.spaceLocator(n=locList[l][0], p=locList[l][1])

#Centrepivot the locators please

"""Break"""

#Creates joints in defined postions
jointList = (['jnt_clavicleA', [0.0, 0.0, 0.0]], ['jnt_shldrA',[10.0, 2.0, 0.0]], ['jnt_elbowA',[30.0, 2.0, -2.0]], ['jnt_wristA',[50.0, 2.0, 0.0]], ['jnt_palmA',[60.0, 2.0, 0.0]])
cmds.select(d=True)
for j in range(len(jointList)):
    print j
    print jointList[j][0]
    print jointList[j][1]
    cmds.joint(n=jointList[j][0], p=jointList[j][1])

    """Break"""
    
#Moves joints to locator (need help on snapping multiple joints to respective locators with same prefix eg:loc_) 
locPos = cmds.xform('loc_clavicleA', q=True, t=True, ws=True)
cmds.xform('jnt_clavicleA', t=locPos)

#Create ikHandle from jnt_shldrA to jnt_wristA
cmds.ikHandle(n= "l_ikh_arm", sj= "jnt_shldrA", ee= "jnt_wristA", sol = "ikRPsolver")
cmds.ikHandle(n= "sch_wrist", sj= "jnt_wristA", ee= "jnt_palmA", sol = "ikSCsolver")

#Parent,Rename and delete extra control
cmds.rename('loc_wristA', 'l_ctrl_hand')
cmds.delete('loc_shldrA', 'loc_clavicleA', 'loc_elbowA')
cmds.parent('l_ikh_arm', 'l_ctrl_hand')
cmds.parent('sch_wrist', 'loc_palmA')
cmds.group('loc_palmA', 'grp_wrist')

#create locator as pole vector, postion of pole vector not defined(to learn)
mc.spaceLocator(n='l_ctrPv_arm')
elbowPos = cmds.xform('jnt_elbowA', q=True, ws=True, t=True)
cmds.xform('l_ctrPv_arm', ws=True, t=elbowPos)
cmds.poleVectorConstraint ('l_ctrPv_arm', 'l_ikh_arm', weight=1)
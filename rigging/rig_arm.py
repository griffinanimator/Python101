shoulder=cmds.joint(name='shoulder_jnt', position=[5,10,-4])
arm=cmds.joint(name='forarm_jnt01', position=[3.5,10,-11])
wrist=cmds.joint(name='wrist_jnt', position=[3.5,9.5, -19])
handEnd=cmds.joint(name='hand_end_jnt', position=[3.5,9.5, -23])
cmds.select('wrist_jnt')
cmds.duplicate('wrist_jnt', name='fingerOne_jnt')
cmds.parent( world=True)
cmds.rotate(0,-20,-20)
cmds.duplicate(name='fingerTwo_jnt')
cmds.rotate(0,20,-28)
cmds.parent('fingerTwo_jnt', 'fingerOne_jnt', 'wrist_jnt')
cmds.ikHandle(n='rpIk_l_arm01', solver= 'ikRPsolver', startJoint='shoulder_jnt', endEffector='wrist_jnt')
box=cmds.curve( p=[(1.5,1.5,1.5),(1.5,1.5,-1.5), (-1.5,1.5,-1.5), (-1.5,1.5,1.5), (1.5,1.5,1.5), (1.5,-1.5,1.5),
(1.5,-1.5,-1.5), (1.5,1.5,-1.5), (-1.5,1.5,-1.5), (-1.5,-1.5,-1.5), (1.5,-1.5,-1.5),
(1.5,1.5,-1.5), (-1.5,1.5,-1.5),(-1.5,-1.5,-1.5), (-1.5,-1.5,1.5), (-1.5,1.5,1.5), 
(-1.5,1.5,-1.5), (1.5,1.5,-1.5), (1.5,1.5,1.5), (-1.5,1.5,1.5), (-1.5,-1.5,1.5),
(1.5,-1.5,1.5), (1.5,1.5,1.5)], d=1 )
cmds.rename(box, 'anim_l_wrist01')
cmds.parent('anim_l_wrist01', 'wrist_jnt')
cmds.setAttr("anim_l_wrist01.translateZ", 0)
cmds.setAttr("anim_l_wrist01.translateX", 0)
cmds.setAttr("anim_l_wrist01.translateY", 0)
cmds.scale(0.6, 0.6, 0.6)
cmds.parent('anim_l_wrist01', w=True)
cmds.makeIdentity(apply=True)
cmds.spaceLocator(n='wrist_loc')
wristPos=cmds.xform("wrist_jnt", q=True, worldSpace=True, translation=True )
cmds.xform('wrist_loc', worldSpace=True, translation=wristPos)
cmds.duplicate('anim_l_wrist01', n='anim_l_elbow01')
elbowPos=cmds.xform("forarm_jnt01", q=True, worldSpace=True, translation=True)
cmds.select('anim_l_elbow01')
cmds.move(3.5,10,-11, rpr=True)
cmds.move(-5,0,0, r=True)
cmds.scale(0.5, 0.5, 0.5)
cmds.makeIdentity(apply=True)
cmds.parentConstraint('wrist_loc', 'wrist_jnt')
cmds.parent('wrist_loc', 'anim_l_wrist01' )
cmds.parent('rpIk_l_arm01', 'wrist_loc')
cmds.select('anim_l_elbow01')
cmds.addAttr(shortName='Extra_Controls', longName='Extra_Controls', at='double') 
cmds.setAttr('anim_l_elbow01.Extra_Controls', cb=True )
cmds.setAttr('anim_l_elbow01.rx', lock=True, keyable=False, channelBox=False)
cmds.setAttr('anim_l_elbow01.ry', lock=True, keyable=False, channelBox=False)
cmds.setAttr('anim_l_elbow01.rz', lock=True, keyable=False, channelBox=False)
cmds.setAttr('anim_l_elbow01.sx', lock=True, keyable=False, channelBox=False)
cmds.setAttr('anim_l_elbow01.sy', lock=True, keyable=False, channelBox=False)
cmds.setAttr('anim_l_elbow01.sz', lock=True, keyable=False, channelBox=False)
cmds.poleVectorConstraint('anim_l_elbow01', 'rpIk_l_arm01')






   

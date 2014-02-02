import maya.cmds as cmds

#create a 4 joint chain
#

clavicle = "l_clavicle_jnt"
shoulder = "l_shoulder_jnt"
elbow = "l_elbow_jnt"
hand = "l_hand_jnt"
palm = "l_palm_jnt"

cmds.select ( d = True )
cmds.joint (n = clavicle)
cmds.joint (clavicle, e=True, zso = True, oj = 'xyz', p=[ 0.0, 0.0, 0.0])

cmds.joint (n = shoulder, p=[ 10.0, 2.0, 0.0])
cmds.joint (shoulder, e=True, zso = True, oj = 'xyz')


cmds.joint (n = elbow, p=[ 30.0, 2.0, -2.0])
cmds.joint (elbow, e=True, zso = True, oj = 'xyz')


cmds.joint (n = hand, p=[ 50.0, 2.0, 0.0])   
cmds.joint (hand, e=True, zso = True, oj = 'xyz')


cmds.joint (n = palm, p=[ 60.0, 2.0, 0.0])
cmds.joint (palm, e=True, zso = True, oj = 'xyz')

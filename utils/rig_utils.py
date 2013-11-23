import maya.cmds as cmds

def createJointChain(info, prefix, *args):
    # Clear the selection
    cmds.select(d=True)
    # Build the joints
    jntList = []
    for i in range(len(info['names'])):
        # Make a name for the joint.
        jntName = info['names'][i].replace('lctr', prefix)
        jnt = cmds.joint(name=jntName, position=info['positions'][i], a=True)
        jntList.append(jnt)
        
    # Make sure the new joint chain is oriented.
    cmds.joint(jntList[0], edit=True, oj='xyz', sao='yup', ch=True, zso=True)
    # We don't need that last joint so delete it.
    # Find the last item in jntList
    jlLen = len(jntList)
    cmds.delete(jntList[jlLen-1])
    # Remove the last joint from jntList
    jntList.pop(3)
    # Return the list of joints
    return jntList

def createIk(ikJnts):
	ikInfo = []
	ikhName = ikJnts[2].replace('ikj', 'ikh')
	ikh = cmds.ikHandle(n=ikhName, sj=ikJnts[0], ee=ikJnts[2], sol='ikRPsolver', p=2, w=.5 )
	# Make a poleVector
	pvCon = cmds.spaceLocator(n=ikhName+'_pv')
	tmpCon = cmds.parentConstraint(ikJnts[1], pvCon, mo=False)
	cmds.delete(tmpCon) 
	cmds.move(-1, pvCon, r=True, z=True )
	cmds.makeIdentity(pvCon, apply=True )
	# Creat a pv constraint
	cmds.poleVectorConstraint( pvCon, ikh[0] )
	return ikh

def importControlObject(ctrlFile):
	print ctrlFile
	cmds.file(ctrlFile, i=True)

""" This is rig_utils.  rig_utils doesn't need a class as it simply 
serves as a place to hold a bunch of regularly used functions used in
building a rig.  We can call functions from here to use in other scripts.
"""

def buildJoints(self, lytObj, prefix, *args):
    """ Print lytObj so you can see whats happening """
    print "This is the lytObj passed from rig_arm"
    print lytObj
    cmds.select(deselect=True)

    self.jointsInfo["orientatition"]='xyz'

    """ You can wrap the jointLength function into buildJoints """
    """ Lets make an empty list to store all the joint information.
    We will return that list at the end """
    joints = []
    cmds.select(d=True)
    for item in lytObj:
        newJointName = prefix+item[0]
    
        if cmds.objExists(newJointName) ==True:
            cmds.delete(newJointName)
            cmds.select(d=True)
        
        newJoint=cmds.joint(n=newJointName, p=item[1], a=True, roo='xyz')
        """ Append the newJoint to the joints list.  You can also add the joint positions
        so you end up returning a list similar to the lytObj list you passed in """
        joints.append([newJoint, item[1]])
        # We don't  realy need to store setAttrs in a dictionary.
        # You will run into an error here because item doesn't have an [2]
        #cmds.setAttr(jnt+'.jointOrientX', item[2][0])
        #cmds.setAttr(jnt+'.jointOrientY', item[2][1])
        #cmds.setAttr(jnt+'.jointOrientZ', item[2][2])

    # You can just setup the joint hierarchy once the joints have been made.
    for j in range(len(joints)):
        print "This is the current item from the joints list"
        print joints[j]
        if j[0] != 0:
            cmds.parent(joints[j][0], joints[j-1][0])

    return joints
import maya.cmds as mc

# Function that creates and orients a 3 joint chain based off position array
def jointChain(jointOrient="xyz",secondOrientAxis="yup"):
    ''' Takes list of positions as argument '''

    worldPos=listPositions()
    jointList=[]

    # Create number of joints equal to length of list, at the positions in the list
    for i in range(len(worldPos)):
        transform = worldPos[i]
        joint=mc.joint(position=(transform[0],transform[1],transform[2]),)
        jointList.append(joint)

    #orient joints
    for item in jointList:
        mc.joint(item, edit=True, orientJoint="{jointOrient}".format(jointOrient=jointOrient),
            sao="{secondOrientAxis}".format(secondOrientAxis=secondOrientAxis))

    mc.select(clear=True)



def listPositions():
    '''Takes a selection argument'''
    positions=[]

    # Store selection
    selection = mc.ls(selection=True,)
    # Validate selection of at least one object
    if len(selection) == 0:
        print("Please Select object(s) to list world position of")
    # Iterate through selection query world position
    for item in selection:
        position=mc.xform(item, query=True, worldSpace=True, translation=True,)
        # Add world positions to positions list
        positions.append(position)
    mc.select(clear=True)
    return positions

jointChain()



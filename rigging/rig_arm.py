import maya.cmds as mc

jointPosition = [[0,0,0],[1,1,1],[2,2,2]]

# Function that creates and orients a 3 joint chain based off position array
def jointChain():
    ''' Takes list of positions as argument '''

    worldPos =listPositions()
    # Find length of list
    length = len(listPositions())
    # Create number of joints equal to length of list, at the positions in the list
    for i in worldPos:
        mc.joint(position=([i][0],[i][1],[i][2]))


def listPositions():
    '''Takes a selection argument'''
    positions=[]

    # Store selection
    selection = mc.ls(selection=True,)
    # Iterate through selection query world position
    for item in selection:
        position=mc.xform(item, query=True, worldSpace=True, translation=True,)
        # Add world positions to positions list
        positions.append(position)

    return positions

jointChain()



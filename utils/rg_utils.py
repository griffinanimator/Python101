# Utils for writing to csv.  
def csvWrite():
    """ This is the path where the csv will be written.  Change this to a path on your local machine. """
    path = "R:/System/CSV_files/armCsv.csv" 
    
    """ Open the csv in maya for writing """
    writer = csv.writer(open(path, 'wb'), delimiter=',')
    
    """ Create a new list based off your selection """
    selectionList = cmds.ls(sl=True)
   
    """ Clear the selection """
    cmds.select(clear=True)
  
    for selection in selectionList:
        """ An empty list to hold both the joint names and the positions """
        jointInfo = []
  
        pos = cmds.xform(selection, q=True, t=True, ws=True)
       
        """ Append the name of the locator and it's position to a new list"""  
        """ I am splitting the positions into seperate variables to make things easier when I try read them later """     
        jointInfo.append(selection)
        jointInfo.append(pos[0])
        jointInfo.append(pos[1])
        jointInfo.append(pos[2])
        """ At this point you could use the joint info to build joints """
        """ Write the data to csv """
        writer.writerow(jointInfo)

    """ Print the joint info so you can see what is happening """
    print jointInfo
    


def csvRead(path):
    
    """ Empty lists to store name and position info """
    
    nodeInfo = []
    
    """ Open the csv """
    reader = csv.reader(open(path, 'rb'), delimiter=';', quotechar='"')
    
    """ Read each row in the csv to get the name and position """
    for row in reader:
        """ Get the value from the row and split it into variables we can use to build joints """
        positions = []
        nodeName = row[0]
        for i in range(len(row)):
        	if i != 0:
        		positions.append(row[i])
 
        """ Append the values to lists outside the for loop """
        nodeInfo.append([nodeName, positions])      

    """ return the list for use in another function """    
    return (nodeInfo)

# The following can be used for a space switching script or to find vectors.
def matchTwistAngle(twistAttribute, ikJoints, targetJoints):
    currentVector = []
    targetVector = []
    
    currentVector = calculateTwistVector(ikJoints[0], ikJoints[1], ikJoints[len(ikJoints)-1])
    targetVector = calculateTwistVector(targetJoints[0], targetJoints[1], targetJoints[len(targetJoints)-1])
    
    targetVector = normaliseVector(targetVector)
    currentVector = normaliseVector(currentVector)
    
    offsetAngle =calculateAngleBetweenNormalisedVectors(targetVector, currentVector)
    
    finalOffset = offsetAngle*-1
    finalOffset = offsetAngle

    return finalOffset

def calculateTwistVector(startJoint, secondJoint, endJoint, *args):
    a = cmds.xform(startJoint, q=True, ws=True, t=True)
    endPos = cmds.xform(endJoint, q=True, ws=True, t=True)
    
    b = [endPos[0] - a[0], endPos[1] - a[1], endPos[2] -a[2]]
    b = normaliseVector(b)
    
    p = cmds.xform(secondJoint, q=True, ws=True, t=True)
    
    p_minus_a = [p[0]-a[0], p[1]-a[1], p[2]-a[2]]
    p_minus_a__dot__b = p_minus_a[0]*b[0] + p_minus_a[1]*b[1] + p_minus_a[2]*b[2]
    
    p_minus_a__dot__b__multiply_b = [p_minus_a__dot__b * b[0], p_minus_a__dot__b * b[1], p_minus_a__dot__b * b[2]]
    
    q = [a[0] + p_minus_a__dot__b__multiply_b[0], a[1] + p_minus_a__dot__b__multiply_b[1], a[2] + p_minus_a__dot__b__multiply_b[2]]
    
    twistVector = [p[0] - q[0], p[1] - q[1], p[2] - q[2]]
    
    return twistVector  
    
def normaliseVector(vector, *args):
    from math import sqrt
    returnVector = list(vector)
    
    vectorLength = sqrt( returnVector[0]*returnVector[0] + returnVector[1]*returnVector[1] + returnVector[2]*returnVector[2])
    
    if vectorLength != 0:
        returnVector[0] /= vectorLength
        returnVector[1] /= vectorLength
        returnVector[2] /= vectorLength
    else:
        returnVector[0] = 1.0
        returnVector[1] = 0.0
        returnVector[2] = 0.0
        
    return returnVector  
    
def calculateAngleBetweenNormalisedVectors(VectA, VectB, *args):
    from math import acos, degrees
    
    dotProduct = VectA[0]*VectB[0] + VectA[1]*VectB[1] + VectA[2]*VectB[2]\
    
    if dotProduct <= -1.0:
        dotProduct = -1.0
    elif dotProduct >= 1.0:
        dotProduct = 1.0
        
    radians = acos(dotProduct)

    return degrees(radians)
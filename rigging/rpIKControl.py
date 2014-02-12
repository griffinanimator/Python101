# rpIKControl.py

import maya.cmds as mc
import maya.OpenMaya as om

def rpIKControl(name,startJoint,endJoint):
    '''
    Takes either a two joint selection or a start joint, end joint argument
    and creates an IK handle between these joints.
    Uses vector maths to determine position of pole vector
    Calls the create control functions for creating an IK control and a pole vector control

    '''

    selection = mc.ls(selection = True, type = "joint")
    prefix = "ik_"


    # Checks users selection is of two joints and not more
    if len(selection) < 2 or len(selection) > 2:
        print("Please select two joints to perform operation")

    # Creates IK Handle
    ikHandle =mc.ikHandle(startJoint = startJoint, endEffector = endJoint, solver = "ikRPsolver", name = "{prefix}{name}#".format(prefix = prefix, name = name))

    # Use PoleVectorPosition function to find where the pole vector control should be created.
    PVPosition = poleVectorPosition(startJoint, endJoint)

    mc.spaceLocator(position = (PVPosition[0],PVPosition[1],PVPosition[2]))

    # Use create controller functions to create controls on the end of the IK change and pole vector position.


    # Group/Organise the controllers and nodes


rpIKControl("arm","joint1","joint3")
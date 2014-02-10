#poleVectorPosition.py

import maya.cmds as mc
import maya.OpenMaya as om

def poleVectorPosition(startJoint, EndJoint):

    selection = [startJoint, EndJoint]
    jointPosition = []

    for joint in selection:
        position = mc.xform(joint, query = True, translation = True, worldSpace = True)
        jointPosition.append(position)

    position = mc.listRelatives(selection[1], parent = True)
    position = mc.xform(position, query = True, translation = True, worldSpace = True)
    jointPosition.append(position)

    # Determine position of Pole Vector Control
    A = om.MVector(jointPosition[0][0],jointPosition[0][1],jointPosition[0][2])
    B = om.MVector(jointPosition[1][0],jointPosition[1][1],jointPosition[1][2])
    C = om.MVector(jointPosition[2][0],jointPosition[2][1],jointPosition[2][2])

    D = B -A
    E = A + (D * 0.5)
    F = C - E
    G = C + (F * 2)

    PVPosition = [G[0], G[1], G[2]]

    return PVPosition





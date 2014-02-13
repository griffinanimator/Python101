import maya.cmds as mc

def splineIKScaleJoints (curve,axis,joints=[]):
    # get the shape of the curve
    temp = mc.listRelatives(curve,fullPath=True, shapes=True)
    curveShape = temp[0]

    # create a curveInfo
    curveInfo = mc.createNode("curveInfo",name="nodeCurveInfo_{curve}Info".format(curve=curve))

    # connecting the curve
    mc.connectAttr("{curveShape}.worldSpace[0]".format(curveShape=curveShape), "{curveInfo}.inputCurve".format(curveInfo=curveInfo))

    # getting the arc length
    arcLength = mc.getAttr("{curveInfo}.arcLength".format(curveInfo=curveInfo))

    # next, create a multiplyDivide node which will create the scale for us
    curveScale =mc.createNode("multiplyDivide", name="nodeMultiplyDiv_{curve}Scale".format(curve=curve))

    # set the operation to divide
    mc.setAttr("{curveScale}.operation".format(curveScale=curveScale),2)

    # connect the input1X to the arcLength
    mc.connectAttr("{curveInfo}.arcLength".format(curveInfo=curveInfo),"{curveScale}.input1X".format(curveScale=curveScale));

    # set the original arcLength
    mc.setAttr("{curveScale}.input2X".format(curveScale=curveScale),arcLength);

    #create a multiplyDivide for each joint and scale the length of them
    for joint in joints:
        # get the current length of the bone
        length = mc.getAttr("{joint}.{axis}".format(joint=joint,axis=axis))

        # create the multiply divide node
        jointScale = mc.createNode("multiplyDivide", name="nodeMultiplyDiv_{joint}Scale".format(joint=joint))

        # connect the curveScale.outputX to jointScale.input1X;
        mc.connectAttr("{curveScale}.outputX".format(curveScale=curveScale),"{jointScale}.input1X".format(jointScale=jointScale))

        # set the jointScale.input2X to the current length
        mc.setAttr("{jointScale}.input2X".format(jointScale=jointScale),length)

        # now connect the jointScale.outputX to the length of the joint;
        mc.connectAttr("{jointScale}.outputX".format(jointScale=jointScale),"{joint}.{axis}".format(joint=joint,axis=axis),force=True)

splineIKScaleJoints(curve="curve1",axis="tx",joints=["joint1","joint2","joint3","joint4","joint5","joint6","joint7"])
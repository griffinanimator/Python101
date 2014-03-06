import maya.cmds as cmds
class jointSplice:
    def __init__(self):
        self.UIElements = {}

    def jointChainSplicer_ui(self, *args):
        if cmds.window('awJointChainSplicer', exists=True):
            cmds.deleteUI('awJointChainSplicer')
        cmds.window('awJointChainSplicer', w=500, h=200, sizeable=True)
        form = cmds.formLayout()
        self.UIElements['tfbg'] = cmds.textFieldButtonGrp(l="How Many?", bl="Cut", bc=self.jointChainSplicer)
        cmds.showWindow('awJointChainSplicer')

    def jointChainSplicer(self, *args):
        gettfbgvalue = cmds.textFieldButtonGrp(self.UIElements['tfbg'], q=True, tx=True)
        origJnt = cmds.ls(sl=1)
        cmds.select(hi=True)
        countSelected = cmds.ls(sl=1)

        if len(countSelected) < 2:
            cmds.warning('Must select a bone')
        else:
            cmds.pickWalk(d='down')
            selChild = cmds.ls(sl=1)
            cmds.select(selChild[0])
            childJoint_tX = cmds.getAttr(selChild[0] + '.tx')
            sourceJoint_radius = cmds.getAttr(origJnt[0] + '.radius')
            cmds.pickWalk(d='up')
            if len(gettfbgvalue) < 2:
                cmds.warning('Have to have at least one segment')
            else:
                for i in range(len(gettfbgvalue)):
                    print 'hi'
                    newJnt = cmds.joint(radius=sourceJoint_radius, o=(0, 0, 0))
                    cmds.move(int(childJoint_tX)/int(gettfbgvalue), 0, 0, newJnt, r=True, ls=True)
                lastJoint = cmds.ls(sl=1)
                cmds.parent(selChild[0], lastJoint[0])
                cmds.select(cl=True)
start = jointSplice()
start.jointChainSplicer_ui()

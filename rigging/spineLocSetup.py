import maya.cmds as cmds

class awSpineCall():
    def __init__(self):
        self.hierarchy = {'root01':{'pos':[0, 8.994, 0], 'children': ['spineA']},
                          'spineA':{'pos':[0, 9.467, 0], 'children':['spineB']},
                          'spineB':{'pos':[0, 9.602, 0], 'children': ['spineC']},
                          'spineC':{'pos':[0, 10.412, 0], 'children':['spineD']},
                          'spineD':{'pos':[0, 11.356, 0], 'children':['spineE']},
                          'spineE':{'pos':[0, 12.293, 0], 'children':['neck']},
                          'neck':{'pos':[0, 12.73, -0.182], 'children':['headA']},
                          'headA':{'pos':[0, 13.631, 0.017], 'children':['jawA', 'headB', 'L_eye']},
                          'headB':{'pos':[0, 17.028, 0.769], 'children':[]},
                          'jawA':{'pos':[0, 14.302, -0.359], 'children':['jawB']},
                          'jawB':{'pos':[0, 13.419, 1.421], 'children':[]},
                          'L_eye':{'pos':[0.395, 14.903, 0.9], 'children':[]}}
        self.spineLocators = []
        self.spineJoints = []

    def seeIfJoints01Exists(self, *args):
        if cmds.objExists('joints01'):
            self.awCreateSpineLocs()
        else:
            cmds.warning('You need to create the group hierarchy so I can place everything in the correct place')

    def seeIfLocatorsExist(self, *args):
        if cmds.objExists('JntLoc_root01'):
            self.awCreateJoints()
        else:
            cmds.warning('You have to place joints before you can build the bones')

    def awPlaceSpineLocs(self, name, parent=None, *args):
        spineLocName = ('JntLoc_' + str(name))
        makeLoc = cmds.spaceLocator(n=spineLocName, p=(0, 0, 0))[0]
        self.spineLocators.append(makeLoc)
        locMove = cmds.move(self.hierarchy[name]['pos'][0], self.hierarchy[name]['pos'][1],
                            self.hierarchy[name]['pos'][2], makeLoc, absolute=True)
        if parent:
            cmds.parent(spineLocName, parent)
        for child in self.hierarchy[name]['children']:
            self.awPlaceSpineLocs(child, parent=spineLocName)

    def awCreateSpineLocs(self, *args):
        self.awPlaceSpineLocs('root01')
        cmds.parent('JntLoc_root01', 'joints01')
            
    def awPlaceJoints(self, *args):
        for loc in self.spineLocators:
            cmds.select(d=True)
            jntName = loc.replace('JntLoc_', 'bn_')
            makeJnt = cmds.joint(name=jntName, p=(0, 0, 0))
            self.spineJoints.append(makeJnt)
            parentGet = cmds.listRelatives(loc, p=True)
            if parentGet:
                cmds.parent(makeJnt, parentGet[0].replace('JntLoc_', 'bn_'))
            jntConstraint = cmds.parentConstraint(loc, makeJnt)
            cmds.delete(jntConstraint)

    def awCreateJoints(self, *args):
        self.awPlaceJoints()
        cmds.select(cl=True)
'''
    def UI_(self, *args):
        if cmds.window('spineTest', exists=True):
            cmds.deleteUI('spineTest')
        cmds.window('spineTest', w=300, h=300)
        cmds.columnLayout()
        cmds.button(c=self.seeIfJoints01Exists)
        cmds.button(c=self.seeIfLocatorsExist)

        cmds.showWindow('spineTest')
'''
start = awSpineCall()
start.UI_()




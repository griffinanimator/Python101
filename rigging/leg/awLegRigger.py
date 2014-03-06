import maya.cmds as cmds

class awLegLocSetup:
    def __init__(self):
        self.hierarchy={'L_thigh':{'pos':[0.833, 8.994, -0.097], 'children':['L_knee']},
                        'L_knee':{'pos':[0.833, 4.973, 0.26], 'children':['L_ankle']},
                        'L_ankle':{'pos':[0.833, 0.917, -0.002], 'children':['L_ball']},
                        'L_ball':{'pos':[0.833, 0.479, 1.155], 'children':['L_Toe']},
                        'L_Toe': {'pos': [0.833, 0, 2.114], 'children': []}}
        self.legLocators = []
        self.legJoints = []
        self.legControls = []
        self.legLocPos = []

    def awPlaceLegLocs(self, name, parent=None, *args):
        legLocName = ('JntLoc_' +str(name))
        makeLegLoc = cmds.spaceLocator(n=legLocName, p=(0, 0, 0))[0]
        self.legLocators.append(makeLegLoc)
        legLocMove = cmds.move(self.hierarchy[name]['pos'][0], self.hierarchy[name]['pos'][1],
                               self.hierarchy[name]['pos'][2], makeLegLoc, absolute=True)
        if parent:
            cmds.parent(legLocName, parent)
        for child in self.hierarchy[name]['children']:
            self.awPlaceLegLocs(child, parent=legLocName)

    def awCreateLegLocs(self, *args):
        self.awPlaceLegLocs('L_thigh')

start = awLegLocSetup()
start.awCreateLegLocs()
'''
    def UI_(self, *args):
        if cmds.window('awLegRigger', exists=True):
            cmds.deleteUI('awLegRigger')
        cmds.window('awLegRigger', w=300, h=200)
        cmds.rowColumnLayout(nc=2)
        cmds.button('test')
        cmds.showWindow('awLegRigger')
'''
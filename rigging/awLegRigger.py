import maya.cmds as cmds

class awLegRigger:
    def __init__(self):
        self.hierarchy={'L_thigh':{'pos':[0.833, 8.994, -0.097], 'children':['L_knee']},
                        'L_knee':{'pos':[0.833, 4.973, 0.26], 'children':['L_ankle']},
                        'L_ankle':{'pos':[0.833, 0.917, -0.002], 'children':['L_ball']},
                        'L_ball':{'pos':[0.833, 0.479, 1.155], 'children':['L_Toe']},
                        'L_Toe': {'pos': [0.833, 0, 2.114], 'children': []}}
        self.legLocators = {}
        self.legJoints = {}
        self.legControls = {}
        self.legLocPos = {}

    def UI_(self, *args):
        if cmds.window('awLegRigger', exists=True):
            cmds.deleteUI('awLegRigger')
        cmds.window('awLegRigger', w=300, h=200)
        cmds.rowColumnLayout(nc=2)
        cmds.button('test')
        cmds.showWindow('awLegRigger')
start = awLegRigger()
start.UI_()
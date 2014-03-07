import maya.cmds as cmds

title = 'Alex Widener Character Picker '
version = 'v 0.01'

class awPicker():

    def __init__(self, *args):
        self.UIElements = {}
        #self.widgets = {}

    def buildUI(self, *args):
        if cmds.window('awCharacterPicker', exists=True):
            cmds.deleteUI('awCharacterPicker')
        cmds.window('awCharacterPicker', w=300, h=300, t=title + version)
        cmds.showWindow('awCharacterPicker')

start = awPicker()
start.buildUI()
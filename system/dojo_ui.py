import maya.cmds as cmds
import rigging.rig_arm as arm
reload(arm)
import util.file_utils as util
reload(util)

class RDojo_UI:

    def __init__(self, *args):
        print 'In RDojo_UI'
        self.UIElements = {}
        self.ui()

    def ui(self, *args):
        windowName = "Window"
        if cmds.window(windowName, exists = True):
            cmds.deleteUI(windowName)

        windowWidth = 110
        windowHeight = 150
        buttonWidth = 100
        buttonHeight= 30

        self.UIElements["window"] = cmds.window(windowName, width = windowWidth, height = windowHeight, title = "RDojo_UI", sizeable = True)

        self.UIElements["guiFlowlayout1"] = cmds.flowLayout(v=True, width = windowWidth, height = windowHeight, bgc = [0.2,0.2,0.2]) #flowLayout is simplest layout. Uses 1 column

        cmds.separator(p= self.UIElements["guiFlowlayout1"])
        self.UIElements["layout_button"] = cmds.button(label = "layout", width = buttonWidth, height = buttonHeight, p = self.UIElements["guiFlowlayout1"], c=self.createLyt)
        self.UIElements["build_button"] = cmds.button(label = "build", width = buttonWidth, height = buttonHeight, p = self.UIElements["guiFlowlayout1"], c=self.createArm)
        self.UIElements["save_button"] = cmds.button(label = "save", width = buttonWidth, height = buttonHeight, p = self.UIElements["guiFlowlayout1"], c=self.saveArm)
        self.UIElements["load_button"] = cmds.button(label = "load", width = buttonWidth, height = buttonHeight, p = self.UIElements["guiFlowlayout1"], c=self.loadArm)

        cmds.showWindow(windowName)

    def createLyt(self, *args):
        locLayout = arm.rig_arm()
        locLayout.build_Locators()

    def createArm(self, *args):
        armLayout = arm.rig_arm()
        armLayout.build_Arm()

    def saveArm(self, *args):
        save = util.fileManager()
        save.createCharFolder()

    def loadArm(self, *args):
        load = util.fileManager()
        load.loadScene()

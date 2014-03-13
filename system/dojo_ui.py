import maya.cmds as cmds
import rigging.rig_arm as arm
reload(arm)
import rigging.rig_leg as leg
reload (leg)
import util.file_utils as util
reload(util)

class RDojo_UI:

    def __init__(self, *args):
        print 'In RDojo_UI'
        self.UIElements = {}
        self.buttonLimb = [] #buttons for arm and leg
        self.buttonSide = [] #buttons for left and right
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
        cmds.radioCollection()
        
        self.buttonLimb.append(cmds.radioButton(label = 'Arm', sl=True))
        self.buttonLimb.append(cmds.radioButton(label = 'Leg')) 

        cmds.radioCollection()
        self.buttonSide.append(cmds.radioButton(label = 'Left', sl=True))
        self.buttonSide.append(cmds.radioButton(label = 'Right'))


        self.UIElements["layout_button"] = cmds.button(label = "layout", width = buttonWidth, height = buttonHeight, p = self.UIElements["guiFlowlayout1"], c=self.createLyt)
        self.UIElements["build_button"] = cmds.button(label = "build", width = buttonWidth, height = buttonHeight, p = self.UIElements["guiFlowlayout1"], c=self.createLimb)
        self.UIElements["save_button"] = cmds.button(label = "save", width = buttonWidth, height = buttonHeight, p = self.UIElements["guiFlowlayout1"], c=self.saveLimb)
        self.UIElements["load_button"] = cmds.button(label = "load", width = buttonWidth, height = buttonHeight, p = self.UIElements["guiFlowlayout1"], c=self.loadLimb)

        cmds.showWindow(windowName)

    def createLyt(self, *args):  #create locator layout
        if cmds.radioButton(self.buttonLimb[0],q = True, sl = True) is True: # if button is 'arm'
            locLayout = arm.rig_arm()
            locLayout.build_Locators(self.buttonSide)
        elif cmds.radioButton(self.buttonLimb[1],q = True, sl = True) is True: #if button is 'leg'
            locLayout = leg.rig_leg()
            locLayout.build_Locators(self.buttonSide)
        else:
            print "Layout is broke"


    def createLimb(self, *args): #build the limb
        if cmds.radioButton(self.buttonLimb[0],q = True, sl = True) is True:
            armLayout = arm.rig_arm()
            armLayout.build_Arm(self.buttonSide)
        elif cmds.radioButton(self.buttonLimb[1],q = True, sl = True) is True:
            armLayout = leg.rig_leg()
            armLayout.build_Leg(self.buttonSide)
        else:
            print "createLimb is broke"

    def saveLimb(self, *args): #save limb into a file
        save = util.fileManager()
        save.createCharFolder()

    def loadLimb(self, *args): #load limb in as a reference
        load = util.fileManager()
        load.loadScene()

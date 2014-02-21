import maya.cmds as cmds
import json
import tempfile

# Import our json_utils module
import utils.json_utils as json_utils
reload(json_utils)

# The UI class
class RDojo_UI:

    # The __init__ function
    # Please look at this documentation
    # http://docs.python.org/2/tutorial/classes.html
    def __init__(self, *args):
        print 'In RDojo_UI'
        """ Create a dictionary to store UI elements.
        This will allow us to access these elements later. """
        self.UIElements = {}

    # The function for building the UI
    def ui(self, *args):
        """ Check to see if the UI exists """
        windowName = "Window"
        if cmds.window(windowName, exists=True):
            cmds.deleteUI(windowName)
        """ Define width and height for buttons and windows"""    
        windowWidth = 110
        windowHeight = 110
        buttonWidth = 100
        buttonHeight = 30

        self.UIElements["window"] = cmds.window(windowName, width=windowWidth, height=windowHeight, title="RDojo_UI", sizeable=True)
        
        self.UIElements["guiFlowLayout1"] = cmds.flowLayout(v=False, width=windowWidth, height=windowHeight, bgc=[0.2, 0.2, 0.2])

        # Rig arm button
        cmds.separator(p=self.UIElements["guiFlowLayout1"])
        self.UIElements["rigarm_button"] = cmds.button(label='rig arm', width=buttonWidth, height=buttonHeight, p=self.UIElements["guiFlowLayout1"], c=self.rigArm) 

        """ Show the window"""
        cmds.showWindow(windowName)



    def rigArm(self, *args):
        import rigging.rig_arm as Rig_Arm
        reload(Rig_Arm)
        Rig_Arm = Rig_Arm.Rig_Arm()
        Rig_Arm.rigArm()
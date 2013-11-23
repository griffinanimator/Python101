import maya.cmds as cmds
import json
import tempfile

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

        # Load Layout button
        cmds.separator(p=self.UIElements["guiFlowLayout1"])
        self.UIElements["loadLayout_button"] = cmds.button(label='load layout', width=buttonWidth, height=buttonHeight, p=self.UIElements["guiFlowLayout1"], c=self.createLayout) 

        # Save Layout button
        cmds.separator(p=self.UIElements["guiFlowLayout1"])
        self.UIElements["saveLayout_button"] = cmds.button(label='save layout', width=buttonWidth, height=buttonHeight, p=self.UIElements["guiFlowLayout1"], c=self.saveLayout) 

        # Rig arm button
        cmds.separator(p=self.UIElements["guiFlowLayout1"])
        self.UIElements["rigarm_button"] = cmds.button(label='rig arm', width=buttonWidth, height=buttonHeight, p=self.UIElements["guiFlowLayout1"], c=self.rigArm) 

        """ Show the window"""
        cmds.showWindow(windowName)

    def createLayout(self, *args):
        basicFilter = "*.json"
        fileName = cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=2, fm=1, okc='Load')

        # Read the Json file
        data = self.readJson(fileName)
        info = json.loads( data )

        # Lets use a loop to build locators
        for i in range(len(info['names'])):
            lctr = cmds.spaceLocator(name=info['names'][i])
            # The position flag won't yield the desired
            # results, so we position the locators after we 
            # make them.
            cmds.xform(lctr, ws=True, t=info['positions'][i])

    def saveLayout(self, *args):
        basicFilter = "*.json"
        fileName = cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=2, fm=1, okc='Save')
        # Make a new dictionary to store the updated locator information.
        newLctrInfo = {}
        # Find the locators in the scene.
        # * works as a wildcard in a string
        cmds.select('lctr*')
        # Store the selected locators to a variable
        lctrSel = cmds.ls(sl=True, type='transform')
        # Clear the selection
        cmds.select(d=True)
        # Now get the position of each locator.
        # Make a new list to hold the positions.
        lctrPositions = []
        for each in lctrSel:
            pos = cmds.xform(each, q=True, ws=True, t=True)
            lctrPositions.append(pos)
        # Now pop our lists into the dictionary.
        newLctrInfo['names']=lctrSel
        newLctrInfo['positions']=lctrPositions
        # Define a path to save the json file.
  
        self.writeJson(fileName, newLctrInfo)

    def rigArm(self, *args):
        import rigging.rig_arm as Rig_Arm
        reload(Rig_Arm)
        Rig_Arm = Rig_Arm.Rig_Arm()
        Rig_Arm.rigArm()
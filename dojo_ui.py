""" Dojo_UI 
    week 05 assignment
"""


import maya.cmds as cmds
import json

#import json_utilitis
"""import utils.json_utils as json_utils
reload(json_utils)"""

# UI class
class RDojo_UI:
    def __init__(self, *args):
        self.UIElements = {}
        self.windowName = "Dojo"

    def ui(self, *args):
        #Check to see if the UI exists
        windowName = self.windowName
        #windowName = "Window"
        if cmds.window(windowName, exists=True):
            cmds.deleteUI(windowName)
        #Define width and height for buttons and windows  
        windowWidth = 300
        windowHeight = 300
        buttonWidth = 300
        buttonHeight = 30

        self.UIElements["window"] = cmds.window(windowName, width=windowWidth, height=windowHeight, title="RDojo_UI", sizeable=True)    
        self.UIElements["guiFlowLayout1"] = cmds.flowLayout(v=True, width=windowWidth, height=windowHeight, bgc=[0.2, 0.2, 0.2])

        # Load Layout button
        cmds.separator(p=self.UIElements["guiFlowLayout1"])
        self.UIElements["loadLayout_button"] = cmds.button(label='load layout', width=buttonWidth, height=buttonHeight, p=self.UIElements["guiFlowLayout1"], c=self.createLayout) 

        # Rig arm button
        cmds.separator(p=self.UIElements["guiFlowLayout1"])
        self.UIElements["rigArm_button"] = cmds.button(label='rigArm', width=buttonWidth, height=buttonHeight, p=self.UIElements["guiFlowLayout1"], c=self.rigArm) 
         
        #Show the window
        cmds.showWindow(windowName)

    def createLayout (self, *args):
        
        fileName = "C:/Users/Wagner/PersonalArt/Scripting/Rigging_Dojo/Python101/locator_info.json"
        
        def readJson(fileName):
            """
            # works too but with seems to be better for file opening 
            f = open(fileName,'r')
            for line in f:
                return line
            f.close()
            """
            with open(fileName, 'r') as inFile:
                data = inFile.read()
            return data
        
        data = readJson(fileName)
        
        # Read the Json file
        info = json.loads( data )
        
        # get info from json loaded file
        for i in range(len(info["names"])):
            print str(i) +": " + str(info["names"][i]) + " -> " + str(info["positions"][i])
            loc = cmds.spaceLocator (n=info["names"][i])
            cmds.xform(loc, ws=True, t=info["positions"][i])
        
    def rigArm(*args):
        import arm_rig as arm_rig
        arm_rig.UI() 

myDojo = RDojo_UI()
myDojo.ui()
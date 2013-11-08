import maya.cmds as cmds
# The UI class
class RDojo_UI:

	# The __init__ function
	# Please look at this documentation
	# http://docs.python.org/2/tutorial/classes.html
	def __init__(self, *args):
		print 'In RDojo_UI'
		""" Create a dictionary to store UI elements.
		This will allow us to access these elements later. """
        UIElements = {}

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

        UIElements["window"] = cmds.window(windowName, width=windowWidth, height=windowHeight, title="Window", sizeable=True)
        
        UIElements["guiFlowLayout1"] = cmds.flowLayout(v=False, width=220, height=windowHeight, bgc=[0.2, 0.2, 0.2])

        cmds.separator(p=UIElements["guiFlowLayout1"])
        UIElements["layout_button"] = cmds.button(label='layout', width=buttonWidth, height=buttonHeight, p=UIElements["guiFlowLayout1"]) 


        """ Show the window"""
        cmds.showWindow(windowName)  
  


 """
 import system.dojo_ui as dojo_ui
reload(dojo_ui)
rdUi = dojo_ui.RDojo_UI()

""" 
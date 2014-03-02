import maya.cmds as cmds

class RDojo_UI:

	def __init__(sef, *args):
		print 'In RDojo_UI'
		self.UIElements = {}

	def ui(self, *args):
		windowName = "Window"
		if cmds.window(windowName, exists = True):
			cmds.deleteUI(windowName)

		windowWidth = 110
		windowHeight = 110
		buttonWidth = 100
		buttonHeight= 30

		self.UIElements["window"] = cmds.window(windowName, width = windowWidth, height = windowHeight, title = "RDojo_UI", sizeable = True)

		self.UIElements["guiFlowlayout1"] = cmds.flowLayout(v=False, width = windowWidth, height = windowHeight, bgc = [0.2,0.2,0.2]) #flowLayout is simplest layout. Uses 1 column

		cmds.separator(p=self.UIElements["guiFlowLayout1"])
		self.UIElements["layout_button"] = cmds.button(label = "layout", width = buttonWidth, height = buttonHeight, p = UIElements["guiFlowLayout1"], c=self.createLyt)

		cmds.showWindow(windowName)

	def createLyt(self, *args)
		print 'lyt'

'''
import system.dojo_ui as dojo_ui
reload(dojo_ui)
rdUi = dojo_ui.RDojo_UI()
'''

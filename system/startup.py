import sys
import maya.cmds as cmds
import pymel.core as pm
import system.dojo_ui as dojo
reload(dojo)

def create_Menu(*args):
	maya_Window = cmds.window('MayaWindow', ma=True, q=True)
	for m in maya_Window: #creates the RDMenu in the menu bar
		if m == 'RDojo_Menu':
			cmds.deleteUI('RDojo_Menu', m=True)
	cmds.menu('RDojo_Menu', label='RDMenu', to=True, p='MayaWindow')
	cmds.menuItem(label="Limbs", command= dojo.RDojo_UI)	#builds a submenu that will open the window for building the limbs
	
create_Menu()
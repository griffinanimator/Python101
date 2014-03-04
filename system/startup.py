import sys
import maya.cmds as cmds
import pymel.core as pm
import system.dojo_ui as dojo
reload(dojo)

def create_Menu(*args):
	maya_Window = cmds.window('MayaWindow', ma=True, q=True)
	for m in maya_Window:
		if m == 'RDojo_Menu':
			cmds.deleteUI('RDojo_Menu', m=True)
	cmds.menu('RDojo_Menu', label='RDMenu', to=True, p='MayaWindow')
	cmds.menuItem(label="arm", command= dojo.RDojo_UI)
	
create_Menu()




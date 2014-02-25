import maya.cmds as cmds
import pymel.core as pm
import rigging.rig_arm as arm
reload(arm)
#import data.loc_info as json

cmds.currentUnit(linear='in')
cmds.currentUnit(time='film')
pm.mel.eval('setProject "C:/Users/Sarah/Desktop/test"')

def create_Menu(*args):
	maya_Window = cmds.window('MayaWindow', ma=True, q=True)
	for m in maya_Window:
		if m == 'RDojo_Menu':
			cmds.deleteUI('RDojo_Menu', m=True)
	cmds.menu('RDojo_Menu', label='RDMenu', to=True, p='MayaWindow')
	#cmds.menuItem(label="arm", command= 'arm.call_To_Build_Loc()')

def run_Script():
	#C:\Users\Sarah\Documents\GitHub\Python101\rigging\rig_arm.py
	print "HELLOO!"
	
create_Menu()




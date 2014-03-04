import os
import sys
import maya.cmds as cmds
import pymel.core as pm

cmds.upAxis( ax='y', rv=True )
cmds.currentUnit( linear='in' )
cmds.currentUnit( time='film' )
pm.mel.eval('setProject "C:/Users/Ganapathi K A/Desktop"')

def create_Menu(*args):
	mi = cmds.window( 'MayaWindow', ma=True, q=True)
	for m in mi:
		if m =='RDojo_Menu'
			cmds.deleteUI('RDojo_Menu', m=True)
	#to=tear off, p=parent to mayawindow
	cmds.menu( 'RDojo_Menu', label='RDMenu', to=True, p='MayaWindow')
	cmds.menuItem(label="arm", command="run_Script()")

#calling function, () to call specific arguments
create_Menu()

def run_Script():
	#C:/Users/Ganapathi K A/Documents/GitHub/Python101/rigging/rig_arm.py
	print "Hello"
import maya.cmds as cmds

cmds.upAxis( ax='y', rv=True )
cmds.currentUnit( linear='cm' )
cmds.currentUnit( time='ntsc' )


def layOutButton(*args):
	import system.practice_ui as practice_ui
	reload(practiceui)
	practiceui=practiceui.Practice_UI()
	practiceui.ui()



def createMenu(*args):
	mi = cmds.window('MayaWindow', ma=True, q=True)
	for m in mi:
		if m == 'RDojo_Menu':
			cmds.deleteUI('RDojo_Menu', m=True)

	cmds.menu('RDojo_Menu', label='RDMenu', to=True, p='MayaWindow')
	cmds.menuItem('RiggingTools', c=layOutButton)


createMenu()
	

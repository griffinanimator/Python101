import maya.cmds as cmds
def createMenu(*args):
    mi = cmds.window('MayaWindow', ma=True, q=True)
    for m in mi:
        if m == 'RDojo':
            cmds.deleteUI('RDojo', m=True)
    cmds.menu('RDojo', label='RDojo', to=True, p='MayaWindow')
    cmds.menuItem('Rigger')
createMenu()



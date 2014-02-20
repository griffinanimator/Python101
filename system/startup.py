import maya.cmds as cmds


def pressButton(*args):
    import rigging.awRig
    reload(rigging.awRig)
    rigging.awRig.awQuickRigger()
    
def awCharacterPickerLoad(*args):
    import rigging.awCharacterPicker
    reload(rigging.awCharacterPicker)
    rigging.awCharacterPicker.awPicker()

    
def createMenu(*args):
    mi = cmds.window('MayaWindow', ma=True, q=True)
    for m in mi:
        if m == 'AlexWidener_Menu':
            cmds.deleteUI('AlexWidener_Menu', m=True)
    cmds.menu('AlexWidener_Menu', label='AlexWidener', to=True, p='MayaWindow')
    cmds.menuItem('awRigger', c=pressButton)
    cmds.menuItem('awCharacterPicker', c=awCharacterPickerLoad)
createMenu()
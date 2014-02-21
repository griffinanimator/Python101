import maya.cmds as mc

#mc.upAxis(ax="y",rv=True)
#mc.currentUnit(linear="cm")

def createMenu(*args):
    mi=mc.window("MayaWindow",ma=True,q=True)
    for m in mi:
        if m =="RDojo_Menu":
            mc.deleteUI("RDojo_Menu",m=True)
    mc.menu("RDojo_Menu",label="RDMenu",to=True,p="MayaWindow")
    riggingTools=mc.menuItem(label="Rigging Tools",subMenu=True)
    mc.menuItem(label="Create Layout",parent=riggingTools,command=createUI)

def createUI(*args):
    import system.dojo_ui as dojo_ui
    reload(dojo_ui)
    rdUI=dojo_ui.RDojo_UI()
    rdUI.ui()

createMenu()
import maya.cmds as mc

#mc.upAxis(ax="y",rv=True)
#mc.currentUnit(linear="cm")

def createMenu(*args):
    mi=mc.window("MayaWindow",ma=True,q=True)
    for m in mi:
        if m =="RDojo_Menu":
            mc.deleteUI("RDojo_Menu",m=True)
    mc.menu("RDojo_Menu",label="RDMenu",to=True,p="MayaWindow")

createMenu()
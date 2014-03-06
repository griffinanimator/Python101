#Turn off LRA for whatever is selected
import maya.cmds as cmds
def lraOffTool():

    sel = cmds.ls(sl=1)
    for each in sel:
        on = cmds.toggle(each, q=True, la=True)
        if on == 1:
            cmds.toggle(la=True)
lraOffTool()
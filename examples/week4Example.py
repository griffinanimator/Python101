""" Iwrote up this example to illustrate a way of stremlining your code.
This example is inspired by some very fine work one of you posted on Git.
"""


import maya.cmds as cmds
# We will use one line of PyMel
import pymel.core as pm


def buttonPressed(name):
    print "pressed %s!" % name


# Using lambda
win = cmds.window(title="My Window")
layout = cmds.columnLayout()
btn = cmds.button( command = lambda *args: buttonPressed('chad') )
cmds.showWindow()


# Callback objects
win = cmds.window(title="My Window")
layout = cmds.columnLayout()
names = [ 'chad', 'robert', 'james' ]
for name in names:
    """ Lambda won't work inside a loop.  We could use Callback if we switch 
    over to PyMel for a moment.  I realize this is a Python class
    but it is neat to get a taste of PyMel. """
    pm.button( label=name, command = Callback( buttonPressed, name ) )
cmds.showWindow()



"""
This brings us to this example based on the work one of you did.
I like the idea behind the setup, however in it's current state
we need one function per locator.  This makes for a lot of lines 
of code that will be difficult to maintain when you get into
building legs, spines, and so on.  Using lambda or the callback class,
we can send an argument to the function that defines the locators purpose.

NOTE: You need to have a few locators in your scene to work with.
"""
def lOCCallback(loc, *args):
    print loc
    mySelection = cmds.ls(sl=True)
    if len(mySelection) == 0:
        # create a warning
        cmds.warning("select a locator")
    else:
        # fill in the textfield with the name of the control
        myLOCName = mySelection[0]
        cmds.select(clear=True)
        cmds.textField(loc[1], e=True,en=True,tx=myLOCName)
        
"""
A for loop can build all of the buttons we need in one go.
"""

def UI():
    # window name, title and size
    if cmds.window("ArmRig", exists = True):
        cmds.deleteUI("ArmRig")
    myWindow = cmds.window("ArmRig", title = "Arm Rig UI", w = 300, h = 80, mxb = False, mnb = False, s = True)
    # buttons
    labelList = ("Select upperArm Locator", "Select Elbow Locator", "Select Wrist Locator", "Select Wrist End Locator")
    textList = ("upperArmLOC", "ElbowLOC", "WristLOC", "WristEndLOC")
    
    cmds.columnLayout( adjustableColumn=True )
    cmds.text(label="Create Locator", align="left", h=30, fn="boldLabelFont")
    
    for l in range(len(labelList)):
        cmds.separator(h=5,style='none')
        pm.button( label=labelList[l], command = Callback(lOCCallback, [labelList[l], textList[l]] ))
        cmds.separator(h=5,style='none')
        cmds.textField(textList[l], w = 300, en = False, text ="no selection")
    
    cmds.showWindow()

UI() 
    
    

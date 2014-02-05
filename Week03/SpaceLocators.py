#Create multiple locators
import maya.cmds as mc
import random as rand

def makeRandomLocator(count):
    for i in range(count):
        x,y,z = [rand.uniform(0,50),rand.uniform(0,50),rand.uniform(0,50)]
        sp_Locator = mc.spaceLocator (name="lct"+str(i),position=(x,y,z))

makeRandomLocator(10)
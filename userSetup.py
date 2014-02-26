import os
import sys

print sys.path
import maya.cmds as cmds

sys.path.append('C:/Users/Ganapathi K A/Documents/GitHub/Python101')

cmds.evalDeferred('import system.startup')
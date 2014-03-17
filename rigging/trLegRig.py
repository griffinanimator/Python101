# trLegRig.py
import maya.cmds as mc
import data.jsonUtils as jsonUtils
import json
import utils.rig_utils as rig_utils

TITLE = "LegRig"

class LegRig:

    def __init__ (self,*args):
        self.legData = {}

    def install(self,*args):
        pass

import maya.cmds as cmds
# The json module from the python library
import json
# Import our json_utils module
import utils.json_utils as json_utils
reload(json_utils)
# Import the rig_utils module
import utils.rig_utils as rig_utils
reload(rig_utils)
import tempfile


TITLE = "LEG"


# The UI class
class Rig_Leg:

    def __init__(self, *args):
        # Anything in __init__ will be initialized when the module is imported.
    	print 'Rig Leg'
        # Rig_Info will be available to all methods in this module.
        self.Rig_Info = {}

    def rigLeg(self, *args):
        basicFilter = "*.json"
        fileName = cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=2, fm=1, okc='Load')

        # Read the Json file
        # Call on the json_utils readJson method.
        data = json_utils.readJson(fileName)
        info = json.loads( data )

        # Use the generic createJointChain method from rigUtils
        # Notice that I am passing the arguments info and a custom string.
        # I am also storing the returned data to the Rig_Info dictionary.
        self.Rig_Info['fkJoints'] = rig_utils.createJointChain(info, 'fkj')
        self.Rig_Info['ikJoints'] = rig_utils.createJointChain(info, 'ikj')
        self.Rig_Info['rigJoints'] = rig_utils.createJointChain(info, 'rigj')


        # Connect the fk, ik, and rig ikJoints
        for i in range(len(self.Rig_Info['rigJoints'])):
            switchPCon = cmds.parentConstraint(self.Rig_Info['ikJoints'][i], self.Rig_Info['rigJoints'][i], mo=True)
            cmds.parentConstraint(self.Rig_Info['fkJoints'][i], self.Rig_Info['rigJoints'][i], mo=True)
            print switchPCon
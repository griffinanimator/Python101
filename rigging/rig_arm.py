import maya.cmds as cmds
import json
# Import our json_utils module
import utils.json_utils as json_utils
reload(json_utils)
# Import the rig_utils module
import utils.rig_utils as rig_utils
reload(rig_utils)
import tempfile

# The UI class
class Rig_Arm:

    def __init__(self, *args):
    	print 'Rig Arm'
        self.Rig_Info = {}

    def rigArm(self, *args):
        basicFilter = "*.json"
        fileName = cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=2, fm=1, okc='Load')

        # Read the Json file
        # Call on the json_utils readJson method.
        data = json_utils.readJson(fileName)
        info = json.loads( data )

        self.Rig_Info['fkJoints'] = rig_utils.createJointChain(info, 'fkj')
        self.Rig_Info['ikJoints'] = rig_utils.createJointChain(info, 'ikj')
        self.Rig_Info['rigJoints'] = rig_utils.createJointChain(info, 'rigj')

        # Setup the ik rig
        ctrlFile = 'C:/Users/Griffy/Documents/GitHub/Python101/rigging/controls/HandControl.ma'
        rig_utils.importControlObject(ctrlFile)
        self.Rig_Info['ikInfo'] = rig_utils.createIk(self.Rig_Info['ikJoints'])

        # Align the control to the last ik joint
        tmpConstraint = cmds.parentConstraint(self.Rig_Info['ikJoints'][2], 'grp_control', mo=False)
        cmds.delete(tmpConstraint)
        # Rename the control
        cmds.rename('grp_control', 'grp_ikArmCtrl')
        cmds.rename('control', 'ikArmCtrl')
        # Constrain the ikHandle to the control
        cmds.pointConstraint('ikArmCtrl', self.Rig_Info['ikInfo'][0])

        # Make the fk controls

        # Connect the fk, ik, and rig ikJoints
        for i in range(len(self.Rig_Info['rigJoints'])):
        	switchPCon = cmds.parentConstraint(self.Rig_Info['ikJoints'][i], self.Rig_Info['rigJoints'][i], mo=True)
        	cmds.parentConstraint(self.Rig_Info['fkJoints'][i], self.Rig_Info['rigJoints'][i], mo=True)
        	print switchPCon
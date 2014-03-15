""" We made a build joints function in rig_utils as we will be building joints
often.  We can import that function into rig_arm instead of writing the instructions for 
building joints inside Rig_Arm.
"""
import maya.cmds as cmds
# Here we import rig_utils
import utils.rig_utils as rig_utils
# Import json_utils
import utils.json_utils as json_utils

class Rig_Arm:
    
    def __init__(self, *args):
        # New Dictionary
        self.arm_info={}

        #Creates a dictionary
        #self.arm_info={}
        #Creates list that goes in a dictionary that defines placement. Note when creating points think of how they will look placed on a grid.
        #self.jntlytPlmt=(['ljnt_shldr', [0.0,0.0,2.0]], ['ljnt_elbow', [0.0,2.0,4.0]], ['ljnt_wrist', [0.0,0.0,7.0]])
        """ You can just do this """
        filename = "C:/Users/Griffy/Documents/GitHub/Python101/data/locator_info.json"
        self.arm_info['lytInfo'] = json_utils.readJson(filename)
   

    def rig_arm(self, *args):
        #Build joints with a list
        """ Now we can use the rig_utils to build some joints.
        We will store those joints in the arm_info dictionary under a new key.
        We can pass self.arm_info['lytInfo'] as an argument.
        You could also try passing more arguments like a prefix to add tothe joint name
        """
        prefix = "rigJoint"
        self.jointsInfo["orientatition"]='xyz'
        self.arm_info['rigJnts']=rig_utils.buildJoints(self.arm_info['lytInfo'], prefix, self.jointsInfo)
        print "This is what we get back from buildJoints"
        print self.arm_info['rigJnts']

        """ This method is cool because you can now build another joint chain with just one line of code !!"""

        self.jointsInfo["orientatition"]='zyx'
        self.arm_info['fkJnts']=rig_utils.buildJoints(self.arm_info['lytInfo'], "fkJoint")


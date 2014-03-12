import maya.cmds as cmds, json, io
from maya import OpenMaya
import util.file_utils as util
reload(util)
import util.buildLimbs_utils as limb
 
class rig_arm:                                                               
    
    def __init__(self, *args):
        self.loc_info = {
        'lctr_l_arm1': (0, 6.855, 0.048), 
        'lctr_l_arm2': (0, 4.83, -1.237), 
       'lctr_l_arm3':(0, 3.068, -0.423), 
        'lctr_l_armEnd': (0, 2.29, 0.755) 
        }

        self.fileclass = util.fileManager()
        self.limbclass = limb.build_Limbs()


    def build_Locators(self, *args): 
        
        data = self.get_Data() #gets dictionary stored in JSON file

        self.limbclass.build_Locators(data)
        
    def get_Data(self,*args):

        locs_pos = self.writeToJSON(self.loc_info) #locator position
        return locs_pos
        

    def writeToJSON(self, loc_info):
        
         #dictionary to store "default" locator positions
        
        file = "C:\Users\Sarah\Documents\GitHub\Python101\data\Armloc_info.json" 

        if cmds.file(file, q=True, ex = True) is True:
            JSON = self.fileclass.get_JSON(file)
        else:
            self.fileclass.write_JSON(file, self.loc_info)
            JSON = self.fileclass.get_JSON(file)

        return JSON


    def build_Arm(self,*args):
        joints = self.build_Joints() #joints
        ikStuff = self.build_Ik(joints)
        ik = ikStuff[0] #ik group
        pv = ikStuff[1] #polevector
        ikrp = ikStuff[2] #ikhandle
        fk = self.build_Fk(joints) #fk groups

        self.limbclass.build_Arm(ikrp,ik,pv, joints,fk)
        
   
    def build_Joints(self,*args):
        position = self.get_Data()
        cmds.select(d=True) #deselects locator so joints won't be parented to it

        jnt = self.limbclass.build_Joints(position)
        return jnt
        
    
    def build_Fk(self,jnt):
        fkgroup = self.limbclass.build_Fk(jnt)
        
        return fkgroup
            
             
    def build_Ik(self,jnt): 
        buildLimb =  self.limbclass.build_Ik(jnt)
        grp = buildLimb[0]
        pv_ctrl = buildLimb[1]
        ikrpName = buildLimb[2]

        
        return grp, pv_ctrl,ikrpName
        
        
    def poleVectorPos(self,jnt):

        loc = self.limbclass.poleVectorPos(jnt)

        return loc

                
        

    #build_Locators() 
    #build_Joints()       

         
    

    
    

                                                                            

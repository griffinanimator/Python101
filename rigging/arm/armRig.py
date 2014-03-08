import maya.cmds as cmds
import rigging.tools.awMirrorObjectsTool as awMOTInstance
import pymel as pm

class awArmCreator():
    def __init__(self):
        self.armHierarchy = {'L_clavicle':{'pos':[0.196, 12.375, -0.036], 'children':['L_shoulder']},
                             'L_shoulder':{'pos':[1.115, 12.517, -0.42], 'children':['L_elbow']},
                             'L_elbow':{'pos':[3.044, 12.517, -0.581], 'children':['L_hand']},
                             'L_hand':{'pos':[5.327, 12.50, 0], 'children':[]}}
        self.armLocators = []
        self.armJoints = []
        self.ikJoints = []
        self.fkJoints = []
        
        
    def UI_(self, *args):
        if cmds.window('awArmCreateUI', exists=True):
            cmds.deleteUI('awArmCreateUI')
        cmds.window('awArmCreateUI', w=300, h=300, sizeable=True)
        cmds.columnLayout()
        cmds.button('place lox', c=self.awTestIfArmExists)
        cmds.button('place joints', c=self.awCreateArmJoints)
        cmds.button('broken hi', c=self.awCreateBrokenHierarchy)
        cmds.button('connect', c=self.awConnectArmTripleChain)
        cmds.button('group', c=self.awCreateBrokenHierarchyPartTwo)
        cmds.button('mirror', c=self.awMirrorArmChain)
        cmds.button('create ik', c=self.createIKChain)
        
        cmds.showWindow('awArmCreateUI')
    #####Locators
    def awPlaceArmLocators(self, name, parent=None, *args):
        #self.armLocators = []
        locName = ('JntLoc_' + str(name))
        makeLoc = cmds.spaceLocator(n=locName, p=(0, 0, 0))[0]
        self.armLocators.append(makeLoc)
        locMove = cmds.move(self.armHierarchy[name]['pos'][0], self.armHierarchy[name]['pos'][1],
                            self.armHierarchy[name]['pos'][2], makeLoc, absolute=True)
        if parent:
            cmds.parent(locName, parent)
        for child in self.armHierarchy[name]['children']:
            self.awPlaceArmLocators(child, parent=locName)

    def awCreateArmLocators(self, *args):
        self.awPlaceArmLocators('L_clavicle')

    def awTestIfArmExists(self, *args):
        if cmds.objExists('JntLoc_L_clavicle'):
            cmds.warning('Arm locators already exist, please start over')
        else:
            self.awCreateArmLocators()
    #####Joints
    def awPlaceArmJoints(self, *args):
        print self.armLocators
        #self.armJoints = []
        for loc in self.armLocators:
            cmds.select(d=True)
            jntName = loc.replace('JntLoc_', 'bn_')
            makeJnt = cmds.joint(n=jntName, p=(0, 0, 0))
            self.armJoints.append(makeJnt)
            parentGet = cmds.listRelatives(loc, p=True)
            if parentGet:
                cmds.parent(makeJnt, parentGet[0].replace('JntLoc_', 'bn_'))
            jntConstraint = cmds.parentConstraint(loc, makeJnt)
            cmds.delete(jntConstraint)
    #####Create Broken Hierarchy
    def awCreateBrokenHierarchy(self, *args):
        #cmds.select('bn_L_shoulder')
        ##Po = parent only, so I don't have to go through additional steps of pickwalking down and deleting children and moving back up
        cmds.duplicate('bn_L_shoulder', n='be_L_clavicleEnd', po=True)
        cmds.setAttr('be_L_clavicleEnd.radius', 0.5)
        cmds.parent('bn_L_shoulder', w=True)
        ###When you come back to this, orient the joints correctly and don't forget to orient the clavicle end joint 
        ###to zero it out, as well as the wrist. You'll have to orient both chains. 

    ####Create IK Chain
    def createIKChain(self, name, *args):
        ikChain = cmds.duplicate('bn_L_shoulder', n='jDrvIK_L_shoulder')
        cmds.select(hi=True)
        ikChainSel = cmds.ls(sl=1)
        self.ikJoints.append(ikChainSel)
        for jnt in self.ikJoints:
            cmds.select(d=True)
            jntIKName = jnt.replace('bn_', 'jDrvIK')
            cmds.joint(e=True, n=jntIKName)
        print 'this is the list' + self.ikJoints
        
            
            
            
            
    
    
    
    
    def awConnectArmTripleChain(self, *args):
        cmds.select('jDrvIK_L_shoulder', 'jDrvFK_L_shoulder', 'bn_L_shoulder')
        chainSel = cmds.ls(sl=1)
        cmds.orientConstraint(chainSel)
        cmds.select('jDrvIK_L_elbow', 'jDrvFK_L_elbow', 'bn_L_elbow')
        elbowSel = cmds.ls(sl=1)
        cmds.orientConstraint(elbowSel)
    def awCreateBrokenHierarchyPartTwo(self, *args):
        newGroup = cmds.group('bn_L_shoulder', 'jDrvIK_L_shoulder', 'jDrvFK_L_shoulder', n='null_L_shoulder', r=True)

    def awMirrorArmChain(self, *args):
        awMOT = awMOTInstance.awMirrorObjects()
        awMOT.awMirrorObjects()
        
        

        
    def awCreateArmJoints(self, *args):
        self.awPlaceArmJoints('L_clavicle')
 
        
        
        
start = awArmCreator()
start.UI_()

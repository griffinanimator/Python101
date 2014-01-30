'''
Arm - Assignment Week 2
Alex Widener 
I got as far as I could so far, but I've got another 4 days before this is due.
I got in the controls and the constraints, but didn't finish setting up the IK/FK switch. Right now,
the default IK weight is on. 

Really sleepy. I'll get back to it in a day or two. 
I'd love any critiques until then, though. E-mail is alexwidener@gmail.com
'''


import maya.cmds as cmds

class armRigger():
    
    def __init__(self):
        self.hierarchy = {'l_clavicle':{'pos':[1.115, 12.517, -0.42],
                                        'children':['l_shoulder']},
                          'l_shoulder':{'pos':[2.51, 12.855, -1.145],
                                        'children':['l_elbow']},
                          'l_elbow':{'pos':[5.548, 12.881, -1.771],
                                     'children':['l_wrist']},
                          'l_wrist':{'pos':[9.24, 12.993, -1.251],
                                     'children':[]}}
        self.locators = []
        self.joints = []
        self.controls = []


    def awPlaceLocs(self, name, parent=None, *args):
        locName = ('JntLoc_' + str(name))
        makeLoc = cmds.spaceLocator(n=locName, p=(0, 0, 0))[0]
        
        self.locators.append(makeLoc)
        locMove = cmds.move(self.hierarchy[name]['pos'][0], self.hierarchy[name]['pos'][1],
                            self.hierarchy[name]['pos'][2], makeLoc, absolute=True)
        if parent:
            cmds.parent(locName, parent)
        for child in self.hierarchy[name]['children']:
            self.awPlaceLocs(child, parent=locName)

    def awCreateLocs(self, *args):
        self.awPlaceLocs('l_clavicle')
        cmds.parent('JntLoc_l_clavicle', 'locators01')
        
    def awGroups(self, *args):
        myGroup = cmds.group(n='arm01', em=1, w=1)
        #So I could write this as setAttr 'arm01.t' to cut down the lines, but apparently when you 
        #do the entire translation in one swoop, it won't hide them from ChannelBox.
        cmds.setAttr('arm01.tx', lock=True, k=False, cb=False)
        cmds.setAttr('arm01.ty', lock=True, k=False, cb=False)
        cmds.setAttr('arm01.tz', lock=True, k=False, cb=False)
        cmds.setAttr('arm01.rx', lock=True, k=False, cb=False)
        cmds.setAttr('arm01.ry', lock=True, k=False, cb=False)
        cmds.setAttr('arm01.rz', lock=True, k=False, cb=False)
        cmds.setAttr('arm01.sx', lock=True, k=False, cb=False)
        cmds.setAttr('arm01.sy', lock=True, k=False, cb=False)
        cmds.setAttr('arm01.sz', lock=True, k=False, cb=False)
        for i in range(5):
            cmds.duplicate(myGroup)
        cmds.rename('arm02', 'joints01')
        cmds.rename('arm03', 'locators01')
        cmds.rename('arm04', 'ikHandles01')
        cmds.rename('arm05', 'fkControls01')
        cmds.rename('arm06', 'ikControls01')
        #When you use the parent command, if you list it like this, it will parent everything to the 
        #final object
        cmds.parent('joints01', 'locators01', 'ikHandles01', 'fkControls01', 'ikControls01', 'arm01')

    def _showUI(self, *args):
        if cmds.window('awArmRigger', exists=True):
            cmds.deleteUI('awArmRigger')
        cmds.window('awArmRigger', wh=(200, 300), mb=True, resizeToFitChildren=True)
        cmds.menuBarLayout()
        cmds.menu(label='File')
        cmds.menuItem(label='Close', c=closeUI)
        cmds.menuItem(label='Website', c= lambda z:mc.showHelp('http://www.alexwidener.com', absolute=True))
        cmds.formLayout()
        cmds.rowColumnLayout(nc=2, columnWidth=[(1, 200), (2, 95)], rowSpacing=[1, 5])
        cmds.text('Create proper group structure', align='left')
        cmds.button('groups', c=self.awGroups)
        cmds.text('Make locators. Move locs as needed', align='left')
        cmds.button('loc', c=self.awCreateLocs)
        cmds.text('Note: Move from Parent to Child', align='left')
        cmds.separator(h=15, style='none')
        cmds.text('Press joint button to generate joints', align='left')
        cmds.button('joint', c=self.awPlaceJoints)
        cmds.text('Press to orient joints XYZ', align='left')
        cmds.button('orient xyz', c=self.awOrientJoints)
        cmds.text('Create FK Controls', align='left')
        cmds.button('FK Controls', c=self.awCreateFKControls)
        cmds.text('Create IK Controls', align='left')
        cmds.button('IK Controls', c=self.awCreateIK)
        cmds.showWindow('awArmRigger')
        

    def awPlaceJoints(self, *args):
        print self.locators
        for loc in self.locators:
            jntName = loc.replace('JntLoc_', 'bn_')
            makeJnt = cmds.joint(name=jntName, p=(0, 0, 0))
            cmds.parent(makeJnt, w=True)
            self.joints.append(makeJnt)
            parentGet = cmds.listRelatives(loc, p=True)
            if parentGet:
                cmds.parent(makeJnt, parentGet[0].replace('JntLoc_', 'bn_'))
            jntConstraint = cmds.parentConstraint(loc, makeJnt)
            cmds.delete(jntConstraint)

    def awCreateJoints(self, *args):
        self.awPlaceJoints()

    def awOrientJoints(self, *args):
        cmds.setAttr('locators01.visibility', 0)
        cmds.select('bn_l_clavicle')
        #have to call the joint command and put it into edit mode to edit the orientation
        cmds.joint(e=True, oj='xyz', sao='yup', ch=1, zso=1)
        #move bones to joints group. Can't get it to work automatically in awCreateJoints for some reason
        cmds.parent('bn_l_clavicle', 'joints01')
        
    def awCreateFKControls(self, *args):
        cmds.select(cl=True)
        cmds.select('bn_l_clavicle', 'bn_l_shoulder', 'bn_l_elbow', 'bn_l_wrist', tgl=True)
        boneSelection = cmds.ls(sl=1)
        for bn in boneSelection:
            fkControlName = bn.replace('bn_', 'FK_')
            fkControlGrpName = bn.replace('bn_', 'FKGrp_')
            makeControl = cmds.circle(n=fkControlName, c=(0, 0, 0), nr=(1, 0, 0), sw=360, r=1, d=3, ut=0, tol=0.01, s=8, ch=0)
            grpControl = cmds.group(n=fkControlGrpName)
        cmds.parent('FKGrp_l_clavicle', 'fkControls01')
        
        cmds.pointConstraint('bn_l_clavicle', 'FKGrp_l_clavicle', offset=(0, 0, 0), weight=1)
        cmds.orientConstraint('bn_l_clavicle', 'FKGrp_l_clavicle', offset=(0, 0, 0), weight=1)
        cmds.delete('FKGrp_l_clavicle_pointConstraint1', 'FKGrp_l_clavicle_orientConstraint1')
        #cmds.pointConstraint('FK_l_clavicle', 'bn_l_clavicle', offset=(0, 0, 0), weight=1)
        cmds.orientConstraint('FK_l_clavicle', 'bn_l_clavicle', offset=(0, 0, 0), weight=1)
        
        cmds.pointConstraint('bn_l_shoulder', 'FKGrp_l_shoulder', offset=(0, 0, 0), weight=1)
        cmds.orientConstraint('bn_l_shoulder', 'FKGrp_l_shoulder', offset=(0, 0, 0), weight=1)
        cmds.delete('FKGrp_l_shoulder_pointConstraint1', 'FKGrp_l_shoulder_orientConstraint1')
        #cmds.pointConstraint('FK_l_shoulder', 'bn_l_shoulder', offset=(0, 0, 0), weight=1)
        cmds.orientConstraint('FK_l_shoulder', 'bn_l_shoulder', offset=(0, 0, 0), weight=1)
        
        cmds.pointConstraint('bn_l_elbow', 'FKGrp_l_elbow', offset=(0, 0, 0), weight=1)
        cmds.orientConstraint('bn_l_elbow', 'FKGrp_l_elbow', offset=(0, 0, 0), weight=1)
        cmds.delete('FKGrp_l_elbow_pointConstraint1', 'FKGrp_l_elbow_orientConstraint1')
        #cmds.pointConstraint('FK_l_elbow', 'bn_l_elbow', offset=(0, 0, 0), weight=1)
        cmds.orientConstraint('FK_l_elbow', 'bn_l_elbow', offset=(0, 0, 0), weight=1)
        
        cmds.pointConstraint('bn_l_wrist', 'FKGrp_l_wrist', offset=(0, 0, 0), weight=1)
        cmds.orientConstraint('bn_l_wrist', 'FKGrp_l_wrist', offset=(0, 0, 0), weight=1)
        cmds.delete('FKGrp_l_wrist_pointConstraint1', 'FKGrp_l_wrist_orientConstraint1')
        #cmds.pointConstraint('FK_l_wrist', 'bn_l_wrist', offset=(0, 0, 0), weight=1)
        cmds.orientConstraint('FK_l_wrist', 'bn_l_wrist', offset=(0, 0, 0), weight=1)

        cmds.parent('FKGrp_l_shoulder', 'FK_l_clavicle')
        cmds.parent('FKGrp_l_elbow', 'FK_l_shoulder')
        cmds.parent('FKGrp_l_wrist', 'FK_l_elbow')

        ''' This works, but didn't fully do what I wanted it to do for this.
        for jnt in self.joints:
            fkControlName = jnt.replace('bn_', 'FK_')
            makeControl = cmds.circle(n=fkControlName, c=(0, 0, 0), nr=(1, 0, 0), sw=360, r=1, d=3, ut=0, tol=0.01, s=8, ch=0)
            parentGetJnt = cmds.listRelatives(jnt, p=True)
            if parentGetJnt:
                cmds.parent(makeControl, parentGetJnt[0].replace('bn_', 'FK_'))
        cmds.parent('FK_l_clavicle', 'fkControls01')
        '''
    def awCreateIK(self, *args):
        cmds.ikHandle(n='l_arm_ikHandle', sj='bn_l_shoulder', ee='bn_l_wrist', w=1, sol='ikRPsolver')
        cmds.parent('l_arm_ikHandle', 'ikHandles01')
        makeIKBox = self.awCreateBox()
        cmds.rename('box_curve01', 'IK_l_arm')
        cmds.rename('boxGrp_curve01', 'IKGrp_l_arm')
        makeMainBox = self.awCreateMainControlBox()
        cmds.parentConstraint('l_arm_ikHandle', 'IKGrp_l_arm')
        cmds.delete('IKGrp_l_arm_parentConstraint1')
        cmds.pointConstraint('IK_l_arm', 'l_arm_ikHandle')
        cmds.parent('IKGrp_l_arm', 'ikControls01')

    def awCreateBox(self, *args):
        points = [(0, 1, 1), (0, 1, -1), (0, -1, -1), (0, -1, 1), (0, 1, 1)]
        
        makeBoxCurve = cmds.curve(ep=points, d=1, k=[0,1,2,3,4], name='box_curve01')
        cmds.group(n='boxGrp_curve01')

    def awCreateMainControlBox(self, *args):
        points = [(3, 11, 0), (3, 6, 0), (6, 6, 0), (6, 11, 0), (3, 11, 0)]
        makeMainControlCurve = cmds.curve(ep=points, d=1, k=[0,1,2,3,4], name='main_control_01')
        cmds.setAttr('main_control_01.t', lock=True, k=False, cb=False)
        cmds.setAttr('main_control_01.r', lock=True, k=False, cb=False)
        cmds.setAttr('main_control_01.s', lock=True, k=False, cb=False)
        cmds.addAttr(at='double', shortName = 'IKFK', longName = 'IKFKSwitch', defaultValue=0, minValue=0, maxValue=10, k=1)
   
    def createSDKs(self, *args):
        pass
        



        
    def awNotesDoNotCall(self, *args):
        pass
        '''
        
        '''


        
        

start = armRigger()
start._showUI()

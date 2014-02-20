import maya.cmds as cmds
from maya import OpenMaya

class awQuickRigger():
    def __init__(self):
        self.hierarchy = {'root01':{'pos':[0, 8.994, 0], 'children': ['spine', 'pelvis']},
                          'spine':{'pos':[0, 9.467, -0.029], 'children':['spineB']},
                          'spineB':{'pos':[0, 9.602, -0.047], 'children': ['spineC']},
                          'spineC':{'pos':[0, 9.939, -0.027], 'children':['spineD']},
                          'spineD':{'pos':[0, 10.412, -0.013], 'children':['spineE']},
                          'spineE':{'pos':[0, 10.885, -0.018], 'children':['spineF']},
                          'spineF':{'pos':[0, 11.356, -0.049], 'children':['spineG']},
                          'spineG':{'pos':[0, 11.826, -0.111], 'children':['spineH']},
                          'spineH':{'pos':[0, 12.293, -0.183], 'children':['neck', 'L_clavicle']},
                          'neck':{'pos':[0, 12.73, -0.182], 'children':['headA']},
                          'headA':{'pos':[0, 13.631, 0.017], 'children':['jawA', 'headB', 'L_eye']},
                          'headB':{'pos':[0, 17.028, 0.769], 'children':[]},
                          'jawA':{'pos':[0, 14.302, -0.359], 'children':['jawB']},
                          'jawB':{'pos':[0, 13.419, 1.421], 'children':[]},
                          'L_eye':{'pos':[0.395, 14.903, 0.9], 'children':[]},
                          'L_clavicle':{'pos':[0.196, 12.375, -0.036], 'children':['L_shoulder']},
                          'L_shoulder':{'pos':[1.115, 12.517, -0.42], 'children':['L_elbow']},
                          'L_elbow':{'pos':[3.044, 12.517, -0.581], 'children':['L_hand']},
                          'L_hand':{'pos':[5.327, 12.50, 0], 'children':['L_thumbA', 'L_indexA', 'L_middleA', 'L_ringCup', 'L_PinkyCup']},
                          'L_thumbA':{'pos':[5.575, 12.774, -0.125], 'children':['L_thumbB']},
                          'L_thumbB':{'pos':[5.89, 12.385, 0.058], 'children':['L_thumbC']},
                          'L_thumbC':{'pos':[6.1, 12.348, 0.162], 'children':['L_thumbD']},
                          'L_thumbD':{'pos':[6.368, 12.289, 0.292], 'children':[]},
                          'L_indexA':{'pos':[6.297, 12.597, -0.178], 'children':['L_indexB']},
                          'L_indexB':{'pos':[6.578, 12.604, -0.157], 'children':['L_indexC']},
                          'L_indexC':{'pos':[6.821, 12.598, -0.141], 'children':['L_indexD']},
                          'L_indexD':{'pos':[7.055, 12.598, -0.125], 'children':[]},
                          'L_middleA':{'pos':[6.315, 12.656, -0.384], 'children':['L_middleB']},
                          'L_middleB':{'pos':[6.621, 12.658, -0.377], 'children':['L_middleC']},
                          'L_middleC':{'pos':[6.864, 12.652, -0.371], 'children':['L_middleD']},
                          'L_middleD':{'pos':[7.158, 12.636, -0.364], 'children':[]},
                          'L_ringCup':{'pos':[5.619, 12.569, -0.587], 'children':['L_ringA']},
                          'L_ringA':{'pos':[6.295, 12.648, -0.558], 'children':['L_ringB']},
                          'L_ringB':{'pos':[6.544, 12.662, -0.561], 'children':['L_ringC']},
                          'L_ringC':{'pos':[6.826, 12.644, -0.566], 'children':['L_ringD']},
                          'L_ringD':{'pos':[7.111, 12.623, -0.57], 'children':[]},
                          'L_PinkyCup':{'pos':[5.653, 12.511, -0.736], 'children':['L_pinkyA']},
                          'L_pinkyA':{'pos':[6.279, 12.625, -0.739], 'children':['L_pinkyB']},
                          'L_pinkyB':{'pos':[6.449, 12.619, -0.745], 'children':['L_pinkyC']},
                          'L_pinkyC':{'pos':[6.634, 12.612, -0.752], 'children':['L_pinkyD']},
                          'L_pinkyD':{'pos':[6.889, 12.593, -0.762], 'children':[]},
                          'pelvis':{'pos':[0, 8.994, -0.01], 'children':['L_thigh']},
                          'L_thigh':{'pos':[0.833, 8.994, -0.097], 'children':['L_knee']},
                          'L_knee':{'pos':[0.833, 4.973, 0.26], 'children':['L_ankle']},
                          'L_ankle':{'pos':[0.833, 0.917, -0.002], 'children':['L_ball']},
                          'L_ball':{'pos':[0.833, 0.479, 1.155], 'children':['L_Toe']},
                          'L_Toe': {'pos': [0.833, 0, 2.114], 'children': []}}
        self.locators = []
        self.joints = []
        self.controls = []
        self.locPos = []

    def UI_(self, *args):
        if cmds.window('AlexRigger', exists=True):
                cmds.deleteUI('AlexRigger')
        cmds.window('AlexRigger', w=200, h=600, t='AlexRigger', s=True)
        cmds.menuBarLayout()
        cmds.menu('File')
        cmds.menuItem('About')
        cmds.menuItem('Website')
        column = cmds.columnLayout('myColumn', adj=True)
        cmds.separator(style='none')
        tabs = cmds.tabLayout(imw=5, imh=5)
        childOne = cmds.rowColumnLayout(nc=2)
        cmds.text('Arm Setup', align='left')
        cmds.separator(h=15, style='none')
        cmds.text('Place locators and then move to desired position', align='left')
        cmds.button('Place locators', c= self.awCreateLocators)
        cmds.text('Build joints and put into a hierarchy', align='left')
        cmds.button(label='Build joints', c=self.awCreateJoints)
        cmds.text('Click to build IK/FK Blend setup', align='left')
        cmds.button('Build Controls', c=self.awDoOrientJoints)
        cmds.text('Set up joint chains for twist', h=50, align='left')
        cmds.separator(h=15, style='none')
        myTextFieldButtonGrp = cmds.textFieldButtonGrp(l='Desired number of joints', bl='Create joints', bc=self.jointChainResolution_go)

        #cmds.checkBoxGrp( numberOfCheckBoxes=3, label='IK/FK/Blend', labelArray3=['IK', 'FK', 'Both'] )
        cmds.separator(h=15, style='none')

        cmds.separator(h=200, style='none')
        cmds.separator(h=200, style='none')
        cmds.text('Leg Setup', align='left')
        cmds.separator(h=15, style='none')
        cmds.separator(h=200, style='none')
        cmds.separator(h=200, style='none')
        cmds.text('Spine Setup', align='left')
        cmds.separator(h=15, style='none')
        cmds.separator(h=200, style='none')
        cmds.text('Setup Twist Joints', align='center')
        cmds.separator(h=15, style='none')
        cmds.text('Select joint to split, then type in number, then press create', align='center')
        cmds.separator(h=15, style='none')
        cmds.separator(style='none')
        cmds.button()
        cmds.button()
        cmds.setParent('..')
        childTwo = cmds.rowColumnLayout(nc=2)
        #BELOW HERE FOR FACE LAYOUT
        cmds.text('Place locator in the center of eyeball', align='left')
        cmds.text('Name locator l_eyeballCenter')
        cmds.text('Select vertices and push this button', align='left')
        cmds.button('Create eyelid bones', c=self.createEyelidBones)
        cmds.text('Renaming eyelids', h=50, align='left')
        cmds.separator(h=50, style='none')
        cmds.text('Select bones from nose to ear', align='left')
        cmds.separator(h=15, style='none')
        cmds.textScrollList("Label eyelid joints", h=50, a=["_l_upper", "_l_lower", "_r_upper", "_r_lower"])
        cmds.button('Rename', h=50)
        cmds.text('Duplicate center locator and rename it l_eyeUpVec_Loc')
        cmds.separator(h=15, style='none')
        cmds.text('Run to get uParam value', align='left')
        cmds.button('Get uParam', c=self.doTheUParamAndDagPath)
        cmds.text('Run to connect uParam to locators', align='left')
        cmds.button('connect uParam')
        cmds.button('curve test', c=self.curveTest)
        cmds.button()
        cmds.button()
        cmds.setParent('..')
        cmds.tabLayout(tabs, edit=True, tabLabel=((childOne, 'Body'), (childTwo, 'Face')) )

        
        cmds.showWindow('AlexRigger')

    def curveTest(self, *args):
        locatorPos = cmds.ls(sl=1)
        for loc in locatorPos:
            pos = cmds.getAttr(loc + '.translate')
            print pos
            self.locPos.append(pos)
        print self.locPos
        for myLocator in locatorPos:
            cmds.curve(d=1, p=myLocator, k=[0,1,2,3,4,5,6,7,8])

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

    def awCreateLocators(self, awGrouper):
        self.awGrouper()
        self.awPlaceLocs('root01')
        cmds.parent('JntLoc_root01', 'locators01')

    def awGrouper(self, *args):
        myGroup=cmds.group(n='arm01', em=1, w=1)
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
        cmds.parent('joints01', 'locators01', 'ikHandles01', 'fkControls01', 'ikControls01', 'arm01')

    def awOrientJoints(self, *args):
        cmds.setAttr('locators01.visibility', 0)
        cmds.select('bn_l_clavicle')
        cmds.joint(e=True, oj='xyz', sao='yup', ch=1, zso=1)
        cmds.parent('bn_l_clavicle', 'joints01')
        cmds.select(cl=True)

    def awDoOrientJoints(self, *args):
        self.awOrientJoints()
        self.selectEndJoints()
        self.awCorrectEndJoint()
        
    def awCreateJoints(self, *args):
        self.awPlaceJoints()

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

    def awCorrectEndJoint(self, *args):
        sel = cmds.ls(sl=1, type='joint')
        for allJnts in sel:
            if cmds.objExists(allJnts + '_aimConstraint*'):
                cmds.delete(allJnts + '_aimConstraint*')
            ori_x = cmds.getAttr(allJnts + '.rx')
            ori_y = cmds.getAttr(allJnts + '.ry')
            ori_z = cmds.getAttr(allJnts + '.rz')
            cmds.setAttr(allJnts + '.jointOrientX', ori_x)
            cmds.setAttr(allJnts + '.jointOrientY', ori_y)
            cmds.setAttr(allJnts + '.jointOrientZ', ori_z)
            cmds.setAttr(allJnts + '.rx', 0)
            cmds.setAttr(allJnts + '.ry', 0)
            cmds.setAttr(allJnts + '.rz', 0)

    def selectEndJoints(self, *args):
        cmds.select('bn_l_wrist', tgl=True)
    
    def jointChainResolution_go():
        selectSourceJoint = cmds.ls(sl=1)
        cmds.select(hi=True)
        if size(selectSourceJoint) < 2:
            cmds.warning('Must select a bone')
        else:
            cmds.pickWalk(d=down)
            selChild[0] = cmds.ls(sl=1)
            cmds.select(selChild[0])
            childJnt_tx = cmds.getAttr(selChild[0] + '.tx')
            sourceJnt_radius = cmds.getAttr(selChild[0] + '.radius')
            cmds.pickWalk(d=up)
            getTextButtonGrp_value = cmds.textFieldButtonGrp(q=True, text=myTextFieldButtonGrp)
            
            if (getTextButtonGrp_value < 2):
                    cmds.warning('Must create at least one segment')
            else:
                    for i in range(getTextButtonGrp_value):
                            xpos = childJnt_tx/getTextButtonGrp_value
                            myJoint = cmds.joint(rad = sourceJnt_radius, o=(0, 0, 0))
                            cmds.move(myJoint, (xpos, 0, 0), r=True, ls=True)
            lastJoint[0] = cmds.ls(sl=1)
            cmds.parent(selChild[0], lastJoint[0])
            cmds.select(cl=True)

                
    def createEyelidBones(vtx, self, *args):
        center = 'r_eyeCenter'
        vtx = cmds.ls(sl=1, fl=1)

        for v in vtx:
            cmds.select(cl=1)
            jnt=cmds.joint()
            pos = cmds.xform(v, q=1, ws=1, t=1)
            cmds.xform(jnt, ws=1, t=pos)
            posC = cmds.xform(center, q=1, ws=1, t=1)
            cmds.select(cl=1)
            jntC = cmds.joint()
            cmds.xform(jntC, ws=1, t=posC)
            cmds.parent(jnt, jntC)
            cmds.joint(jntC, e=1, oj='xyz', secondaryAxisOrient='yup', ch=1, zso=1)

    def uParamCurveNodes(self, *args):

        sel = cmds.ls(sl=1)
        crv = "R_upLidHigh_CRV"
        for s in sel:
            pos = cmds.xform(s, q=1, ws=1, t=1)
            u = getUParam(pos, crv)
            name = s.replace('_LOC', '_PCI')
            pci = cmds.createNode('pointOnCurveInfo', n=name)
            cmds.connectAttr(crv + '.worldSpace', pci + '.inputCurve')
        cmds.setAttr(pci + '.parameter', u)
        cmds.connectAttr(pci + '.position', s + '.t')
        
    def doTheUParamAndDagPath(self, *args):
        self.getUParam()
        self.getDagPath()

    def getUParam( pnt = [], crv = None):

        point = OpenMaya.MPoint(pnt[0],pnt[1],pnt[2])
        curveFn = OpenMaya.MFnNurbsCurve(getDagPath(crv))
        paramUtill=OpenMaya.MScriptUtil()
        paramPtr=paramUtill.asDoublePtr()
        isOnCurve = curveFn.isPointOnCurve(point)
        if isOnCurve == True:
        
            curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
        else :
            point = curveFn.closestPoint(point,paramPtr,0.001,OpenMaya.MSpace.kObject)
            curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
    
        param = paramUtill.getDouble(paramPtr)  
        return param

    def getDagPath( objectName):
    
        if isinstance(objectName, list)==True:
            oNodeList=[]
            for o in objectName:
                selectionList = OpenMaya.MSelectionList()
                selectionList.add(o)
                oNode = OpenMaya.MDagPath()
                selectionList.getDagPath(0, oNode)
                oNodeList.append(oNode)
            return oNodeList
        else:
            selectionList = OpenMaya.MSelectionList()
            selectionList.add(objectName)
            oNode = OpenMaya.MDagPath()
            selectionList.getDagPath(0, oNode)
            return oNode

start = awQuickRigger()
start.UI_()

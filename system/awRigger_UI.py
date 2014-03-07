import maya.cmds as cmds
import rigging.awLegLocSetup as awLegLocSetupInstance
import rigging.spine.spineLocSetup as awSpineLocSetupInstance
import rigging.tools.lraOffTool as lraOffToolInstance
import rigging.awGrouper as awGroupInstance
import rigging.tools.awOrientJointTool as awOrientJointInstance
import sys

class alexWidenerRigger_UI:
    def __init__(self, *args):
        #http://docs.python.org/2/tutorial/classes.html
        print 'In alexWidenerRigger_UI'
        '''Create a dictionary to store elements
        This will allow us to access these elements later'''
        self.UIElements = {}
        self.spineLocators = []
        self.spineJoints = []

    def ui(self, *args):
        windowName = 'alexwidenerautorigger'
        if cmds.window(windowName, exists=True):
            cmds.deleteUI(windowName)
        windowWidth=200
        windowHeight=500
        buttonWidth=100
        buttonHeight=25
        self.UIElements["window"] = cmds.window(windowName,
                                           width=windowWidth,
                                           height=windowHeight,
                                           title="Alex Widener Rigger UI",
                                           sizeable=True)
        self.UIElements["menu"] = cmds.menuBarLayout()
        self.UIElements["menuItemFile"] = cmds.menu('File')
        self.UIElements["menuItemClose"] = cmds.menuItem('Close', c=self.closeWindow)

        self.UIElements["ToolsAtTheTopLayout"] = cmds.rowColumnLayout(nc=2,
                                                                      w=windowWidth,
                                                                      h=windowHeight)
        self.UIElements["selectHierarchyButton"] =cmds.button(label='Select Hierarchy',
                                                              w=buttonWidth,
                                                              h=buttonHeight,
                                                              c=self.selectHiTool)
        self.UIElements["LRA On Tool"]=cmds.button(label='LRA ON',
                                                   w=buttonWidth,
                                                   h=buttonHeight)
        self.UIElements["LRA ALL OFF TOOL"] = cmds.button(label='LRA ALL OFF',
                                          w=buttonWidth,
                                          h=buttonHeight,
                                          c=self.lraOffTool)
        cmds.separator(p=self.UIElements["ToolsAtTheTopLayout"], h=15)
        self.UIElements["Orient Joints Tool"] = cmds.button(label='Orient Joints XYZ',
                                                            w=buttonWidth,
                                                            h=buttonHeight,
                                                            c=self.loadAwOrientJointTool)
#
#                                            
#        self.UIElements["guiRowColumnLayout1"] = cmds.rowColumnLayout(nc=2,
#                                                       w=windowWidth,
#                                                       h=windowHeight,
#                                                       bgc=[0.2, 0.2, 0.2])

        #cmds.separator(p=self.UIElements["guiFlowLayout1"])

        cmds.text('Legs', align='left', p=self.UIElements["ToolsAtTheTopLayout"])
        cmds.separator(p=self.UIElements["ToolsAtTheTopLayout"], h=15)

        self.UIElements["awGrouperButton"] = cmds.button(label='create groups',
                                                         w=buttonWidth,
                                                         h=buttonHeight,
                                                         p=self.UIElements["ToolsAtTheTopLayout"],
                                                         c=self.loadAwGrouper)
        cmds.text('Place the locators. Move from parent to child. Do not rotate.', p=self.UIElements["ToolsAtTheTopLayout"])
        cmds.separator(h=15, p=self.UIElements["ToolsAtTheTopLayout"])
        self.UIElements["locatorLegButton"] = cmds.button(label='place locators for legs',
                                                          w=buttonWidth,
                                                          h=buttonHeight,
                                                          p=self.UIElements["ToolsAtTheTopLayout"],
                                                          bgc=[0, 0, 0],
                                                          c=self.loadAwLegLocSetup)
        cmds.separator(h=15, p=self.UIElements["ToolsAtTheTopLayout"])
        
        cmds.text('Spine', align='left', p=self.UIElements["ToolsAtTheTopLayout"])
        self.UIElements["spineLocators"] = cmds.button(label='spineLocators',
                                                       w=buttonWidth,
                                                       h=buttonHeight,
                                                       p=self.UIElements["ToolsAtTheTopLayout"],
                                                       c=self.loadAwSpineLocSetup)
        self.UIElements["spineJoints"] = cmds.button(label='createJointsforSpine',
                                          w=buttonWidth,
                                          h=buttonHeight,
                                          p=self.UIElements["ToolsAtTheTopLayout"],
                                          c=self.loadAwSpineJntSetup)
        self.UIElements["layout_button"] = cmds.button(label='layout',
                                           w=buttonWidth, 
                                           h=buttonHeight,
                                           p=self.UIElements["ToolsAtTheTopLayout"],
                                           c=self.createLayout)

                                           
        cmds.showWindow(windowName)
#Notes before bed - Going to need to make sure these individual buttons can call the individual functions within the other scripts. 
#right now, for the spine one, it's going to call the entire class, but it's not going to call the functions that I'm going to need individually. 
#Look into that.

    def closeWindow(self, *args):
        if cmds.window('alexwidenerautorigger', exists=True):
            cmds.deleteUI('alexwidenerautorigger')
    def createLayout(self, *args):
        print 'lyt'
        
    def loadAwLegLocSetup(self, *args):
        awLegLoc = awLegLocSetupInstance.awLegLoc()
        awLegLoc.awCreateLegLocs()
        
    def loadAwSpineLocSetup(self, *args):
        awSpineLoc = awSpineLocSetupInstance.awSpineCall()
        awSpineLoc.seeIfJoints01Exists()

    def loadAwSpineJntSetup(self, *args):
        awSpineJnt = awSpineLocSetupInstance.awSpineCall()
        awSpineJnt.awCreateJoints()

    def loadAwGrouper(self, *args):
        if cmds.objExists('character01'):
            cmds.warning('Please remove character01 and subsequent groups')
        else:
            awGroup = awGroupInstance.awMasterGroupCreator()
        cmds.select(cl=True)

    def lraOnTool(self, *args):
        pass
        
    def selectHiTool(self, *args):
        cmds.select(hi=True)

    def lraOffTool(self, *args):
        sel = cmds.ls(sl=1)
        for each in sel:
            on = cmds.toggle(each, q=True, la=True)
            if on == 1:
                cmds.toggle(la=True)
    def loadAwOrientJointTool(self, *args):
        awOJ = awOrientJointInstance.awOrientJoint()
        #awOJ.awOrientJoint()
        
        
        
start = alexWidenerRigger_UI()
start.ui()

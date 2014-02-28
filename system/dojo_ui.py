import maya.cmds as cmds



class Practice_UI:
    
    def __init__(self, *args):
        print 'In _Practice_UI'
        self.UIElements = {}
    #Check and if UI element exist
    def ui(self, *args):
        windowName="Window"
        if cmds.window(windowName, exists=True):
            cmds.deleteUI(windowName)
        windowWidth=100
        windowHeight=100
        buttonWidth=90
        buttonHeight=20
       
        self.UIElements["window"] = cmds.window(windowName, width=windowWidth, height=windowHeight, title="Practice_UI", sizeable=True)
        self.UIElements["guiFlowLayout1"] = cmds.flowLayout(v=False, width=windowWidth, height=windowHeight, bgc=[0.4,0.4,0.4])
        
        #Load Layout Button
        cmds.separator(p=self.UIElements["guiFlowLayout1"])
        self.UIElements["loadLayout_button"]=cmds.button(label='layout', width=buttonWidth, height=buttonHeight, parent=self.UIElements["guiFlowLayout1"], c=self.createLyt)  
        

        #Save Layout Button
        cmds.separator(p=self.UIElements["guiFlowLayout1"])
        self.UIElements["saveLayout_button"]=cmds.button(label='save_layout', width=buttonWidth, height=buttonHeight, parent=self.UIElements["guiFlowLayout1"], c=self.saveLyt)
        
        
        cmds.showWindow(windowName)
        
    def createLyt(self, *args):
        
        loc_info={}
        locator_info=['locCtrl_shld',[0.0,0.0,0.0]], ['locCtrl_elbow', [3.0, 0.0, -2.0]], ['locCtrl', [6.0, 0.0, 0.0]], ['locCtrl_wrist', [8.0, 0.0, 0.0]]

        locList=[]
        for loc in locator_info:
            locLyt=cmds.spaceLocator(name=loc[0], position=loc[1])
            locPiv=cmds.CenterPivot()
            locList.append(locLyt)
            
            


        
    def saveLyt(self, *args):
        print "save"
        


                
                
       


    

        

                

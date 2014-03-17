import maya.cmds as mc
import json
import data.jsonUtils as jsonUtils
import os
import sys
import rigging.trArmRig as trArmRig

UIData="D:/Users/Toby/Documents/GitHub/Python101/data/UIElements"

# UI Class
class RDojo_UI:

    '''
    RDojo UI __Init__ function
    '''
    def __init__(self,*args):
        # Create UIElements dictionary in __init__ making it global
        self.UIElements={}
        # Define common window variables
        self.window="tr_rigginToolWindow"
        self.title="Rigging Tool"
        self.size=(110,100)


    def ui(self,*args):
        # Check to see if window exists
        if mc.window(self.window,exists=True):
            mc.deleteUI(self.window,window=True)
        # create window
        self.UIElements["window"]=mc.window(self.window,title=self.title,sizeable=False,resizeToFitChildren=True)
        buttonHeight=30
        buttonWidth=100
        # create default form layout
        self.UIElements["formLayout1"]=mc.formLayout(numberOfDivisions=100)
        self.UIElements["buildButton"]=mc.button(label="Build Rig",width=buttonWidth,height=buttonHeight,parent=self.UIElements["formLayout1"],command=arm.install)
        self.UIElements["rigModulesTSL"]=mc.textScrollList("Rig_Modules_TSL",parent=self.UIElements["formLayout1"],allowMultiSelection=False)
        self.UIElements["StoreLayoutButton"]=mc.button(label="Write Layout Button",width=buttonWidth,height=buttonHeight,parent=self.UIElements["formLayout1"])
        self.UIElements["RigModuleLabel"]=mc.text(label="Rig Modules")
        mc.formLayout(self.UIElements["formLayout1"],edit=True,
            attachForm=[(self.UIElements["RigModuleLabel"],"top",5),(self.UIElements["buildButton"],"bottom",5),(self.UIElements["buildButton"],"left",5),(self.UIElements["buildButton"],"right",5),
            (self.UIElements["rigModulesTSL"],"left",5),(self.UIElements["rigModulesTSL"],"right",5),(self.UIElements["StoreLayoutButton"],"left",5),(self.UIElements["StoreLayoutButton"],"right",5),
            (self.UIElements["RigModuleLabel"],"right",5),(self.UIElements["RigModuleLabel"],"left",5)],
            attachControl=[(self.UIElements["rigModulesTSL"],"bottom",5,self.UIElements["StoreLayoutButton"]),(self.UIElements["rigModulesTSL"],"top",5,self.UIElements["RigModuleLabel"]),
            (self.UIElements["StoreLayoutButton"],"bottom",5,self.UIElements["buildButton"])],
            attachPosition=[],
            attachNone=[]
            )

        mc.textScrollList(self.UIElements["rigModulesTSL"],edit=True,append=returnMods(filePath))

        jsonUtils.writeJson(UIData,self.UIElements)
        # Show Window
        mc.showWindow(self.window)

    arm = trArmRig.ArmRig()

filePath = "D:/Users/Toby/Documents/GitHub/Python101/rigging"

def findAllFiles(fileDirectory,fileExtension):
    # Return list of file names with extension
    allFiles = os.listdir(fileDirectory)

    # Refine file list to the just files with specified extension
    returnFiles=[]
    for f in allFiles:
        splitString = str(f).rpartition(fileExtension)

        if not splitString[1] == " and splitString[2] == ":
                returnFiles.append(splitString[0])

    return returnFiles

def returnMods(path):
    # search directory for available modules
    allPyFiles = findAllFiles(path,".py")

    returnModules =[]

    for file in allPyFiles:
        if file !="__init__":
            returnModules.append(file)

    return returnModules

arm = trArmRig.ArmRig()

def setRigModule(module,*args):
    import rigging.module as module
    instance =module.TITLE+"()"

    return instance

UIElements=jsonUtils.readJson(UIData)
UIElements=json.loads(UIElements)


def TSLSelection(TSL,*args):
        selectedItem=mc.textScrollList(TSL,query=True,selectItem=True)
        return selectedItem
print(TSLSelection(UIElements["RigModuleLabel"]))
import maya.cmds as cmds, json, os
import pymel.core as pm

class fileManager:

    def __init__(self, *args):
        return None
        

    def write_JSON(self,fileName, info): #writes JSON file of limb joint positions
        with open(fileName, 'w') as outfile:
            json.dump(info,outfile,ensure_ascii=False)


    def get_JSON(self, fileName): #gets the JSON file of the joints' positions
        d = json.load(open(fileName,'r'))
        return d


    def dialogbox(self, message): #dialog box for entering character name for saving and retrieving the file
        result = cmds.promptDialog(
                title='Character',
                message= message,
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
                dismissString='Cancel')

        if result == 'OK':
                name = cmds.promptDialog(query=True, text=True)
                return name


    def createCharFolder(self): #creates a folder to store the character file
        name = self.dialogbox("Character Name")
        newpath = r"C:/"+ name + "/"
        if not os.path.exists(newpath): os.makedirs(newpath)
        self.saveScene(name, newpath)
    
    def saveScene(self, name, newpath): #saves the scene
        file1 = cmds.file(rename=name+".ma")
        cmds.file(save=True, type = 'mayaAscii')
        long =  cmds.file(q=True,sceneName = True)
        short =  cmds.file(q=True, sceneName= True, shortName = True)
        new = newpath+short

        cmds.file(new, type = 'mayaAscii', es=True) 

    def loadScene(self): #loads it as a reference
        name = self.dialogbox("File Name")
        loc =  cmds.file(name, q=True, loc = True)
        cmds.file(loc, r=True)
import maya.cmds as cmds, json, os
import pymel.core as pm

class fileManager:

    def __init__(self, *args):
        print "fileManager!"

    def write_JSON(self,fileName, info):
        '''print fileName
        fout = open(fileName, 'w') #"opens" up file to be written in
        infoDump = json.dumps(info, fout, indent=3) #writes in file
        fout.close()'''
        print type(fileName)

        with open(fileName, 'w') as outfile:
            json.dump(info,outfile,ensure_ascii=False)
            print "yep"
        print "done"

    def get_JSON(self, fileName):
        print "yes"
        d = json.load(open(fileName,'r'))
        print d
        return d





    def dialogbox(self, message):

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


    def createCharFolder(self):
        name = self.dialogbox("Character Name")
        print name
        newpath = r"C:/"+ name + "/"
        if not os.path.exists(newpath): os.makedirs(newpath)
        #different variation of name for file
        self.saveScene(name, newpath)
    
    def saveScene(self, name, newpath):
        #DESEELCT
        file1 = cmds.file(rename=name+".ma")
        cmds.file(save=True, type = 'mayaAscii')
        long =  cmds.file(q=True,sceneName = True)
        short =  cmds.file(q=True, sceneName= True, shortName = True)
        new = newpath+short

        cmds.file(new, type = 'mayaAscii', es=True) 

    def loadScene(self):
        name = self.dialogbox("File Name")
        print cmds.file(name, q=True, ex=True)

        loc =  cmds.file(name, q=True, loc = True)

        cmds.file(loc, r=True)



        #if check is True:
            #cmds.file()



                



    #query file name
    #if file exists, reference it in scene






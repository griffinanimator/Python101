import maya.cmds as cmds, json, os

class fileManager:

    def __init__(self, *args):
        print "fileManager!"

    def write_JSON(self,fileName, info):
        print fileName
        fout = open(fileName, 'w') #"opens" up file to be written in
        infoDump = json.dumps(info, fout, indent=3) #writes in file
        fout.close()
        return infoDump

    def createCharFolder(self):
        result = cmds.promptDialog(
                title='Character Name',
                message='Enter Character Name:',
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
                dismissString='Cancel')

        if result == 'OK':
                text = cmds.promptDialog(query=True, text=True)
                print text
                newpath = r"C:/"+ text
                if not os.path.exists(newpath): os.makedirs(newpath)



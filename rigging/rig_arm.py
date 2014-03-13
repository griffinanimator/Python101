class Joint_UI:

def __init__(self, *args):
print "CreateJoints"
self.jointsInfo={}


def buildJoints(self, prefix, lytObj, *args):
cmds.select(deselect=True)

self.jointsInfo["orientatition"]='xyz'


cmds.select(d=True)
for item in lytObj:
newJointName = prefix+item[0]

if cmds.objExists(newJointName) ==True:
cmds.delete(newJointName)
cmds.select(d=True)

self.jointsInfo["position"]=cmds.joint(n=newJointName, p=item[1], a=True, roo='xyz')
self.jointsInfo["orientation"]=cmds.setAttr(jnt+'.jointOrientX', item[2][0])
self.jointsInfo["orientation"]=cmds.setAttr(jnt+'.jointOrientY', item[2][1])
self.jointsInfo["orientation"]=cmds.setAttr(jnt+'.jointOrientZ', item[2][2])

def jointLength(self, *args):

for j in range(len(info['joints'])):
if j !=0:
cmds.parent(joints[j], joints[j-1])

return joints









   



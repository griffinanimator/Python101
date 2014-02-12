import maya.cmds as mc

#list relatives of selected to get hierarchy
selection = mc.ls(selection = True, type = "joint")
selectedHierarchy = mc.listRelatives(selection, allDescendents = True)

jointList = []
for item in selectedHierarchy:
    itemType = mc.objectType(item)
    print(itemType)

    #if itemType == "joint":
        #item.append(jointList)



print(jointList)
#store this in a list to be iterated through
#for joint in selection:

#use string formating and the rename function to rename the skeleton

#list all joints in scene by type

#use starts with to split list of joints into bind joints and non bind joints.


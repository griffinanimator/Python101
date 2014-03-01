import maya.cmds as cmds, json, io
from maya import OpenMaya
 
                                                               
    
arm_name = { 
'shoulder': 'lctr_l_arm1', 
'elbow': 'lctr_l_arm2', 
'wrist' : 'lctr_l_arm3', 
'palm' : 'lctr_l_armEnd'} #dictonary to store locator names


def build_Locators(): 
    
    data = get_Data() #gets dictionary stored in JSON file 

    for key in data: #builds the locator according to the information in the loc_info dictionary
        locator = cmds.spaceLocator(n=key)[0] #creates the locator at world origin. Avoided using the position(p) flag becuause it positioned according to the local position, not translation
        cmds.xform(locator, t=data[key]) #changes translation of locator according to info in JSON
    #build_Joints()    
    
def get_Data():
    
    locs_pos = write_JSON(arm_name)[0] #locator position
    file = write_JSON(arm_name)[1] #locator name
    data = json.loads(locs_pos) #loads information from JSON file to data variable
    
    return data
    

def write_JSON(arm_name):
    
    loc_info = {
    arm_name['shoulder']: (0, 14.311348, 0.0477619), 
    arm_name['elbow']: (0, 8.52323, -2.195134), 
    arm_name['wrist']:(0, 1.613664, -0.422523), 
    arm_name['palm']: (0, 0.492216, 0.373344) 
    } #dictionary to store "default" locator positions
    
    file = "C:\Users\Sarah\Documents\GitHub\Python101\data\loc_info.json"
    fout = open(file, 'w') #"opens" up file to be written in
    locDump = json.dumps(loc_info, fout, indent=3) #writes in file
    fout.close() 
    
    return locDump, file
   

def build_Joints():
    jnt = []
    position = get_Data()
    cmds.select(d=True) #deselects locator so joints won't be parented to it
    for key in sorted(position): #sorted so joints will be in correct order
        name = key.replace('lctr','jnt')
        locPos = cmds.xform(key, q=True, t=True, ws = True) #gets locator position
        buildJnt= cmds.joint(n=name, p=locPos) #creates joints in locator's position
        jnt.append(buildJnt)
        cmds.delete(key) #deletes locator
    
    for i  in range(len(jnt)):
        cmds.joint(jnt[i], e=True, zso = True, oj = 'xyz')
 
    build_Ik(jnt)
    
       
      
def build_Fk(jnt):
    fkctrl = []
    fkgroup = []
    cmds.select(d=True) 
    for i in range(len(jnt)-1): # creates ctrls for all joints but the palm
        jntpos = cmds.xform(jnt[i], q=True, t=True, ws = True)
        name = jnt[i].replace('jnt', 'ctrl_fk')
        circle = cmds.circle(n=name, nr= (1,0,0), r = 1)
        cmds.xform(circle, t=jntpos)
        grp = cmds.group(circle, n ="grp_" + name) #groups for controls
        cmds.parentConstraint(jnt[i], grp, mo=False) #temporary parent constraint to get right angle for control
        cmds.parentConstraint(jnt[i], grp, e=True, rm=True)
         
        fkgroup.append(grp)
        cmds.parentConstraint(circle, jnt[i])
        
        fkctrl.append(circle)
        
    for i in range(1, len(fkctrl)): #parent const ctrls to the upper in heirarchy for all controls but the first one
        cmds.parentConstraint(fkctrl[i-1], fkgroup[i], mo = True)
        
         
def build_Ik(jnt): 
    ikrpName= jnt[0].replace('jnt', 'ikRP')
    ikname = jnt[0].replace('jnt', 'ctrl_ik') 
    wristjnt = jnt[len(jnt)-2]
    
    jntpos = cmds.xform(jnt[len(jnt)-2], q=True, t=True, ws = True)
    
    pv_ctrl = poleVectorPos(jnt)
    
    ikrp = cmds.ikHandle(n=ikrpName, sj = jnt[0], ee= wristjnt, solver = 'ikRPsolver')
    
    cmds.poleVectorConstraint(pv_ctrl, ikrpName)
   
    
    #create control
    ikcon = cmds.circle(n=ikname, nr= (1,0,0), r = 1.5)
    cmds.xform(ikname, t=jntpos)
    grp =  cmds.group(ikname, n ="grp_" + ikname)
    cmds.parentConstraint(wristjnt, grp, mo=False)
    cmds.parentConstraint(wristjnt, grp, e=True, rm=True)
    
    cmds.pointConstraint(ikcon, ikrpName)

    cmds.orientConstraint(ikcon, wristjnt)
    
    cmds.pointConstraint(ikcon, pv_ctrl, mo=True) #contrains pv to wrist handle
    
    
def poleVectorPos(jnt):

    #get positions of joints
    start = cmds.xform(jnt[0], q = 1, ws = 1, t = 1) # shoulder
    mid = cmds.xform(jnt[1], q = 1, ws = 1, t = 1) #elbow
    end = cmds.xform(jnt[2], q = 1, ws = 1, t = 1)#wrist

    #create get the xyz vector postion of each joint
    startV = OpenMaya.MVector(start[0], start[1], start[2])
    midV = OpenMaya.MVector(mid[0], mid[1], mid[2])
    endV = OpenMaya.MVector(end[0], end[1], end[2])


    startEnd  = endV - startV
    startMid = midV - startV

    dotP = startMid * startEnd
    proj = float(dotP) / float(startEnd.length())


    startEndN = startEnd.normal() #return normalized value 

    projV = startEndN * proj #figure projection vector

    arrowV = startMid - projV

    finalV = arrowV + midV

    loc = cmds.spaceLocator(n = "armPV")[0]
    cmds.xform(loc, ws =1, t =(finalV.x, finalV.y, finalV.z))
    
    return loc

            
    

#build_Locators() 
#build_Joints()       

     
    

    
    

                                                                            

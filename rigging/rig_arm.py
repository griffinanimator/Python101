import maya.cmds as cmds, json, io   
                                                                

    
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
    
    position = get_Data()
    cmds.select(d=True) #deselects locator so joints won't be parented to it
    for key in sorted(position): #sorted so joints will be in correct order
        name = key.replace('lctr','jnt')
        locPos = cmds.xform(key, q=True, t=True, ws = True) #gets locator position
        test= cmds.joint(n=name, p=locPos) #creates joints in locator's position
        cmds.delete(key) #deletes locator
       
      
    
       
    

#build_Locators()        
#build_Joints()
     
    
#def build_Ik():
    
    
#def build_Fk():
                                                                            

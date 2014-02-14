import maya.cmds as cmds, json, io

arm_name = { 
'shoulder': 'lctr_l_arm1', 
'elbow': 'lctr_l_arm2', 
'wrist' : 'lctr_l_wrist', 
'palm' : 'lctr_l_armEnd'} #dictonary to store locator names
  
 
loc_info = {
arm_name['shoulder']: (0, 14.311348, 0.0477619), 
arm_name['elbow']: (0, 8.52323, -2.195134), 
arm_name['wrist']:(0, 1.613664, -0.422523), 
arm_name['palm']: (0, 0.492216, 0.373344)

} #dictionary to store locator locations
 
                                                                                 

def build_Locators(loc_dict):                                                                                      
    for loc in loc_info: #builds the locator according to the information in the loc_info dictionary
      
        locator = cmds.spaceLocator(n=loc, p=loc_info[loc]) 
        print loc  #prints locator name from the dictionary
        print loc_info[loc]  #prints locator position from the dictionary
     
    write_JSON(loc_dict)
        

def write_JSON(loc_dict):
    fout = open("C:\Users\Sarah\Documents\GitHub\Python101\data\loc_info.json", 'w') #figure out file directories
    json.dump(loc_info, fout, indent=3)
    fout.close()                                                                                
    
build_Locators(loc_info) 
import maya.cmds as cmds

# This is the base command for creating a joint.
cmds.joint(name='jnt1') 


""" Looking at the Python Command Reference you will see that cmds.joint 
has several flags that can be used.
Next to each flag you will see the properties of that flag.
The properties indicate if the flag can be used in "Edit", "Query", or "Edit" mode.
"""
# We can position the joint by using the p flag.  
# Lets delete the previous joint and create a new one with a specified position.
cmds.delete('jnt1')
cmds.joint(name='jnt1', p=[0.0, 0.0, 2.0])


# We can also use the position flag in edit mode.
cmds.joint('jnt1', edit=True, p=[2.0, 0.0, 4.0])

# Now lets look at some other usefull commands


# cmds.getAttr
""" getAttr will return the value of the queried attribute.
In this example we will get the translateX value of joint1 """
print cmds.getAttr('jnt1.translateX')

""" We can also set attributes using cmds.setAttr """
cmds.setAttr('jnt1.translateX', 4)



""" Now let's create a second joint so we can use cmds.connectAttr
to connect the translate x of joint1 to the translate y of the new joint
"""
# NOTE:  If a joint is selected when we make a new joint, the
# 2 joints will end up in a hierarchy.  Let's clear our selection
cmds.select(d=True)
cmds.joint(name='jnt2', p=[0.0, 0.0, 2.0])
cmds.connectAttr('jnt1.translateX', 'jnt2.translateY')
# Try moving joint1 in the x axis to see the result

"""
We have learned how to create some joints and manipulate
the joints attributes.  Now we will look at a way to create a 
chain of joints quickly.  Note that this is just one method.
We will take this even farther later on.
"""
"""
To get the job done efficiently we must introduce variables, lists, and loops.
A variable is a container of sorts that will store any data that you give it.
In this example "var" will serve as a variable. 
"""
var = ('a')
print var

""" A list is exactly what the name implies.  In this example
we will make a list of items.
"""
var = ('a', 'b', 'c')
print var

""" As you can see, var is now equal to a list of 3 items ('a', 'b', 'c').
If we want to acess the individual items, we need to use a loop.  There are
different kinds of loops but we will start with the "for" loop. 
NOTE: Pythone relies on white space to indicate that we are in a loop.  
Simply use the "Tab" button to create this space. """

for item in var:
    print item
    
""" This is pretty easy so far right? Lets try this with our joints """
jointList = ('jnt_shldr', 'jnt_elbow', 'jnt_wrist')
for j in jointList:
    cmds.joint(n=j)
    
""" Now we have 3 joints in our scene, but they are all in the same spot.
We need a way to position these joints.  This is where nested lists come in.
Before we get into that we need to understand what an index is.  To demonstrate, 
I will use another type of for loop. """

for j in range(len(jointList)):
    print j
    
""" Do you see how the numbers 1, 2, and 3 are printed out?
This numbers indicate that items position or index in the jointList.
Now try this. """

for j in range(len(jointList)):
    print j
    print jointList[j] # The "[]" are used to indicate the index number
    
""" This idea of index numbers includes items in a nested list as well.
Try this example and look at the print out """

jointList = (['jnt_shldrA',[0.0, 0.0, 2.0]], ['jnt_elbowA',[0.0, 2.0, 5.0]], ['jnt_wristA',[0.0, 0.0, 8.0]])
cmds.select(d=True)
for j in range(len(jointList)):
    print j
    print jointList[j][0]
    print jointList[j][1]
    cmds.joint(n=jointList[j][0], p=jointList[j][1])
    



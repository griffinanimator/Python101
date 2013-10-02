Welcome to Python scripting 101.  This syllabus will give you an outline of the material we will be covering in this session.  In this course you will learn the core concepts required to write tools for Autodesk Maya.  Your job will be to use each week's lesson to build a character rigging tool.   I will provide video lectures as well as scheduled one on one time.  Each week you will receive an assignment which should be completed before the beginning of the next week.  I encourage you all to stay active in the class threads.  Ask a lot of questions and help eachother out.  I will provide the basic structure for the rigging tool, and will be available to answer any questions if you get stuck.

Setup (Week 1)
Install Python 2.7
Choosing and using an IDE.
Wing, Eclipse, Sublime.
IDE Basics.
Interpreter.
Project settings, preferences, add ons, and other tips.
Running Python from Sublime.
Using a Code Repository
Setting up Git.
Link to Session1 Git Repo
Git for Windows
Setting Up Your Tool Set
userSetup.py
Setting environment variables.
Testing your environment with sys.path

Week 1 Assignment:  
Instal an IDE, and setup the Session 1 project.
Create a new file called Week1.py and save it in the Modules folder.
Use Git to push your new file to the repo.

An Introduction to Python in Maya (Week 2)
What is Python and how is it implemented in Maya?   Documentation
Understanding how you can do anything you could do manually in Maya by using .cmds
Create objects (joint, locator).
Edit attributes.
Print statements.

Python command reference, and the script editor output.
New command window.
Show output and line numbers.
Clearing the output window.

Week 2 Assignment:  
Explore the Python Command Reference.  
Set the Maya script editor to echo all commands.  Create some objects in Maya, locate the command in the output , and lookup the command in the Python reference.
The Basics of Python. (Week 3)
Python modules and the Python reference.   http://docs.python.org/2/reference/
Basic concepts.
Loops
Conditions
Syntax
Data types
Operations
Lists
Dictionaries
Commenting
Error Checking and debugging.
Project structure and importing modules.

Week 3 Assignment:
Create a for loop that creates 4 locators with the names (‘lctr_l_arm1’, ‘lctr_l_arm2’, ‘lctr_l_wrist’, lctrr_l_armEnd’).  We will do this with a dictionary called ‘locator_info.
Add print statements to print the locator name and it’s position in ‘locator_info’.
Save the data in locator_info to a JSON file.

Customize your Maya environment with startup.py ( Week 4 )
Load project settings 
Use UI modules to create a RDojo menu to access your tools.

Week 4 Assignment:
Create ‘startup.py in the root of the project folder.
Set some preferences like frame rate, units, and a default project.
Make a RDojo menu that loads when Maya starts.

Building Your First Tool (Week 5)
A quick course in rigging an arm.
Load locator_info from JSON.
Position your locators and save the now locator_info to JSON.
Build joints based off the locators positions and names.
Draw an IK handle to manipulate the joints.
Create a controller and parent the IKHandle to the controller.
Setup FK controls.

Week 5 Assignments:
Build a module to generate an arm rig.
Consider how this module could be used to generate a leg.
Getting More Advanced (Week 5)
Classes
List comprehension 
Arguments
Return
Maya UI Construction
Create a window, a layout, and a button.
Have the button call on the Build_Arm class.

Week 5 Assignments:
Create a UI with a rig arm button.  
Add a UI call button to your custom menu.
Have the rig arm button run the rigArm script
Bonus:  Make a button that creates 4 locators.
Navigating a project (Week 6)
Create files and folders.
Move around your project.
Load files.

Week 6 Assignments:
Create a folder for a specific character.
Generate an arm rig and save it to that folder.
Reference your rig into a new scene.
Save that scene as a .ma and push it to the repo.


Refine your tool (Week 7)
Look at making your rigging tool more versatile.
Setup your module so it can be used as a basis for building a leg.
Replace locators with something more user friendly.
Use utility files to pull common code out of individual modules.

Week 7 Assignments:
Edit your code to make it more modular and streamlined.

Week 8 Filling In The Blanks
Go over any concepts that need clarification.
Continue refining the arm rig.
Continue refining the code.
Discuss PyMel, and PySide.

Week 8 Assignments:
Continue learning Python.
Get faster at your day to day work.




Core Concepts:
Understand basic to advanced Python concepts.
Understand the purpose and have the ability to use repositories, external editors, and documentation.
Understand how to design and implement a tool set by using a rigging tool as an example.
Know how to make a basic UI.
Gain a more thorough understanding of the Maya environment.
Learn to read and write external data.





Resources
Python Command Reference
Code Academy
PyQt
PySide
Tech-Artists.org
PyMel


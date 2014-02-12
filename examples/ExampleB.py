# ExampleB.py

import maya.cmds as cmds

print "Hello.  We are in ExampleB"

class Example_Class:
	def Import_Module(self):
		import ExampleC as exc
		reload(exc)
		print exc
		info = "Python is Fun"
		exc.PrintInfo(info)

		self.PrintInfo()

		tmpVar = exc.DoStuff()
		print tmpVar


	def PrintInfo(self):
		print "ExampleB Info"
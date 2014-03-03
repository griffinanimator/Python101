import Modules.Import_Example as Import_Example
"""
You can place information outside of the class.
Similar to __init__, this information will be available
when you import this module.
"""
TITLE = "Arm"

class Get_Module:
	print "Get_Module"

	def __init__(self):
		""" Here you can see the instance associated with the
		imported instance of Import_Example """
		print "Imported instance of Import_Example"
		print Import_Example


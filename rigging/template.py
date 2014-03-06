#
#User Interface creation for Maya
#

from PyQt4 import QtGui, QtCore, uic
from pymel.core import *
import pymel.core as pm
fromt pymel import *

#Path to the designer UI file
ui_filename = 'R:/RD Github/Python101/rigging/makeCube.ui'
form_class, base_class = uic.loadUiType(ui_filename)

#Interface class
class Interface(base_class, form_class):
    def __inti__(self):
                super(base_class, self).__init__()
                self.setupUi(self)
                self.setObjectName('makeCube')
                self.setDockNestingEnabled(True)
                self.connectInterface()
    def connectInterface(self):
        QtCore.QObject.connect(self.makeCube, QtCore.SIGNAL("clicked()"), self.makeCubeWin)
    def makeCubeWin(self):
        mel.eval('')

#main
def main():
        global ui
        ui=interface()
        ui.show()

if __name__ == "__main__":
    main()

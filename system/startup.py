import os
import sys

print sys.path

sys.path.append("C:/Users/Ganapathi K A/Documents/GitHub/Python101/")

def loadUI(*args):
    import system.dojo_ui as dojoui
    dojoui = dojoui.RDojo_UI()
    dojoui.ui()

import startup as startup
reload (startup)
print startup
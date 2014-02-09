import os
import sys

print sys.path

sys.path.append("C:/Users/Ganapathi K A/Documents/GitHub/Python101/")
sys.path.append(os.environ['RDOJO'])
sys.path.append('R:')
import startup as startup
reload (startup)
print startup
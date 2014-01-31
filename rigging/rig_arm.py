import maya.cmds as cmds

cmds.joint(p=(0, 14.311348, 0.0477619))
cmds.joint(p=(0, 8.52323, -2.195134))
cmds.joint('joint1', e=True, zso = True, oj = 'xyz', sao = 'yup')
cmds.joint(p=(0, 1.613664, -0.422523))
cmds.joint('joint2', e=True, zso = True, oj = 'xyz', sao = 'yup')
cmds.joint(p=(0, 0.492216, 0.373344))
cmds.joint('joint3', e=True, zso = True, oj = 'xyz', sao = 'yup')
cmds.joint(p=(0, -0.737759, 1.060683))
cmds.joint('joint4', e=True, zso = True, oj = 'xyz', sao = 'yup')

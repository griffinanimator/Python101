import maya.cmds as cmds
class presetUI():
    def __init__(self):
        if cmds.window('presetUI', exists=True):
            cmds.deleteUI('presetUI')
        self.widgets = {}
        self.widgets["window"] = cmds.window("presetUI", title="Presets", w=500, h=300, mnb=False, mxb=False, sizeable=False)
        self.widgets["formLayout"] = cmds.formLayout(w=500, h=300)
        self.widgets["floatField"] = cmds.floatFieldGrp(numberOfFields=3, label="Position", value1 = 0.0, value2 = 0.0, value3 = 0.0)
        self.widgets["floatSlider"] = cmds.floatSliderGrp(label="Example", field = True, minValue = -10, maxValue = 10, fieldMinValue = -10, fieldMaxValue = 10, value = 0)
        self.widgets["radioButtonGrp"] = cmds.radioButtonGrp(label="Radio Buttons", labelArray3 = ["Yes", "No", "Maybe"], numberOfRadioButtons=3)
        self.widgets["inputTextField"] = cmds.textField(w=300, h=30, text="Input Directory", enable=False)
        self.widgets["outputTextField"] = cmds.textField(w=300, h=30, text="Output Directory", enable=False)
        self.widgets["inputButton"] = cmds.button(w=30, h=30, label='...')
        self.widgets["outputButton"] = cmds.button(w=30, h=30, label='...')        
        self.widgets["swatch"] = cmds.canvas(rgbValue=(0, 0, 1), width=50, height=50)
        self.widgets["colorEditor"] = cmds.button(label='Color Editor', w=100, h=50)
        self.widgets["checkBox1"] = cmds.checkBox(label='Yes', v=0)
        self.widgets["checkBox2"] = cmds.checkBox(label='Yes', v=0)
        
        #place controls
        #attach form is af, look it up
        cmds.formLayout(self.widgets["formLayout"], edit=True, af=[(self.widgets["floatField"], 'top', 10), (self.widgets["floatField"], 'left', 5)])
        cmds.formLayout(self.widgets["formLayout"], edit=True, af=[(self.widgets["floatSlider"], 'top', 40), (self.widgets["floatSlider"], 'left', 5)])        
        cmds.formLayout(self.widgets["formLayout"], edit=True, af=[(self.widgets["radioButtonGrp"], 'top', 70), (self.widgets["radioButtonGrp"], 'left', 5)])        
        cmds.formLayout(self.widgets["formLayout"], edit=True, af=[(self.widgets["inputTextField"], 'top', 100), (self.widgets["inputTextField"], 'left', 5)])        
        cmds.formLayout(self.widgets["formLayout"], edit=True, af=[(self.widgets["outputTextField"], 'top', 135), (self.widgets["outputTextField"], 'left', 5)])        
        cmds.formLayout(self.widgets["formLayout"], edit=True, af=[(self.widgets["inputButton"], 'top', 100), (self.widgets["inputButton"], 'left', 305)])        
        cmds.formLayout(self.widgets["formLayout"], edit=True, af=[(self.widgets["outputButton"], 'top', 135), (self.widgets["outputButton"], 'left', 305)])        
        cmds.formLayout(self.widgets["formLayout"], edit=True, af=[(self.widgets["swatch"], 'top', 170), (self.widgets["swatch"], 'left', 0)])        
        cmds.formLayout(self.widgets["formLayout"], edit=True, af=[(self.widgets["colorEditor"], 'top', 170), (self.widgets["colorEditor"], 'left', 55)])        
        cmds.formLayout(self.widgets["formLayout"], edit=True, af=[(self.widgets["checkBox1"], 'top', 180), (self.widgets["checkBox1"], 'left', 160)])        
        cmds.formLayout(self.widgets["formLayout"], edit=True, af=[(self.widgets["checkBox2"], 'top', 180), (self.widgets["checkBox2"], 'left', 100)])        



        cmds.showWindow(self.widgets["window"])
        cmds.window(self.widgets["window"], edit=True, w=500, h=300)
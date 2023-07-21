import maya.cmds as cmds
import math

class Rocket(object):

    def __init__(self, bodyParts = 3, noseConeHeight = 2, fuelTanks = 2):
        self.bodyParts = bodyParts
        self.noseConeHeight = noseConeHeight
        self.fuelTanks = fuelTanks

        
    def _creatParts(self):

        grp = cmds.group(empty=1, n="MyRocket_Group")

        for i in range(self.bodyParts):
            body = cmds.polyCylinder(name=self._getBodyPartName(i))

            cmds.parent(body, grp)

        self.body_part_radius = cmds.polyCylinder(self._getBodyPartName(0), q=1, radius=1)
        self.body_part_height = cmds.polyCylinder(self._getBodyPartName(0), q=1, height=1)

        for i in range(self.fuelTanks):
        
            tank = cmds.polyCone(name=self._getFuelTankName(i), radius=self.body_part_radius*math.sin(math.pi / self.fuelTanks))
            cmds.parent(tank, grp)

        self.fuel_tank_height = cmds.polyCone(self._getFuelTankName(0), q=1, height=1)

        self.nose_cone = cmds.polyCone(name="noseCone", height = self.noseConeHeight)
        cmds.parent(self.nose_cone, grp)
        

    def generateModel(self):
        self._creatParts()
        for i in range(self.fuelTanks):
            alpha = i * 2.0 * math.pi / self.fuelTanks
            x = self.body_part_radius * math.sin(alpha)
            y = self.body_part_radius * math.cos(alpha)
            cmds.xform(self._getFuelTankName(i), t=[x,self.fuel_tank_height/2, y], r=1) 

        for i in range(self.bodyParts):
            cmds.xform(self._getBodyPartName(i), t=[0,self.fuel_tank_height+self.body_part_height/2+self.body_part_height*i,0], r=1)

        cmds.xform(self.nose_cone, t=[0,self.fuel_tank_height + (self.noseConeHeight/2.0) + (self.body_part_height*self.bodyParts),0], r=1)

        print (self.fuel_tank_height)
        print (self.noseConeHeight)
        print (self.body_part_height)
        print (self.bodyParts)


    def _getFuelTankName(self,i):
        return "fuelTank_{}".format(i)

    def _getBodyPartName(self,i):
        return "bodyPart_{}".format(i)

    
my_rocket = Rocket (bodyParts = 4, noseConeHeight = 4, fuelTanks = 10)
my_rocket.generateModel()

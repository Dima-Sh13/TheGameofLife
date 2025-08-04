from utils import *
import random as ra


"""
pg.draw.rect(self.mainScreen,color_negro,(self.screenX-self.screenX,self.screenY-self.screenY,self.screenX//3,self.screenY//4))
pg.draw.rect(self.mainScreen,color_verde,(self.screenX-self.screenX+5,self.screenY-self.screenY +5,self.screenX//3-10,self.screenY//4-10))
pg.draw.rect(self.mainScreen,color_negro,(self.screenX//3,self.screenY-self.screenY,self.screenX//3,self.screenY//4))
pg.draw.rect(self.mainScreen,color_verde,(self.screenX//3+5,self.screenY-self.screenY +5,self.screenX//3-10,self.screenY//4-10))
pg.draw.rect(self.mainScreen,color_negro,(self.screenX-self.screenX//3-2,self.screenY-self.screenY,self.screenX//3,self.screenY//4))
pg.draw.rect(self.mainScreen,color_verde,(self.screenX-self.screenX//3+5,self.screenY-self.screenY +5,self.screenX//3-10,self.screenY//4-10))


pg.draw.rect(self.mainScreen,color_negro,(self.screenX-self.screenX,self.screenY//4-5,self.screenX//3,self.screenY//4))
pg.draw.rect(self.mainScreen,color_verde,(self.screenX-self.screenX+5,self.screenY//4 ,self.screenX//3-10,self.screenY//4-10))


pg.draw.rect(self.mainScreen,color_negro,(self.screenX//3,self.screenY-self.screenY,self.screenX//3,self.screenY//4))
pg.draw.rect(self.mainScreen,color_verde,(self.screenX//3 +5,self.screenY-self.screenY-5,self.screenX//3-10,self.screenY//4-10))
"""

nombre = ""
for i in range(1,8):
    i = abcdario[ra.randint(1,25)] 
    nombre += i

print(nombre.capitalize())    
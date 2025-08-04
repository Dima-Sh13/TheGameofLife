import pygame as pg
from utils import *
from functions import time


pg.display.set_caption("Life")
refreshT = pg.time.Clock()



class Partida():
    def __init__(self):
        pg.init()
        self.screenX = 1060
        self.screenY = 790
        self.mainScreen = pg.display.set_mode((self.screenX, self.screenY))
        pg.display.set_caption("Life")
        self.generation = 0
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour = 0
        self.refreshT = pg.time.Clock()
    def time(self):
        hour += 1
        if self.hour >24:
                day +=1
                hour = 0
        if self.day > 30:
                month +=1
        if self.month > 12:
                year +=1
                month = 0  
        if self.year > 30:
                generation +=1
    def bucleLife(self):
        gameOn = True
        while gameOn:
            self.refreshT.tick(1)
            for eventos in pg.event.get():
                if eventos.type == pg.QUIT:
                    gameOn = False
            self.draw_world()
            self.mainScreen.fill((color_blanco))
            pg.draw.rect(self.mainScreen,color_negro,(self.screenX-self.screenX,self.screenY-self.screenY,self.screenX//3,self.screenY//4))
            pg.draw.rect(self.mainScreen,color_verde,(self.screenX+5,self.screenY +5,self.screenX//3-10,self.screenY//4-10))
            pg.draw.rect(self.mainScreen,color_negro,(self.screenX//3,self.screenY-self.screenY,self.screenX//3,self.screenY//4))
            pg.draw.rect(self.mainScreen,color_verde,(self.screenX//3 +5,self.screenY-self.screenY-5,self.screenX//3-10,self.screenY//4-10))
            
            pg.display.flip()
    def draw_world (self):
        pg.draw.rect(self.mainScreen,color_negro,(self.screenX//3,self.screenY,self.screenX//3,self.screenY//4))
    
class Persona():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.sex = ""
        self.health = True
        self.hunger = 0
        self.thirst = 0

    def dibujar(self,surface):
        pass
        #pg.draw.rect(surface,(1,1,1),(self.pos_x,self.pos_y,self.w,self.h)) 
         
         
juego = Partida()
juego.bucleLife()    
    
    
    
    




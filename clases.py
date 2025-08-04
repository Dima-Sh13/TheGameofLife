import pygame as pg
from utils import *


class Celda():
    def __init__(self, pos_x, pos_y):
        self.population = 0
        self.woods = 0
        self.water = 0
        self.alive = True
        self.happines = 0
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw(self,screenX,screenY,mainScreen):
        pg.draw.rect(mainScreen,color_negro,(self.pos_x,self.pos_y,screenX//3,screenY//4))
        pg.draw.rect(mainScreen,color_verde,(self.pos_x+5,self.pos_y +5,screenX//3-10,screenY//4-10))    


class Persona():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.sex = ""
        self.health = True
        self.hunger = 0
        self.thirst = 0

    def dibujar(self,surface, limit):
        pass
        pg.draw.rect(surface,color_negro,(self.pos_x,self.pos_y,self.w,self.h))
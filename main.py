import pygame as pg
from utils import *
from functions import time
from clases import Celda, Persona
import random as ra

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
           
            self.mainScreen.fill((color_blanco))
            celda1.draw(self.screenX,self.screenY,self.mainScreen)
            pg.display.flip()
   
    
 
         
         
juego = Partida()
celda1 = Celda(screenX-screenX,screenY-screenY)    
juego.bucleLife()    
    
    
    




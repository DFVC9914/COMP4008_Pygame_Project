#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:24:39 2020
@author: Chao Cui
"""

import pygame
import os
Images_Path = os.getcwd()
# Global variables
Screen_Width = 500
Screen_Height = 200
Fps = 15
   
# The background of the game
class Game_Map() :
    def __init__(self,x,y,image):
        self.x = x
        self.y = y
        self.image = image

    def Map_Move(self):
        if self.x < -(Screen_Width-10) :  
            self.x = Screen_Width   
        else:
            self.x -= 10  

    def Map_Update(self):
        Screen.blit(pygame.image.load(os.path.join(self.image)).convert(), (self.x, self.y))

# 
class Game_Role():
    def __init__(self) :
        self.rect = pygame.Rect(0, 0, 0, 0)  # 小恐龙矩形图片的初始化,Rect(left,top,width,height)
        self.jumpHeight = 130
        self.jumpState = False  # 跳跃状态，true为跳跃
        self.lowest_y = 140  # 最低坐标
        self.jumpValue = 0  # 跳跃增变量

# Initialising pygame
pygame.init()
# creating the display with WIDTH and HEIGHT
Screen = pygame.display.set_mode((Screen_Width,Screen_Height))
# Set the title of the game
pygame.display.set_caption("CWG's Game")
Fps_Flash = pygame.time.Clock()
bg1 = Game_Map(0, 20,"1.png")
bg2 = Game_Map(500, 20,"2.png")

event = pygame.event.poll()
while True:
    bg1.Map_Update()
    bg1.Map_Move()
    bg2.Map_Update()
    bg2.Map_Move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()# for the rest of the people with windows or Linux
            os._exit(0) # for Mac users.
    pygame.display.flip()      
    Fps_Flash.tick(Fps)